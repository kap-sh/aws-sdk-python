"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#UpdateFormData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.fields_map
    import capo_amplifyuibuilder.types.form_action_type
    import capo_amplifyuibuilder.types.form_cta
    import capo_amplifyuibuilder.types.form_data_type_config
    import capo_amplifyuibuilder.types.form_name
    import capo_amplifyuibuilder.types.form_style
    import capo_amplifyuibuilder.types.label_decorator
    import capo_amplifyuibuilder.types.sectional_element_map


class UpdateFormData(TypedDict, closed=True):
    name: NotRequired["capo_amplifyuibuilder.types.form_name.FormName"]
    """<p>The name of the form.</p>"""
    data_type: NotRequired[
        "capo_amplifyuibuilder.types.form_data_type_config.FormDataTypeConfig"
    ]
    """<p>The type of data source to use to create the form.</p>"""
    form_action_type: NotRequired[
        "capo_amplifyuibuilder.types.form_action_type.FormActionType"
    ]
    """<p>Specifies whether to perform a create or update action on the form.</p>"""
    fields: NotRequired["capo_amplifyuibuilder.types.fields_map.FieldsMap"]
    """<p>The configuration information for the form's fields.</p>"""
    style: NotRequired["capo_amplifyuibuilder.types.form_style.FormStyle"]
    """<p>The configuration for the form's style.</p>"""
    sectional_elements: NotRequired[
        "capo_amplifyuibuilder.types.sectional_element_map.SectionalElementMap"
    ]
    """<p>The configuration information for the visual helper elements for the form. These elements are not associated with any data.</p>"""
    schema_version: NotRequired["str"]
    """<p>The schema version of the form.</p>"""
    cta: NotRequired["capo_amplifyuibuilder.types.form_cta.FormCTA"]
    """<p>The <code>FormCTA</code> object that stores the call to action configuration for the form.</p>"""
    label_decorator: NotRequired[
        "capo_amplifyuibuilder.types.label_decorator.LabelDecorator"
    ]
    """<p>Specifies an icon or decoration to display on the form.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFormData) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "data_type" in value:
        import capo_amplifyuibuilder.types.form_data_type_config

        out["dataType"] = (
            capo_amplifyuibuilder.types.form_data_type_config.serialize_json(
                value["data_type"]
            )
        )
    if "form_action_type" in value:
        import capo_amplifyuibuilder.types.form_action_type

        out["formActionType"] = (
            capo_amplifyuibuilder.types.form_action_type.serialize_json(
                value["form_action_type"]
            )
        )
    if "fields" in value:
        import capo_amplifyuibuilder.types.fields_map

        out["fields"] = capo_amplifyuibuilder.types.fields_map.serialize_json(
            value["fields"]
        )
    if "style" in value:
        import capo_amplifyuibuilder.types.form_style

        out["style"] = capo_amplifyuibuilder.types.form_style.serialize_json(
            value["style"]
        )
    if "sectional_elements" in value:
        import capo_amplifyuibuilder.types.sectional_element_map

        out["sectionalElements"] = (
            capo_amplifyuibuilder.types.sectional_element_map.serialize_json(
                value["sectional_elements"]
            )
        )
    if "schema_version" in value:
        out["schemaVersion"] = value["schema_version"]
    if "cta" in value:
        import capo_amplifyuibuilder.types.form_cta

        out["cta"] = capo_amplifyuibuilder.types.form_cta.serialize_json(value["cta"])
    if "label_decorator" in value:
        out["labelDecorator"] = value["label_decorator"]
    return out


def deserialize_json(data: dict) -> UpdateFormData:
    out: UpdateFormData = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "dataType" in data:
        import capo_amplifyuibuilder.types.form_data_type_config

        out["data_type"] = (
            capo_amplifyuibuilder.types.form_data_type_config.deserialize_json(
                data["dataType"]
            )
        )
    if "formActionType" in data:
        import capo_amplifyuibuilder.types.form_action_type

        out["form_action_type"] = (
            capo_amplifyuibuilder.types.form_action_type.deserialize_json(
                data["formActionType"]
            )
        )
    if "fields" in data:
        import capo_amplifyuibuilder.types.fields_map

        out["fields"] = capo_amplifyuibuilder.types.fields_map.deserialize_json(
            data["fields"]
        )
    if "style" in data:
        import capo_amplifyuibuilder.types.form_style

        out["style"] = capo_amplifyuibuilder.types.form_style.deserialize_json(
            data["style"]
        )
    if "sectionalElements" in data:
        import capo_amplifyuibuilder.types.sectional_element_map

        out["sectional_elements"] = (
            capo_amplifyuibuilder.types.sectional_element_map.deserialize_json(
                data["sectionalElements"]
            )
        )
    if "schemaVersion" in data:
        out["schema_version"] = data["schemaVersion"]
    if "cta" in data:
        import capo_amplifyuibuilder.types.form_cta

        out["cta"] = capo_amplifyuibuilder.types.form_cta.deserialize_json(data["cta"])
    if "labelDecorator" in data:
        out["label_decorator"] = data["labelDecorator"]
    return out
