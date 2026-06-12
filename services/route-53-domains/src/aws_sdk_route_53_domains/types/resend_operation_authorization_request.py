"""Generated from Smithy shape ``com.amazonaws.route53domains#ResendOperationAuthorizationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_route_53_domains.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route_53_domains.types.operation_id


class ResendOperationAuthorizationRequest(TypedDict):
    operation_id: "aws_sdk_route_53_domains.types.operation_id.OperationId"
    """<p> Operation ID. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResendOperationAuthorizationRequest) -> dict:
    out: dict = {}
    out["OperationId"] = value["operation_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResendOperationAuthorizationRequest:
    out: ResendOperationAuthorizationRequest = {}  # type: ignore[typeddict-item]
    if "OperationId" in data:
        out["operation_id"] = data["OperationId"]
    else:
        raise DeserializationError(
            "ResendOperationAuthorizationRequest.operation_id required"
        )
    return out
