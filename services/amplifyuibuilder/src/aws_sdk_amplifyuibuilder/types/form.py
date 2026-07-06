"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#Form``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

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
    import aws_sdk_amplifyuibuilder.types.uuid


class Form(TypedDict, closed=True):
    app_id: "str"
    """<p>The unique ID of the Amplify app associated with the form.</p>"""
    environment_name: "str"
    """<p>The name of the backend environment that is a part of the Amplify app.</p>"""
    id: "aws_sdk_amplifyuibuilder.types.uuid.Uuid"
    """<p>The unique ID of the form.</p>"""
    name: "aws_sdk_amplifyuibuilder.types.form_name.FormName"
    """<p>The name of the form.</p>"""
    form_action_type: "aws_sdk_amplifyuibuilder.types.form_action_type.FormActionType"
    """<p>The operation to perform on the specified form.</p>"""
    style: "aws_sdk_amplifyuibuilder.types.form_style.FormStyle"
    """<p>Stores the configuration for the form's style.</p>"""
    data_type: "aws_sdk_amplifyuibuilder.types.form_data_type_config.FormDataTypeConfig"
    """<p>The type of data source to use to create the form.</p>"""
    fields: "aws_sdk_amplifyuibuilder.types.fields_map.FieldsMap"
    """<p>Stores the information about the form's fields.</p>"""
    sectional_elements: (
        "aws_sdk_amplifyuibuilder.types.sectional_element_map.SectionalElementMap"
    )
    """<p>Stores the visual helper elements for the form that are not associated with any data.</p>"""
    schema_version: "str"
    """<p>The schema version of the form when it was imported.</p>"""
    tags: NotRequired["aws_sdk_amplifyuibuilder.types.tags.Tags"]
    """<p>One or more key-value pairs to use when tagging the form.</p>"""
    cta: NotRequired["aws_sdk_amplifyuibuilder.types.form_cta.FormCTA"]
    """<p>Stores the call to action configuration for the form.</p>"""
    label_decorator: NotRequired[
        "aws_sdk_amplifyuibuilder.types.label_decorator.LabelDecorator"
    ]
    """<p>Specifies an icon or decoration to display on the form.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Form) -> dict:
    out: dict = {}
    out["appId"] = value["app_id"]
    out["environmentName"] = value["environment_name"]
    out["id"] = value["id"]
    out["name"] = value["name"]
    import aws_sdk_amplifyuibuilder.types.form_action_type

    out["formActionType"] = (
        aws_sdk_amplifyuibuilder.types.form_action_type.serialize_json(
            value["form_action_type"]
        )
    )
    import aws_sdk_amplifyuibuilder.types.form_style

    out["style"] = aws_sdk_amplifyuibuilder.types.form_style.serialize_json(
        value["style"]
    )
    import aws_sdk_amplifyuibuilder.types.form_data_type_config

    out["dataType"] = (
        aws_sdk_amplifyuibuilder.types.form_data_type_config.serialize_json(
            value["data_type"]
        )
    )
    import aws_sdk_amplifyuibuilder.types.fields_map

    out["fields"] = aws_sdk_amplifyuibuilder.types.fields_map.serialize_json(
        value["fields"]
    )
    import aws_sdk_amplifyuibuilder.types.sectional_element_map

    out["sectionalElements"] = (
        aws_sdk_amplifyuibuilder.types.sectional_element_map.serialize_json(
            value["sectional_elements"]
        )
    )
    out["schemaVersion"] = value["schema_version"]
    if "tags" in value:
        import aws_sdk_amplifyuibuilder.types.tags

        out["tags"] = aws_sdk_amplifyuibuilder.types.tags.serialize_json(value["tags"])
    if "cta" in value:
        import aws_sdk_amplifyuibuilder.types.form_cta

        out["cta"] = aws_sdk_amplifyuibuilder.types.form_cta.serialize_json(
            value["cta"]
        )
    if "label_decorator" in value:
        out["labelDecorator"] = value["label_decorator"]
    return out


def deserialize_json(data: dict) -> Form:
    out: Form = {}  # type: ignore[typeddict-item]
    if "appId" in data:
        out["app_id"] = data["appId"]
    else:
        raise DeserializationError("Form.app_id required")
    if "environmentName" in data:
        out["environment_name"] = data["environmentName"]
    else:
        raise DeserializationError("Form.environment_name required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("Form.id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("Form.name required")
    if "formActionType" in data:
        import aws_sdk_amplifyuibuilder.types.form_action_type

        out["form_action_type"] = (
            aws_sdk_amplifyuibuilder.types.form_action_type.deserialize_json(
                data["formActionType"]
            )
        )
    else:
        raise DeserializationError("Form.form_action_type required")
    if "style" in data:
        import aws_sdk_amplifyuibuilder.types.form_style

        out["style"] = aws_sdk_amplifyuibuilder.types.form_style.deserialize_json(
            data["style"]
        )
    else:
        raise DeserializationError("Form.style required")
    if "dataType" in data:
        import aws_sdk_amplifyuibuilder.types.form_data_type_config

        out["data_type"] = (
            aws_sdk_amplifyuibuilder.types.form_data_type_config.deserialize_json(
                data["dataType"]
            )
        )
    else:
        raise DeserializationError("Form.data_type required")
    if "fields" in data:
        import aws_sdk_amplifyuibuilder.types.fields_map

        out["fields"] = aws_sdk_amplifyuibuilder.types.fields_map.deserialize_json(
            data["fields"]
        )
    else:
        raise DeserializationError("Form.fields required")
    if "sectionalElements" in data:
        import aws_sdk_amplifyuibuilder.types.sectional_element_map

        out["sectional_elements"] = (
            aws_sdk_amplifyuibuilder.types.sectional_element_map.deserialize_json(
                data["sectionalElements"]
            )
        )
    else:
        raise DeserializationError("Form.sectional_elements required")
    if "schemaVersion" in data:
        out["schema_version"] = data["schemaVersion"]
    else:
        raise DeserializationError("Form.schema_version required")
    if "tags" in data:
        import aws_sdk_amplifyuibuilder.types.tags

        out["tags"] = aws_sdk_amplifyuibuilder.types.tags.deserialize_json(data["tags"])
    if "cta" in data:
        import aws_sdk_amplifyuibuilder.types.form_cta

        out["cta"] = aws_sdk_amplifyuibuilder.types.form_cta.deserialize_json(
            data["cta"]
        )
    if "labelDecorator" in data:
        out["label_decorator"] = data["labelDecorator"]
    return out
