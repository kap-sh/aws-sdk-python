"""Generated from Smithy shape ``com.amazonaws.qapps#CreateQAppOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_qapps.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qapps.types.app_arn
    import aws_sdk_qapps.types.app_required_capabilities
    import aws_sdk_qapps.types.app_status
    import aws_sdk_qapps.types.app_version
    import aws_sdk_qapps.types.description
    import aws_sdk_qapps.types.initial_prompt
    import aws_sdk_qapps.types.q_apps_timestamp
    import aws_sdk_qapps.types.title
    import aws_sdk_qapps.types.uuid


class CreateQAppOutput(TypedDict, closed=True):
    app_id: "aws_sdk_qapps.types.uuid.UUID"
    """<p>The unique identifier of the new Q App.</p>"""
    app_arn: "aws_sdk_qapps.types.app_arn.AppArn"
    """<p>The Amazon Resource Name (ARN) of the new Q App.</p>"""
    title: "aws_sdk_qapps.types.title.Title"
    """<p>The title of the new Q App.</p>"""
    description: NotRequired["aws_sdk_qapps.types.description.Description"]
    """<p>The description of the new Q App.</p>"""
    initial_prompt: NotRequired["aws_sdk_qapps.types.initial_prompt.InitialPrompt"]
    """<p>The initial prompt displayed when the Q App is started.</p>"""
    app_version: "aws_sdk_qapps.types.app_version.AppVersion"
    """<p>The version of the new Q App.</p>"""
    status: "aws_sdk_qapps.types.app_status.AppStatus"
    r"""<p>The status of the new Q App, such as \"Created\".</p>"""
    created_at: "aws_sdk_qapps.types.q_apps_timestamp.QAppsTimestamp"
    """<p>The date and time the Q App was created.</p>"""
    created_by: "str"
    """<p>The user who created the Q App.</p>"""
    updated_at: "aws_sdk_qapps.types.q_apps_timestamp.QAppsTimestamp"
    """<p>The date and time the Q App was last updated.</p>"""
    updated_by: "str"
    """<p>The user who last updated the Q App.</p>"""
    required_capabilities: NotRequired[
        "aws_sdk_qapps.types.app_required_capabilities.AppRequiredCapabilities"
    ]
    """<p>The capabilities required to run the Q App, such as file upload or third-party integrations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateQAppOutput) -> dict:
    out: dict = {}
    out["appId"] = value["app_id"]
    out["appArn"] = value["app_arn"]
    out["title"] = value["title"]
    if "description" in value:
        out["description"] = value["description"]
    if "initial_prompt" in value:
        out["initialPrompt"] = value["initial_prompt"]
    out["appVersion"] = value["app_version"]
    import aws_sdk_qapps.types.app_status

    out["status"] = aws_sdk_qapps.types.app_status.serialize_json(value["status"])
    import aws_sdk_qapps.types.q_apps_timestamp

    out["createdAt"] = aws_sdk_qapps.types.q_apps_timestamp.serialize_json(
        value["created_at"]
    )
    out["createdBy"] = value["created_by"]
    import aws_sdk_qapps.types.q_apps_timestamp

    out["updatedAt"] = aws_sdk_qapps.types.q_apps_timestamp.serialize_json(
        value["updated_at"]
    )
    out["updatedBy"] = value["updated_by"]
    if "required_capabilities" in value:
        import aws_sdk_qapps.types.app_required_capabilities

        out["requiredCapabilities"] = (
            aws_sdk_qapps.types.app_required_capabilities.serialize_json(
                value["required_capabilities"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateQAppOutput:
    out: CreateQAppOutput = {}  # type: ignore[typeddict-item]
    if "appId" in data:
        out["app_id"] = data["appId"]
    else:
        raise DeserializationError("CreateQAppOutput.app_id required")
    if "appArn" in data:
        out["app_arn"] = data["appArn"]
    else:
        raise DeserializationError("CreateQAppOutput.app_arn required")
    if "title" in data:
        out["title"] = data["title"]
    else:
        raise DeserializationError("CreateQAppOutput.title required")
    if "description" in data:
        out["description"] = data["description"]
    if "initialPrompt" in data:
        out["initial_prompt"] = data["initialPrompt"]
    if "appVersion" in data:
        out["app_version"] = data["appVersion"]
    else:
        raise DeserializationError("CreateQAppOutput.app_version required")
    if "status" in data:
        import aws_sdk_qapps.types.app_status

        out["status"] = aws_sdk_qapps.types.app_status.deserialize_json(data["status"])
    else:
        raise DeserializationError("CreateQAppOutput.status required")
    if "createdAt" in data:
        import aws_sdk_qapps.types.q_apps_timestamp

        out["created_at"] = aws_sdk_qapps.types.q_apps_timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("CreateQAppOutput.created_at required")
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    else:
        raise DeserializationError("CreateQAppOutput.created_by required")
    if "updatedAt" in data:
        import aws_sdk_qapps.types.q_apps_timestamp

        out["updated_at"] = aws_sdk_qapps.types.q_apps_timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("CreateQAppOutput.updated_at required")
    if "updatedBy" in data:
        out["updated_by"] = data["updatedBy"]
    else:
        raise DeserializationError("CreateQAppOutput.updated_by required")
    if "requiredCapabilities" in data:
        import aws_sdk_qapps.types.app_required_capabilities

        out["required_capabilities"] = (
            aws_sdk_qapps.types.app_required_capabilities.deserialize_json(
                data["requiredCapabilities"]
            )
        )
    return out
