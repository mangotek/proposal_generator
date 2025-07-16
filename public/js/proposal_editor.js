// proposal_generator/public/js/proposal_editor.js

frappe.ui.form.on("Proposal", {
    refresh(frm) {
        if (!frm.is_new() && !window.quillEditorInitialized) {
            let container = frm.fields_dict.layout_html.$wrapper;
            container.empty();
            let editorDiv = $(`<div id="quill-editor" style="height:400px;"></div>`);
            container.append(editorDiv);

            const quill = new Quill('#quill-editor', {
                theme: 'snow',
                modules: {
                    toolbar: [
                        [{ 'header': [1, 2, false] }],
                        ['bold', 'italic', 'underline'],
                        [{ 'list': 'ordered'}, { 'list': 'bullet' }],
                        ['link', 'image']
                    ]
                }
            });

            if (frm.doc.layout_html) {
                quill.clipboard.dangerouslyPasteHTML(frm.doc.layout_html);
            }

            window.quillEditorInitialized = true;

            frm.save_custom = () => {
                frm.set_value("layout_html", quill.root.innerHTML);
                return true;
            };
        }
    }
});
