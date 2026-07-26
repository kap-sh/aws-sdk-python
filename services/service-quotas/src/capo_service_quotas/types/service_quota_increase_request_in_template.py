"""Generated from Smithy shape ``com.amazonaws.servicequotas#ServiceQuotaIncreaseRequestInTemplate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_quotas.types.aws_region
    import capo_service_quotas.types.global_quota
    import capo_service_quotas.types.quota_code
    import capo_service_quotas.types.quota_name
    import capo_service_quotas.types.quota_unit
    import capo_service_quotas.types.quota_value
    import capo_service_quotas.types.service_code
    import capo_service_quotas.types.service_name


class ServiceQuotaIncreaseRequestInTemplate(TypedDict, closed=True):
    service_code: NotRequired["capo_service_quotas.types.service_code.ServiceCode"]
    """<p>Specifies the service identifier. To find the service code value for an Amazon Web Services service, use the <a>ListServices</a> operation.</p>"""
    service_name: NotRequired["capo_service_quotas.types.service_name.ServiceName"]
    """<p>Specifies the service name.</p>"""
    quota_code: NotRequired["capo_service_quotas.types.quota_code.QuotaCode"]
    """<p>Specifies the quota identifier. To find the quota code for a specific quota, use the <a>ListServiceQuotas</a> operation, and look for the <code>QuotaCode</code> response in the output for the quota you want.</p>"""
    quota_name: NotRequired["capo_service_quotas.types.quota_name.QuotaName"]
    """<p>Specifies the quota name.</p>"""
    desired_value: NotRequired["capo_service_quotas.types.quota_value.QuotaValue"]
    """<p>The new, increased value of the quota.</p>"""
    aws_region: NotRequired["capo_service_quotas.types.aws_region.AwsRegion"]
    """<p>The Amazon Web Services Region.</p>"""
    unit: NotRequired["capo_service_quotas.types.quota_unit.QuotaUnit"]
    """<p>The unit of measurement.</p>"""
    global_quota: "capo_service_quotas.types.global_quota.GlobalQuota"
    """<p>Indicates whether the quota is global.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceQuotaIncreaseRequestInTemplate) -> dict:
    out: dict = {}
    if "service_code" in value:
        out["ServiceCode"] = value["service_code"]
    if "service_name" in value:
        out["ServiceName"] = value["service_name"]
    if "quota_code" in value:
        out["QuotaCode"] = value["quota_code"]
    if "quota_name" in value:
        out["QuotaName"] = value["quota_name"]
    if "desired_value" in value:
        out["DesiredValue"] = value["desired_value"]
    if "aws_region" in value:
        out["AwsRegion"] = value["aws_region"]
    if "unit" in value:
        out["Unit"] = value["unit"]
    out["GlobalQuota"] = value.get("global_quota", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceQuotaIncreaseRequestInTemplate:
    out: ServiceQuotaIncreaseRequestInTemplate = {}  # type: ignore[typeddict-item]
    if "ServiceCode" in data:
        out["service_code"] = data["ServiceCode"]
    if "ServiceName" in data:
        out["service_name"] = data["ServiceName"]
    if "QuotaCode" in data:
        out["quota_code"] = data["QuotaCode"]
    if "QuotaName" in data:
        out["quota_name"] = data["QuotaName"]
    if "DesiredValue" in data:
        out["desired_value"] = data["DesiredValue"]
    if "AwsRegion" in data:
        out["aws_region"] = data["AwsRegion"]
    if "Unit" in data:
        out["unit"] = data["Unit"]
    if "GlobalQuota" in data:
        out["global_quota"] = data["GlobalQuota"]
    else:
        out["global_quota"] = False
    return out
