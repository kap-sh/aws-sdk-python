"""Generated from Smithy shape ``com.amazonaws.servicediscovery#UpdateServiceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_servicediscovery.types.operation_id


class UpdateServiceResponse(TypedDict):
    operation_id: NotRequired["aws_sdk_servicediscovery.types.operation_id.OperationId"]
    """<p>A value that you can use to determine whether the request completed successfully. To get the status of the operation, see <a href=\"https://docs.aws.amazon.com/cloud-map/latest/api/API_GetOperation.html\">GetOperation</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateServiceResponse) -> dict:
    out: dict = {}
    if "operation_id" in value:
        out["OperationId"] = value["operation_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateServiceResponse:
    out: UpdateServiceResponse = {}  # type: ignore[typeddict-item]
    if "OperationId" in data:
        out["operation_id"] = data["OperationId"]
    return out
