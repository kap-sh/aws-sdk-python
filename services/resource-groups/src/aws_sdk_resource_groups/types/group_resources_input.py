"""Generated from Smithy shape ``com.amazonaws.resourcegroups#GroupResourcesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_resource_groups.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resource_groups.types.group_string_v2
    import aws_sdk_resource_groups.types.resource_arn_list


class GroupResourcesInput(TypedDict, closed=True):
    group: "aws_sdk_resource_groups.types.group_string_v2.GroupStringV2"
    """<p>The name or the Amazon resource name (ARN) of the resource group to add resources to.</p>"""
    resource_arns: "aws_sdk_resource_groups.types.resource_arn_list.ResourceArnList"
    """<p>The list of Amazon resource names (ARNs) of the resources to be added to the group. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GroupResourcesInput) -> dict:
    out: dict = {}
    out["Group"] = value["group"]
    import aws_sdk_resource_groups.types.resource_arn_list

    out["ResourceArns"] = (
        aws_sdk_resource_groups.types.resource_arn_list.serialize_json(
            value["resource_arns"]
        )
    )
    return out


def deserialize_json(data: dict) -> GroupResourcesInput:
    out: GroupResourcesInput = {}  # type: ignore[typeddict-item]
    if "Group" in data:
        out["group"] = data["Group"]
    else:
        raise DeserializationError("GroupResourcesInput.group required")
    if "ResourceArns" in data:
        import aws_sdk_resource_groups.types.resource_arn_list

        out["resource_arns"] = (
            aws_sdk_resource_groups.types.resource_arn_list.deserialize_json(
                data["ResourceArns"]
            )
        )
    else:
        raise DeserializationError("GroupResourcesInput.resource_arns required")
    return out
