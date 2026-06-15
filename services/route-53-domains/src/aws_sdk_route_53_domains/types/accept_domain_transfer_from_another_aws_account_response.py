"""Generated from Smithy shape ``com.amazonaws.route53domains#AcceptDomainTransferFromAnotherAwsAccountResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route_53_domains.types.operation_id


class AcceptDomainTransferFromAnotherAwsAccountResponse(TypedDict):
    operation_id: NotRequired["aws_sdk_route_53_domains.types.operation_id.OperationId"]
    r"""<p>Identifier for tracking the progress of the request. To query the operation status, use <a href=\"https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_GetOperationDetail.html\">GetOperationDetail</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: AcceptDomainTransferFromAnotherAwsAccountResponse,
) -> dict:
    out: dict = {}
    if "operation_id" in value:
        out["OperationId"] = value["operation_id"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> AcceptDomainTransferFromAnotherAwsAccountResponse:
    out: AcceptDomainTransferFromAnotherAwsAccountResponse = {}  # type: ignore[typeddict-item]
    if "OperationId" in data:
        out["operation_id"] = data["OperationId"]
    return out
