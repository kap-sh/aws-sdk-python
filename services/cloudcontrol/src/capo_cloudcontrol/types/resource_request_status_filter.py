"""Generated from Smithy shape ``com.amazonaws.cloudcontrol#ResourceRequestStatusFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudcontrol.types.operation_statuses
    import capo_cloudcontrol.types.operations


class ResourceRequestStatusFilter(TypedDict, closed=True):
    operations: NotRequired["capo_cloudcontrol.types.operations.Operations"]
    """<p>The operation types to include in the filter.</p>"""
    operation_statuses: NotRequired[
        "capo_cloudcontrol.types.operation_statuses.OperationStatuses"
    ]
    """<p>The operation statuses to include in the filter.</p> <ul> <li> <p> <code>PENDING</code>: The operation has been requested, but not yet initiated.</p> </li> <li> <p> <code>IN_PROGRESS</code>: The operation is in progress.</p> </li> <li> <p> <code>SUCCESS</code>: The operation completed.</p> </li> <li> <p> <code>FAILED</code>: The operation failed.</p> </li> <li> <p> <code>CANCEL_IN_PROGRESS</code>: The operation is in the process of being canceled.</p> </li> <li> <p> <code>CANCEL_COMPLETE</code>: The operation has been canceled.</p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceRequestStatusFilter) -> dict:
    out: dict = {}
    if "operations" in value:
        import capo_cloudcontrol.types.operations

        out["Operations"] = capo_cloudcontrol.types.operations.serialize_aws_json_1_0(
            value["operations"]
        )
    if "operation_statuses" in value:
        import capo_cloudcontrol.types.operation_statuses

        out["OperationStatuses"] = (
            capo_cloudcontrol.types.operation_statuses.serialize_aws_json_1_0(
                value["operation_statuses"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ResourceRequestStatusFilter:
    out: ResourceRequestStatusFilter = {}  # type: ignore[typeddict-item]
    if "Operations" in data:
        import capo_cloudcontrol.types.operations

        out["operations"] = capo_cloudcontrol.types.operations.deserialize_aws_json_1_0(
            data["Operations"]
        )
    if "OperationStatuses" in data:
        import capo_cloudcontrol.types.operation_statuses

        out["operation_statuses"] = (
            capo_cloudcontrol.types.operation_statuses.deserialize_aws_json_1_0(
                data["OperationStatuses"]
            )
        )
    return out
