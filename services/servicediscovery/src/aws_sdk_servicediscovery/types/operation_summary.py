"""Generated from Smithy shape ``com.amazonaws.servicediscovery#OperationSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_servicediscovery.types.operation_id
    import aws_sdk_servicediscovery.types.operation_status


class OperationSummary(TypedDict):
    id: NotRequired["aws_sdk_servicediscovery.types.operation_id.OperationId"]
    """<p>The ID for an operation.</p>"""
    status: NotRequired[
        "aws_sdk_servicediscovery.types.operation_status.OperationStatus"
    ]
    """<p>The status of the operation. Values include the following:</p> <ul> <li> <p> <b>SUBMITTED</b>: This is the initial state immediately after you submit a request.</p> </li> <li> <p> <b>PENDING</b>: Cloud Map is performing the operation.</p> </li> <li> <p> <b>SUCCESS</b>: The operation succeeded.</p> </li> <li> <p> <b>FAIL</b>: The operation failed. For the failure reason, see <code>ErrorMessage</code>.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OperationSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "status" in value:
        import aws_sdk_servicediscovery.types.operation_status

        out["Status"] = (
            aws_sdk_servicediscovery.types.operation_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OperationSummary:
    out: OperationSummary = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Status" in data:
        import aws_sdk_servicediscovery.types.operation_status

        out["status"] = (
            aws_sdk_servicediscovery.types.operation_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    return out
