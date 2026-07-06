"""Generated from Smithy shape ``com.amazonaws.servicequotas#DeleteServiceQuotaIncreaseRequestFromTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_service_quotas.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_service_quotas.types.aws_region
    import aws_sdk_service_quotas.types.quota_code
    import aws_sdk_service_quotas.types.service_code


class DeleteServiceQuotaIncreaseRequestFromTemplateRequest(TypedDict, closed=True):
    service_code: "aws_sdk_service_quotas.types.service_code.ServiceCode"
    """<p>Specifies the service identifier. To find the service code value for an Amazon Web Services service, use the <a>ListServices</a> operation.</p>"""
    quota_code: "aws_sdk_service_quotas.types.quota_code.QuotaCode"
    """<p>Specifies the quota identifier. To find the quota code for a specific quota, use the <a>ListServiceQuotas</a> operation, and look for the <code>QuotaCode</code> response in the output for the quota you want.</p>"""
    aws_region: "aws_sdk_service_quotas.types.aws_region.AwsRegion"
    """<p>Specifies the Amazon Web Services Region for which the request was made.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DeleteServiceQuotaIncreaseRequestFromTemplateRequest,
) -> dict:
    out: dict = {}
    out["ServiceCode"] = value["service_code"]
    out["QuotaCode"] = value["quota_code"]
    out["AwsRegion"] = value["aws_region"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DeleteServiceQuotaIncreaseRequestFromTemplateRequest:
    out: DeleteServiceQuotaIncreaseRequestFromTemplateRequest = {}  # type: ignore[typeddict-item]
    if "ServiceCode" in data:
        out["service_code"] = data["ServiceCode"]
    else:
        raise DeserializationError(
            "DeleteServiceQuotaIncreaseRequestFromTemplateRequest.service_code required"
        )
    if "QuotaCode" in data:
        out["quota_code"] = data["QuotaCode"]
    else:
        raise DeserializationError(
            "DeleteServiceQuotaIncreaseRequestFromTemplateRequest.quota_code required"
        )
    if "AwsRegion" in data:
        out["aws_region"] = data["AwsRegion"]
    else:
        raise DeserializationError(
            "DeleteServiceQuotaIncreaseRequestFromTemplateRequest.aws_region required"
        )
    return out
