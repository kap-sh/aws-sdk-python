"""Generated from Smithy shape ``com.amazonaws.servicequotas#PutServiceQuotaIncreaseRequestIntoTemplateRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_service_quotas.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_service_quotas.types.aws_region
    import aws_sdk_service_quotas.types.quota_code
    import aws_sdk_service_quotas.types.quota_value
    import aws_sdk_service_quotas.types.service_code


class PutServiceQuotaIncreaseRequestIntoTemplateRequest(TypedDict):
    quota_code: "aws_sdk_service_quotas.types.quota_code.QuotaCode"
    """<p>Specifies the quota identifier. To find the quota code for a specific quota, use the <a>ListServiceQuotas</a> operation, and look for the <code>QuotaCode</code> response in the output for the quota you want.</p>"""
    service_code: "aws_sdk_service_quotas.types.service_code.ServiceCode"
    """<p>Specifies the service identifier. To find the service code value for an Amazon Web Services service, use the <a>ListServices</a> operation.</p>"""
    aws_region: "aws_sdk_service_quotas.types.aws_region.AwsRegion"
    """<p>Specifies the Amazon Web Services Region to which the template applies.</p>"""
    desired_value: "aws_sdk_service_quotas.types.quota_value.QuotaValue"
    """<p>Specifies the new, increased value for the quota.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: PutServiceQuotaIncreaseRequestIntoTemplateRequest,
) -> dict:
    out: dict = {}
    out["QuotaCode"] = value["quota_code"]
    out["ServiceCode"] = value["service_code"]
    out["AwsRegion"] = value["aws_region"]
    out["DesiredValue"] = value["desired_value"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> PutServiceQuotaIncreaseRequestIntoTemplateRequest:
    out: PutServiceQuotaIncreaseRequestIntoTemplateRequest = {}  # type: ignore[typeddict-item]
    if "QuotaCode" in data:
        out["quota_code"] = data["QuotaCode"]
    else:
        raise DeserializationError(
            "PutServiceQuotaIncreaseRequestIntoTemplateRequest.quota_code required"
        )
    if "ServiceCode" in data:
        out["service_code"] = data["ServiceCode"]
    else:
        raise DeserializationError(
            "PutServiceQuotaIncreaseRequestIntoTemplateRequest.service_code required"
        )
    if "AwsRegion" in data:
        out["aws_region"] = data["AwsRegion"]
    else:
        raise DeserializationError(
            "PutServiceQuotaIncreaseRequestIntoTemplateRequest.aws_region required"
        )
    if "DesiredValue" in data:
        out["desired_value"] = data["DesiredValue"]
    else:
        raise DeserializationError(
            "PutServiceQuotaIncreaseRequestIntoTemplateRequest.desired_value required"
        )
    return out
