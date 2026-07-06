"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#FormSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_amplifyuibuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.form_action_type
    import aws_sdk_amplifyuibuilder.types.form_data_type_config
    import aws_sdk_amplifyuibuilder.types.form_name
    import aws_sdk_amplifyuibuilder.types.uuid


class FormSummary(TypedDict, closed=True):
    app_id: "str"
    """<p>The unique ID for the app associated with the form summary.</p>"""
    data_type: "aws_sdk_amplifyuibuilder.types.form_data_type_config.FormDataTypeConfig"
    """<p>The form's data source type.</p>"""
    environment_name: "str"
    """<p>The name of the backend environment that is part of the Amplify app.</p>"""
    form_action_type: "aws_sdk_amplifyuibuilder.types.form_action_type.FormActionType"
    """<p>The type of operation to perform on the form.</p>"""
    id: "aws_sdk_amplifyuibuilder.types.uuid.Uuid"
    """<p>The ID of the form.</p>"""
    name: "aws_sdk_amplifyuibuilder.types.form_name.FormName"
    """<p>The name of the form.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FormSummary) -> dict:
    out: dict = {}
    out["appId"] = value["app_id"]
    import aws_sdk_amplifyuibuilder.types.form_data_type_config

    out["dataType"] = (
        aws_sdk_amplifyuibuilder.types.form_data_type_config.serialize_json(
            value["data_type"]
        )
    )
    out["environmentName"] = value["environment_name"]
    import aws_sdk_amplifyuibuilder.types.form_action_type

    out["formActionType"] = (
        aws_sdk_amplifyuibuilder.types.form_action_type.serialize_json(
            value["form_action_type"]
        )
    )
    out["id"] = value["id"]
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> FormSummary:
    out: FormSummary = {}  # type: ignore[typeddict-item]
    if "appId" in data:
        out["app_id"] = data["appId"]
    else:
        raise DeserializationError("FormSummary.app_id required")
    if "dataType" in data:
        import aws_sdk_amplifyuibuilder.types.form_data_type_config

        out["data_type"] = (
            aws_sdk_amplifyuibuilder.types.form_data_type_config.deserialize_json(
                data["dataType"]
            )
        )
    else:
        raise DeserializationError("FormSummary.data_type required")
    if "environmentName" in data:
        out["environment_name"] = data["environmentName"]
    else:
        raise DeserializationError("FormSummary.environment_name required")
    if "formActionType" in data:
        import aws_sdk_amplifyuibuilder.types.form_action_type

        out["form_action_type"] = (
            aws_sdk_amplifyuibuilder.types.form_action_type.deserialize_json(
                data["formActionType"]
            )
        )
    else:
        raise DeserializationError("FormSummary.form_action_type required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("FormSummary.id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("FormSummary.name required")
    return out
