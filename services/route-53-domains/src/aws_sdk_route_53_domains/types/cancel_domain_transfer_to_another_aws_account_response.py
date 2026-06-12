"""Generated from Smithy shape ``com.amazonaws.route53domains#CancelDomainTransferToAnotherAwsAccountResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route_53_domains.types.operation_id


class CancelDomainTransferToAnotherAwsAccountResponse(TypedDict):
    operation_id: NotRequired["aws_sdk_route_53_domains.types.operation_id.OperationId"]
    """<p>The identifier that <code>TransferDomainToAnotherAwsAccount</code> returned to track the progress of the request. Because the transfer request was canceled, the value is no longer valid, and you can't use <code>GetOperationDetail</code> to query the operation status.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: CancelDomainTransferToAnotherAwsAccountResponse,
) -> dict:
    out: dict = {}
    if "operation_id" in value:
        out["OperationId"] = value["operation_id"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> CancelDomainTransferToAnotherAwsAccountResponse:
    out: CancelDomainTransferToAnotherAwsAccountResponse = {}  # type: ignore[typeddict-item]
    if "OperationId" in data:
        out["operation_id"] = data["OperationId"]
    return out
