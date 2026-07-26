"""Generated from Smithy shape ``com.amazonaws.resourcegroups#GroupResourcesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resource_groups.types.failed_resource_list
    import capo_resource_groups.types.pending_resource_list
    import capo_resource_groups.types.resource_arn_list


class GroupResourcesOutput(TypedDict, closed=True):
    succeeded: NotRequired[
        "capo_resource_groups.types.resource_arn_list.ResourceArnList"
    ]
    """<p>A list of Amazon resource names (ARNs) of the resources that this operation successfully added to the group.</p>"""
    failed: NotRequired[
        "capo_resource_groups.types.failed_resource_list.FailedResourceList"
    ]
    """<p>A list of Amazon resource names (ARNs) of any resources that this operation failed to add to the group.</p>"""
    pending: NotRequired[
        "capo_resource_groups.types.pending_resource_list.PendingResourceList"
    ]
    """<p>A list of Amazon resource names (ARNs) of any resources that this operation is still in the process adding to the group. These pending additions continue asynchronously. You can check the status of pending additions by using the <code> <a>ListGroupResources</a> </code> operation, and checking the <code>Resources</code> array in the response and the <code>Status</code> field of each object in that array. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GroupResourcesOutput) -> dict:
    out: dict = {}
    if "succeeded" in value:
        import capo_resource_groups.types.resource_arn_list

        out["Succeeded"] = capo_resource_groups.types.resource_arn_list.serialize_json(
            value["succeeded"]
        )
    if "failed" in value:
        import capo_resource_groups.types.failed_resource_list

        out["Failed"] = capo_resource_groups.types.failed_resource_list.serialize_json(
            value["failed"]
        )
    if "pending" in value:
        import capo_resource_groups.types.pending_resource_list

        out["Pending"] = (
            capo_resource_groups.types.pending_resource_list.serialize_json(
                value["pending"]
            )
        )
    return out


def deserialize_json(data: dict) -> GroupResourcesOutput:
    out: GroupResourcesOutput = {}  # type: ignore[typeddict-item]
    if "Succeeded" in data:
        import capo_resource_groups.types.resource_arn_list

        out["succeeded"] = (
            capo_resource_groups.types.resource_arn_list.deserialize_json(
                data["Succeeded"]
            )
        )
    if "Failed" in data:
        import capo_resource_groups.types.failed_resource_list

        out["failed"] = (
            capo_resource_groups.types.failed_resource_list.deserialize_json(
                data["Failed"]
            )
        )
    if "Pending" in data:
        import capo_resource_groups.types.pending_resource_list

        out["pending"] = (
            capo_resource_groups.types.pending_resource_list.deserialize_json(
                data["Pending"]
            )
        )
    return out
