"""Generated from Smithy shape ``com.amazonaws.drs#PutLaunchActionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_drs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_drs.types.launch_action_category
    import aws_sdk_drs.types.launch_action_description
    import aws_sdk_drs.types.launch_action_id
    import aws_sdk_drs.types.launch_action_name
    import aws_sdk_drs.types.launch_action_order
    import aws_sdk_drs.types.launch_action_parameters
    import aws_sdk_drs.types.launch_action_resource_id
    import aws_sdk_drs.types.launch_action_version
    import aws_sdk_drs.types.ssm_document_name


class PutLaunchActionRequest(TypedDict, closed=True):
    resource_id: "aws_sdk_drs.types.launch_action_resource_id.LaunchActionResourceId"
    action_code: "aws_sdk_drs.types.ssm_document_name.SsmDocumentName"
    """<p>Launch action code.</p>"""
    order: "aws_sdk_drs.types.launch_action_order.LaunchActionOrder"
    action_id: "aws_sdk_drs.types.launch_action_id.LaunchActionId"
    optional: "bool"
    """<p>Whether the launch will not be marked as failed if this action fails.</p>"""
    active: "bool"
    """<p>Whether the launch action is active.</p>"""
    name: "aws_sdk_drs.types.launch_action_name.LaunchActionName"
    action_version: "aws_sdk_drs.types.launch_action_version.LaunchActionVersion"
    category: "aws_sdk_drs.types.launch_action_category.LaunchActionCategory"
    parameters: NotRequired[
        "aws_sdk_drs.types.launch_action_parameters.LaunchActionParameters"
    ]
    description: "aws_sdk_drs.types.launch_action_description.LaunchActionDescription"


# --- restJson1 ser/de ---
def serialize_json(value: PutLaunchActionRequest) -> dict:
    out: dict = {}
    out["resourceId"] = value["resource_id"]
    out["actionCode"] = value["action_code"]
    out["order"] = value["order"]
    out["actionId"] = value["action_id"]
    out["optional"] = value["optional"]
    out["active"] = value["active"]
    out["name"] = value["name"]
    out["actionVersion"] = value["action_version"]
    out["category"] = value["category"]
    if "parameters" in value:
        import aws_sdk_drs.types.launch_action_parameters

        out["parameters"] = aws_sdk_drs.types.launch_action_parameters.serialize_json(
            value["parameters"]
        )
    out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> PutLaunchActionRequest:
    out: PutLaunchActionRequest = {}  # type: ignore[typeddict-item]
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    else:
        raise DeserializationError("PutLaunchActionRequest.resource_id required")
    if "actionCode" in data:
        out["action_code"] = data["actionCode"]
    else:
        raise DeserializationError("PutLaunchActionRequest.action_code required")
    if "order" in data:
        out["order"] = data["order"]
    else:
        raise DeserializationError("PutLaunchActionRequest.order required")
    if "actionId" in data:
        out["action_id"] = data["actionId"]
    else:
        raise DeserializationError("PutLaunchActionRequest.action_id required")
    if "optional" in data:
        out["optional"] = data["optional"]
    else:
        raise DeserializationError("PutLaunchActionRequest.optional required")
    if "active" in data:
        out["active"] = data["active"]
    else:
        raise DeserializationError("PutLaunchActionRequest.active required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("PutLaunchActionRequest.name required")
    if "actionVersion" in data:
        out["action_version"] = data["actionVersion"]
    else:
        raise DeserializationError("PutLaunchActionRequest.action_version required")
    if "category" in data:
        out["category"] = data["category"]
    else:
        raise DeserializationError("PutLaunchActionRequest.category required")
    if "parameters" in data:
        import aws_sdk_drs.types.launch_action_parameters

        out["parameters"] = aws_sdk_drs.types.launch_action_parameters.deserialize_json(
            data["parameters"]
        )
    if "description" in data:
        out["description"] = data["description"]
    else:
        raise DeserializationError("PutLaunchActionRequest.description required")
    return out
