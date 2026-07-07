"""Generated from Smithy shape ``com.amazonaws.drs#PutLaunchActionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_drs.types.launch_action_category
    import aws_sdk_drs.types.launch_action_description
    import aws_sdk_drs.types.launch_action_id
    import aws_sdk_drs.types.launch_action_name
    import aws_sdk_drs.types.launch_action_order
    import aws_sdk_drs.types.launch_action_parameters
    import aws_sdk_drs.types.launch_action_resource_id
    import aws_sdk_drs.types.launch_action_type
    import aws_sdk_drs.types.launch_action_version
    import aws_sdk_drs.types.ssm_document_name


class PutLaunchActionResponse(TypedDict, closed=True):
    resource_id: NotRequired[
        "aws_sdk_drs.types.launch_action_resource_id.LaunchActionResourceId"
    ]
    action_id: NotRequired["aws_sdk_drs.types.launch_action_id.LaunchActionId"]
    action_code: NotRequired["aws_sdk_drs.types.ssm_document_name.SsmDocumentName"]
    """<p>Launch action code.</p>"""
    type: NotRequired["aws_sdk_drs.types.launch_action_type.LaunchActionType"]
    """<p>Launch action type.</p>"""
    name: NotRequired["aws_sdk_drs.types.launch_action_name.LaunchActionName"]
    active: NotRequired["bool"]
    """<p>Whether the launch action is active.</p>"""
    order: NotRequired["aws_sdk_drs.types.launch_action_order.LaunchActionOrder"]
    action_version: NotRequired[
        "aws_sdk_drs.types.launch_action_version.LaunchActionVersion"
    ]
    optional: NotRequired["bool"]
    """<p>Whether the launch will not be marked as failed if this action fails.</p>"""
    parameters: NotRequired[
        "aws_sdk_drs.types.launch_action_parameters.LaunchActionParameters"
    ]
    description: NotRequired[
        "aws_sdk_drs.types.launch_action_description.LaunchActionDescription"
    ]
    category: NotRequired[
        "aws_sdk_drs.types.launch_action_category.LaunchActionCategory"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: PutLaunchActionResponse) -> dict:
    out: dict = {}
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "action_id" in value:
        out["actionId"] = value["action_id"]
    if "action_code" in value:
        out["actionCode"] = value["action_code"]
    if "type" in value:
        out["type"] = value["type"]
    if "name" in value:
        out["name"] = value["name"]
    if "active" in value:
        out["active"] = value["active"]
    if "order" in value:
        out["order"] = value["order"]
    if "action_version" in value:
        out["actionVersion"] = value["action_version"]
    if "optional" in value:
        out["optional"] = value["optional"]
    if "parameters" in value:
        import aws_sdk_drs.types.launch_action_parameters

        out["parameters"] = aws_sdk_drs.types.launch_action_parameters.serialize_json(
            value["parameters"]
        )
    if "description" in value:
        out["description"] = value["description"]
    if "category" in value:
        out["category"] = value["category"]
    return out


def deserialize_json(data: dict) -> PutLaunchActionResponse:
    out: PutLaunchActionResponse = {}  # type: ignore[typeddict-item]
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    if "actionId" in data:
        out["action_id"] = data["actionId"]
    if "actionCode" in data:
        out["action_code"] = data["actionCode"]
    if "type" in data:
        out["type"] = data["type"]
    if "name" in data:
        out["name"] = data["name"]
    if "active" in data:
        out["active"] = data["active"]
    if "order" in data:
        out["order"] = data["order"]
    if "actionVersion" in data:
        out["action_version"] = data["actionVersion"]
    if "optional" in data:
        out["optional"] = data["optional"]
    if "parameters" in data:
        import aws_sdk_drs.types.launch_action_parameters

        out["parameters"] = aws_sdk_drs.types.launch_action_parameters.deserialize_json(
            data["parameters"]
        )
    if "description" in data:
        out["description"] = data["description"]
    if "category" in data:
        out["category"] = data["category"]
    return out
