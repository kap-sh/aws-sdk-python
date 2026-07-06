"""Generated from Smithy shape ``com.amazonaws.resourcegroups#UngroupResourcesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_resource_groups.types.failed_resource_list
    import aws_sdk_resource_groups.types.pending_resource_list
    import aws_sdk_resource_groups.types.resource_arn_list


class UngroupResourcesOutput(TypedDict, closed=True):
    succeeded: NotRequired[
        "aws_sdk_resource_groups.types.resource_arn_list.ResourceArnList"
    ]
    """<p>A list of resources that were successfully removed from the group by this operation.</p>"""
    failed: NotRequired[
        "aws_sdk_resource_groups.types.failed_resource_list.FailedResourceList"
    ]
    """<p>A list of any resources that failed to be removed from the group by this operation.</p>"""
    pending: NotRequired[
        "aws_sdk_resource_groups.types.pending_resource_list.PendingResourceList"
    ]
    """<p>A list of any resources that are still in the process of being removed from the group by this operation. These pending removals continue asynchronously. You can check the status of pending removals by using the <code> <a>ListGroupResources</a> </code> operation. After the resource is successfully removed, it no longer appears in the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UngroupResourcesOutput) -> dict:
    out: dict = {}
    if "succeeded" in value:
        import aws_sdk_resource_groups.types.resource_arn_list

        out["Succeeded"] = (
            aws_sdk_resource_groups.types.resource_arn_list.serialize_json(
                value["succeeded"]
            )
        )
    if "failed" in value:
        import aws_sdk_resource_groups.types.failed_resource_list

        out["Failed"] = (
            aws_sdk_resource_groups.types.failed_resource_list.serialize_json(
                value["failed"]
            )
        )
    if "pending" in value:
        import aws_sdk_resource_groups.types.pending_resource_list

        out["Pending"] = (
            aws_sdk_resource_groups.types.pending_resource_list.serialize_json(
                value["pending"]
            )
        )
    return out


def deserialize_json(data: dict) -> UngroupResourcesOutput:
    out: UngroupResourcesOutput = {}  # type: ignore[typeddict-item]
    if "Succeeded" in data:
        import aws_sdk_resource_groups.types.resource_arn_list

        out["succeeded"] = (
            aws_sdk_resource_groups.types.resource_arn_list.deserialize_json(
                data["Succeeded"]
            )
        )
    if "Failed" in data:
        import aws_sdk_resource_groups.types.failed_resource_list

        out["failed"] = (
            aws_sdk_resource_groups.types.failed_resource_list.deserialize_json(
                data["Failed"]
            )
        )
    if "Pending" in data:
        import aws_sdk_resource_groups.types.pending_resource_list

        out["pending"] = (
            aws_sdk_resource_groups.types.pending_resource_list.deserialize_json(
                data["Pending"]
            )
        )
    return out
