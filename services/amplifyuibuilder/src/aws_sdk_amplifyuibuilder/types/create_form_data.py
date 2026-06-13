"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#CreateFormData``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_amplifyuibuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.fields_map
    import aws_sdk_amplifyuibuilder.types.form_action_type
    import aws_sdk_amplifyuibuilder.types.form_cta
    import aws_sdk_amplifyuibuilder.types.form_data_type_config
    import aws_sdk_amplifyuibuilder.types.form_name
    import aws_sdk_amplifyuibuilder.types.form_style
    import aws_sdk_amplifyuibuilder.types.label_decorator
    import aws_sdk_amplifyuibuilder.types.sectional_element_map
    import aws_sdk_amplifyuibuilder.types.tags


class CreateFormData(TypedDict):
    name: "aws_sdk_amplifyuibuilder.types.form_name.FormName"
    """<p>The name of the form.</p>"""
    data_type: "aws_sdk_amplifyuibuilder.types.form_data_type_config.FormDataTypeConfig"
    """<p>The type of data source to use to create the form.</p>"""
    form_action_type: "aws_sdk_amplifyuibuilder.types.form_action_type.FormActionType"
    """<p>Specifies whether to perform a create or update action on the form.</p>"""
    fields: "aws_sdk_amplifyuibuilder.types.fields_map.FieldsMap"
    """<p>The configuration information for the form's fields.</p>"""
    style: "aws_sdk_amplifyuibuilder.types.form_style.FormStyle"
    """<p>The configuration for the form's style.</p>"""
    sectional_elements: (
        "aws_sdk_amplifyuibuilder.types.sectional_element_map.SectionalElementMap"
    )
    """<p>The configuration information for the visual helper elements for the form. These elements are not associated with any data.</p>"""
    schema_version: "str"
    """<p>The schema version of the form.</p>"""
    cta: NotRequired["aws_sdk_amplifyuibuilder.types.form_cta.FormCTA"]
    """<p>The <code>FormCTA</code> object that stores the call to action configuration for the form.</p>"""
    tags: NotRequired["aws_sdk_amplifyuibuilder.types.tags.Tags"]
    """<p>One or more key-value pairs to use when tagging the form data.</p>"""
    label_decorator: NotRequired[
        "aws_sdk_amplifyuibuilder.types.label_decorator.LabelDecorator"
    ]
    """<p>Specifies an icon or decoration to display on the form.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFormData) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_amplifyuibuilder.types.form_data_type_config

    out["dataType"] = (
        aws_sdk_amplifyuibuilder.types.form_data_type_config.serialize_json(
            value["data_type"]
        )
    )
    import aws_sdk_amplifyuibuilder.types.form_action_type

    out["formActionType"] = (
        aws_sdk_amplifyuibuilder.types.form_action_type.serialize_json(
            value["form_action_type"]
        )
    )
    import aws_sdk_amplifyuibuilder.types.fields_map

    out["fields"] = aws_sdk_amplifyuibuilder.types.fields_map.serialize_json(
        value["fields"]
    )
    import aws_sdk_amplifyuibuilder.types.form_style

    out["style"] = aws_sdk_amplifyuibuilder.types.form_style.serialize_json(
        value["style"]
    )
    import aws_sdk_amplifyuibuilder.types.sectional_element_map

    out["sectionalElements"] = (
        aws_sdk_amplifyuibuilder.types.sectional_element_map.serialize_json(
            value["sectional_elements"]
        )
    )
    out["schemaVersion"] = value["schema_version"]
    if "cta" in value:
        import aws_sdk_amplifyuibuilder.types.form_cta

        out["cta"] = aws_sdk_amplifyuibuilder.types.form_cta.serialize_json(
            value["cta"]
        )
    if "tags" in value:
        import aws_sdk_amplifyuibuilder.types.tags

        out["tags"] = aws_sdk_amplifyuibuilder.types.tags.serialize_json(value["tags"])
    if "label_decorator" in value:
        out["labelDecorator"] = value["label_decorator"]
    return out


def deserialize_json(data: dict) -> CreateFormData:
    out: CreateFormData = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateFormData.name required")
    if "dataType" in data:
        import aws_sdk_amplifyuibuilder.types.form_data_type_config

        out["data_type"] = (
            aws_sdk_amplifyuibuilder.types.form_data_type_config.deserialize_json(
                data["dataType"]
            )
        )
    else:
        raise DeserializationError("CreateFormData.data_type required")
    if "formActionType" in data:
        import aws_sdk_amplifyuibuilder.types.form_action_type

        out["form_action_type"] = (
            aws_sdk_amplifyuibuilder.types.form_action_type.deserialize_json(
                data["formActionType"]
            )
        )
    else:
        raise DeserializationError("CreateFormData.form_action_type required")
    if "fields" in data:
        import aws_sdk_amplifyuibuilder.types.fields_map

        out["fields"] = aws_sdk_amplifyuibuilder.types.fields_map.deserialize_json(
            data["fields"]
        )
    else:
        raise DeserializationError("CreateFormData.fields required")
    if "style" in data:
        import aws_sdk_amplifyuibuilder.types.form_style

        out["style"] = aws_sdk_amplifyuibuilder.types.form_style.deserialize_json(
            data["style"]
        )
    else:
        raise DeserializationError("CreateFormData.style required")
    if "sectionalElements" in data:
        import aws_sdk_amplifyuibuilder.types.sectional_element_map

        out["sectional_elements"] = (
            aws_sdk_amplifyuibuilder.types.sectional_element_map.deserialize_json(
                data["sectionalElements"]
            )
        )
    else:
        raise DeserializationError("CreateFormData.sectional_elements required")
    if "schemaVersion" in data:
        out["schema_version"] = data["schemaVersion"]
    else:
        raise DeserializationError("CreateFormData.schema_version required")
    if "cta" in data:
        import aws_sdk_amplifyuibuilder.types.form_cta

        out["cta"] = aws_sdk_amplifyuibuilder.types.form_cta.deserialize_json(
            data["cta"]
        )
    if "tags" in data:
        import aws_sdk_amplifyuibuilder.types.tags

        out["tags"] = aws_sdk_amplifyuibuilder.types.tags.deserialize_json(data["tags"])
    if "labelDecorator" in data:
        out["label_decorator"] = data["labelDecorator"]
    return out
