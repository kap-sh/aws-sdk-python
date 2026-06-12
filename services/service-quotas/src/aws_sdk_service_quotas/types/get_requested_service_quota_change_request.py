"""Generated from Smithy shape ``com.amazonaws.servicequotas#GetRequestedServiceQuotaChangeRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_service_quotas.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_service_quotas.types.request_id


class GetRequestedServiceQuotaChangeRequest(TypedDict):
    request_id: "aws_sdk_service_quotas.types.request_id.RequestId"
    """<p>Specifies the ID of the quota increase request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRequestedServiceQuotaChangeRequest) -> dict:
    out: dict = {}
    out["RequestId"] = value["request_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRequestedServiceQuotaChangeRequest:
    out: GetRequestedServiceQuotaChangeRequest = {}  # type: ignore[typeddict-item]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    else:
        raise DeserializationError(
            "GetRequestedServiceQuotaChangeRequest.request_id required"
        )
    return out
