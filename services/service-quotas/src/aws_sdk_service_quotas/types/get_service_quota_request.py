"""Generated from Smithy shape ``com.amazonaws.servicequotas#GetServiceQuotaRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_service_quotas.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_service_quotas.types.quota_code
    import aws_sdk_service_quotas.types.quota_context_id
    import aws_sdk_service_quotas.types.service_code


class GetServiceQuotaRequest(TypedDict, closed=True):
    service_code: "aws_sdk_service_quotas.types.service_code.ServiceCode"
    """<p>Specifies the service identifier. To find the service code value for an Amazon Web Services service, use the <a>ListServices</a> operation.</p>"""
    quota_code: "aws_sdk_service_quotas.types.quota_code.QuotaCode"
    """<p>Specifies the quota identifier. To find the quota code for a specific quota, use the <a>ListServiceQuotas</a> operation, and look for the <code>QuotaCode</code> response in the output for the quota you want.</p>"""
    context_id: NotRequired[
        "aws_sdk_service_quotas.types.quota_context_id.QuotaContextId"
    ]
    """<p>Specifies the resource with an Amazon Resource Name (ARN).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetServiceQuotaRequest) -> dict:
    out: dict = {}
    out["ServiceCode"] = value["service_code"]
    out["QuotaCode"] = value["quota_code"]
    if "context_id" in value:
        out["ContextId"] = value["context_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetServiceQuotaRequest:
    out: GetServiceQuotaRequest = {}  # type: ignore[typeddict-item]
    if "ServiceCode" in data:
        out["service_code"] = data["ServiceCode"]
    else:
        raise DeserializationError("GetServiceQuotaRequest.service_code required")
    if "QuotaCode" in data:
        out["quota_code"] = data["QuotaCode"]
    else:
        raise DeserializationError("GetServiceQuotaRequest.quota_code required")
    if "ContextId" in data:
        out["context_id"] = data["ContextId"]
    return out
