"""Generated from Smithy shape ``com.amazonaws.resourcegroups#UngroupResourcesInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_resource_groups.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resource_groups.types.group_string_v2
    import aws_sdk_resource_groups.types.resource_arn_list


class UngroupResourcesInput(TypedDict):
    group: "aws_sdk_resource_groups.types.group_string_v2.GroupStringV2"
    """<p>The name or the Amazon resource name (ARN) of the resource group from which to remove the resources.</p>"""
    resource_arns: "aws_sdk_resource_groups.types.resource_arn_list.ResourceArnList"
    """<p>The Amazon resource names (ARNs) of the resources to be removed from the group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UngroupResourcesInput) -> dict:
    out: dict = {}
    out["Group"] = value["group"]
    import aws_sdk_resource_groups.types.resource_arn_list

    out["ResourceArns"] = (
        aws_sdk_resource_groups.types.resource_arn_list.serialize_json(
            value["resource_arns"]
        )
    )
    return out


def deserialize_json(data: dict) -> UngroupResourcesInput:
    out: UngroupResourcesInput = {}  # type: ignore[typeddict-item]
    if "Group" in data:
        out["group"] = data["Group"]
    else:
        raise DeserializationError("UngroupResourcesInput.group required")
    if "ResourceArns" in data:
        import aws_sdk_resource_groups.types.resource_arn_list

        out["resource_arns"] = (
            aws_sdk_resource_groups.types.resource_arn_list.deserialize_json(
                data["ResourceArns"]
            )
        )
    else:
        raise DeserializationError("UngroupResourcesInput.resource_arns required")
    return out
