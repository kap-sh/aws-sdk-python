"""Generated from Smithy shape ``com.amazonaws.servicequotas#GetAWSDefaultServiceQuotaRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_service_quotas.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_service_quotas.types.quota_code
    import aws_sdk_service_quotas.types.service_code


class GetAWSDefaultServiceQuotaRequest(TypedDict, closed=True):
    service_code: "aws_sdk_service_quotas.types.service_code.ServiceCode"
    """<p>Specifies the service identifier. To find the service code value for an Amazon Web Services service, use the <a>ListServices</a> operation.</p>"""
    quota_code: "aws_sdk_service_quotas.types.quota_code.QuotaCode"
    """<p>Specifies the quota identifier. To find the quota code for a specific quota, use the <a>ListServiceQuotas</a> operation, and look for the <code>QuotaCode</code> response in the output for the quota you want.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAWSDefaultServiceQuotaRequest) -> dict:
    out: dict = {}
    out["ServiceCode"] = value["service_code"]
    out["QuotaCode"] = value["quota_code"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAWSDefaultServiceQuotaRequest:
    out: GetAWSDefaultServiceQuotaRequest = {}  # type: ignore[typeddict-item]
    if "ServiceCode" in data:
        out["service_code"] = data["ServiceCode"]
    else:
        raise DeserializationError(
            "GetAWSDefaultServiceQuotaRequest.service_code required"
        )
    if "QuotaCode" in data:
        out["quota_code"] = data["QuotaCode"]
    else:
        raise DeserializationError(
            "GetAWSDefaultServiceQuotaRequest.quota_code required"
        )
    return out
