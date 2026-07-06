"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteQueuedReservedInstancesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.delete_queued_reserved_instances_id_list


class DeleteQueuedReservedInstancesRequest(TypedDict, closed=True):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    reserved_instances_ids: NotRequired[
        "aws_sdk_ec2.types.delete_queued_reserved_instances_id_list.DeleteQueuedReservedInstancesIdList"
    ]
    """<p>The IDs of the Reserved Instances.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteQueuedReservedInstancesRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "reserved_instances_ids" in value:
        import aws_sdk_ec2.types.delete_queued_reserved_instances_id_list

        aws_sdk_ec2.types.delete_queued_reserved_instances_id_list.serialize_ec2_query(
            value["reserved_instances_ids"], pairs, f"{prefix}.ReservedInstancesIds"
        )


def deserialize_ec2_query(el: Element) -> DeleteQueuedReservedInstancesRequest:
    out: DeleteQueuedReservedInstancesRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    if el.find("ReservedInstancesIds") is not None:
        import aws_sdk_ec2.types.delete_queued_reserved_instances_id_list

        out["reserved_instances_ids"] = (
            aws_sdk_ec2.types.delete_queued_reserved_instances_id_list.deserialize_ec2_query(
                el, "ReservedInstancesIds"
            )
        )
    return out
