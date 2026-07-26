"""Generated from Smithy shape ``com.amazonaws.qapps#GetQAppOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_qapps.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qapps.types.app_arn
    import capo_qapps.types.app_definition
    import capo_qapps.types.app_required_capabilities
    import capo_qapps.types.app_status
    import capo_qapps.types.app_version
    import capo_qapps.types.description
    import capo_qapps.types.initial_prompt
    import capo_qapps.types.q_apps_timestamp
    import capo_qapps.types.title
    import capo_qapps.types.uuid


class GetQAppOutput(TypedDict, closed=True):
    app_id: "capo_qapps.types.uuid.UUID"
    """<p>The unique identifier of the Q App.</p>"""
    app_arn: "capo_qapps.types.app_arn.AppArn"
    """<p>The Amazon Resource Name (ARN) of the Q App.</p>"""
    title: "capo_qapps.types.title.Title"
    """<p>The title of the Q App.</p>"""
    description: NotRequired["capo_qapps.types.description.Description"]
    """<p>The description of the Q App.</p>"""
    initial_prompt: NotRequired["capo_qapps.types.initial_prompt.InitialPrompt"]
    """<p>The initial prompt displayed when the Q App is started.</p>"""
    app_version: "capo_qapps.types.app_version.AppVersion"
    """<p>The version of the Q App.</p>"""
    status: "capo_qapps.types.app_status.AppStatus"
    """<p>The status of the Q App.</p>"""
    created_at: "capo_qapps.types.q_apps_timestamp.QAppsTimestamp"
    """<p>The date and time the Q App was created.</p>"""
    created_by: "str"
    """<p>The user who created the Q App.</p>"""
    updated_at: "capo_qapps.types.q_apps_timestamp.QAppsTimestamp"
    """<p>The date and time the Q App was last updated.</p>"""
    updated_by: "str"
    """<p>The user who last updated the Q App.</p>"""
    required_capabilities: NotRequired[
        "capo_qapps.types.app_required_capabilities.AppRequiredCapabilities"
    ]
    """<p>The capabilities required to run the Q App, such as file upload or third-party integrations.</p>"""
    app_definition: "capo_qapps.types.app_definition.AppDefinition"
    """<p>The full definition of the Q App, specifying the cards and flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetQAppOutput) -> dict:
    out: dict = {}
    out["appId"] = value["app_id"]
    out["appArn"] = value["app_arn"]
    out["title"] = value["title"]
    if "description" in value:
        out["description"] = value["description"]
    if "initial_prompt" in value:
        out["initialPrompt"] = value["initial_prompt"]
    out["appVersion"] = value["app_version"]
    import capo_qapps.types.app_status

    out["status"] = capo_qapps.types.app_status.serialize_json(value["status"])
    import capo_qapps.types.q_apps_timestamp

    out["createdAt"] = capo_qapps.types.q_apps_timestamp.serialize_json(
        value["created_at"]
    )
    out["createdBy"] = value["created_by"]
    import capo_qapps.types.q_apps_timestamp

    out["updatedAt"] = capo_qapps.types.q_apps_timestamp.serialize_json(
        value["updated_at"]
    )
    out["updatedBy"] = value["updated_by"]
    if "required_capabilities" in value:
        import capo_qapps.types.app_required_capabilities

        out["requiredCapabilities"] = (
            capo_qapps.types.app_required_capabilities.serialize_json(
                value["required_capabilities"]
            )
        )
    import capo_qapps.types.app_definition

    out["appDefinition"] = capo_qapps.types.app_definition.serialize_json(
        value["app_definition"]
    )
    return out


def deserialize_json(data: dict) -> GetQAppOutput:
    out: GetQAppOutput = {}  # type: ignore[typeddict-item]
    if "appId" in data:
        out["app_id"] = data["appId"]
    else:
        raise DeserializationError("GetQAppOutput.app_id required")
    if "appArn" in data:
        out["app_arn"] = data["appArn"]
    else:
        raise DeserializationError("GetQAppOutput.app_arn required")
    if "title" in data:
        out["title"] = data["title"]
    else:
        raise DeserializationError("GetQAppOutput.title required")
    if "description" in data:
        out["description"] = data["description"]
    if "initialPrompt" in data:
        out["initial_prompt"] = data["initialPrompt"]
    if "appVersion" in data:
        out["app_version"] = data["appVersion"]
    else:
        raise DeserializationError("GetQAppOutput.app_version required")
    if "status" in data:
        import capo_qapps.types.app_status

        out["status"] = capo_qapps.types.app_status.deserialize_json(data["status"])
    else:
        raise DeserializationError("GetQAppOutput.status required")
    if "createdAt" in data:
        import capo_qapps.types.q_apps_timestamp

        out["created_at"] = capo_qapps.types.q_apps_timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("GetQAppOutput.created_at required")
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    else:
        raise DeserializationError("GetQAppOutput.created_by required")
    if "updatedAt" in data:
        import capo_qapps.types.q_apps_timestamp

        out["updated_at"] = capo_qapps.types.q_apps_timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("GetQAppOutput.updated_at required")
    if "updatedBy" in data:
        out["updated_by"] = data["updatedBy"]
    else:
        raise DeserializationError("GetQAppOutput.updated_by required")
    if "requiredCapabilities" in data:
        import capo_qapps.types.app_required_capabilities

        out["required_capabilities"] = (
            capo_qapps.types.app_required_capabilities.deserialize_json(
                data["requiredCapabilities"]
            )
        )
    if "appDefinition" in data:
        import capo_qapps.types.app_definition

        out["app_definition"] = capo_qapps.types.app_definition.deserialize_json(
            data["appDefinition"]
        )
    else:
        raise DeserializationError("GetQAppOutput.app_definition required")
    return out
