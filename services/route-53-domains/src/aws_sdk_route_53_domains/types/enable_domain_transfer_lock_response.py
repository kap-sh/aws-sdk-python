"""Generated from Smithy shape ``com.amazonaws.route53domains#EnableDomainTransferLockResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route_53_domains.types.operation_id


class EnableDomainTransferLockResponse(TypedDict):
    operation_id: NotRequired["aws_sdk_route_53_domains.types.operation_id.OperationId"]
    """<p>Identifier for tracking the progress of the request. To use this ID to query the operation status, use GetOperationDetail.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnableDomainTransferLockResponse) -> dict:
    out: dict = {}
    if "operation_id" in value:
        out["OperationId"] = value["operation_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EnableDomainTransferLockResponse:
    out: EnableDomainTransferLockResponse = {}  # type: ignore[typeddict-item]
    if "OperationId" in data:
        out["operation_id"] = data["OperationId"]
    return out
