"""Generated from Smithy shape ``com.amazonaws.drs#DeleteLaunchActionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_drs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_drs.types.launch_action_id
    import aws_sdk_drs.types.launch_action_resource_id


class DeleteLaunchActionRequest(TypedDict):
    resource_id: "aws_sdk_drs.types.launch_action_resource_id.LaunchActionResourceId"
    action_id: "aws_sdk_drs.types.launch_action_id.LaunchActionId"


# --- restJson1 ser/de ---
def serialize_json(value: DeleteLaunchActionRequest) -> dict:
    out: dict = {}
    out["resourceId"] = value["resource_id"]
    out["actionId"] = value["action_id"]
    return out


def deserialize_json(data: dict) -> DeleteLaunchActionRequest:
    out: DeleteLaunchActionRequest = {}  # type: ignore[typeddict-item]
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    else:
        raise DeserializationError("DeleteLaunchActionRequest.resource_id required")
    if "actionId" in data:
        out["action_id"] = data["actionId"]
    else:
        raise DeserializationError("DeleteLaunchActionRequest.action_id required")
    return out
