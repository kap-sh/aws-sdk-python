"""Generated from Smithy shape ``com.amazonaws.servicequotas#ServiceQuota``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_quotas.types.applied_level_enum
    import aws_sdk_service_quotas.types.error_reason
    import aws_sdk_service_quotas.types.global_quota
    import aws_sdk_service_quotas.types.metric_info
    import aws_sdk_service_quotas.types.quota_adjustable
    import aws_sdk_service_quotas.types.quota_arn
    import aws_sdk_service_quotas.types.quota_code
    import aws_sdk_service_quotas.types.quota_context_info
    import aws_sdk_service_quotas.types.quota_description
    import aws_sdk_service_quotas.types.quota_name
    import aws_sdk_service_quotas.types.quota_period
    import aws_sdk_service_quotas.types.quota_unit
    import aws_sdk_service_quotas.types.quota_value
    import aws_sdk_service_quotas.types.service_code
    import aws_sdk_service_quotas.types.service_name


class ServiceQuota(TypedDict):
    service_code: NotRequired["aws_sdk_service_quotas.types.service_code.ServiceCode"]
    """<p>Specifies the service identifier. To find the service code value for an Amazon Web Services service, use the <a>ListServices</a> operation.</p>"""
    service_name: NotRequired["aws_sdk_service_quotas.types.service_name.ServiceName"]
    """<p>Specifies the service name.</p>"""
    quota_arn: NotRequired["aws_sdk_service_quotas.types.quota_arn.QuotaArn"]
    """<p>The Amazon Resource Name (ARN) of the quota.</p>"""
    quota_code: NotRequired["aws_sdk_service_quotas.types.quota_code.QuotaCode"]
    """<p>Specifies the quota identifier. To find the quota code for a specific quota, use the <a>ListServiceQuotas</a> operation, and look for the <code>QuotaCode</code> response in the output for the quota you want.</p>"""
    quota_name: NotRequired["aws_sdk_service_quotas.types.quota_name.QuotaName"]
    """<p>Specifies the quota name.</p>"""
    value: NotRequired["aws_sdk_service_quotas.types.quota_value.QuotaValue"]
    """<p>The quota value.</p>"""
    unit: NotRequired["aws_sdk_service_quotas.types.quota_unit.QuotaUnit"]
    """<p>The unit of measurement.</p>"""
    adjustable: "aws_sdk_service_quotas.types.quota_adjustable.QuotaAdjustable"
    """<p>Indicates whether the quota value can be increased.</p>"""
    global_quota: "aws_sdk_service_quotas.types.global_quota.GlobalQuota"
    """<p>Indicates whether the quota is global.</p>"""
    usage_metric: NotRequired["aws_sdk_service_quotas.types.metric_info.MetricInfo"]
    """<p>Information about the measurement.</p>"""
    period: NotRequired["aws_sdk_service_quotas.types.quota_period.QuotaPeriod"]
    """<p>The period of time.</p>"""
    error_reason: NotRequired["aws_sdk_service_quotas.types.error_reason.ErrorReason"]
    """<p>The error code and error reason.</p>"""
    quota_applied_at_level: NotRequired[
        "aws_sdk_service_quotas.types.applied_level_enum.AppliedLevelEnum"
    ]
    """<p>Filters the response to return applied quota values for the <code>ACCOUNT</code>, <code>RESOURCE</code>, or <code>ALL</code> levels. <code>ACCOUNT</code> is the default.</p>"""
    quota_context: NotRequired[
        "aws_sdk_service_quotas.types.quota_context_info.QuotaContextInfo"
    ]
    """<p>The context for this service quota.</p>"""
    description: NotRequired[
        "aws_sdk_service_quotas.types.quota_description.QuotaDescription"
    ]
    """<p>The quota description. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceQuota) -> dict:
    out: dict = {}
    if "service_code" in value:
        out["ServiceCode"] = value["service_code"]
    if "service_name" in value:
        out["ServiceName"] = value["service_name"]
    if "quota_arn" in value:
        out["QuotaArn"] = value["quota_arn"]
    if "quota_code" in value:
        out["QuotaCode"] = value["quota_code"]
    if "quota_name" in value:
        out["QuotaName"] = value["quota_name"]
    if "value" in value:
        out["Value"] = value["value"]
    if "unit" in value:
        out["Unit"] = value["unit"]
    out["Adjustable"] = value.get("adjustable", False)
    out["GlobalQuota"] = value.get("global_quota", False)
    if "usage_metric" in value:
        import aws_sdk_service_quotas.types.metric_info

        out["UsageMetric"] = (
            aws_sdk_service_quotas.types.metric_info.serialize_aws_json_1_1(
                value["usage_metric"]
            )
        )
    if "period" in value:
        import aws_sdk_service_quotas.types.quota_period

        out["Period"] = (
            aws_sdk_service_quotas.types.quota_period.serialize_aws_json_1_1(
                value["period"]
            )
        )
    if "error_reason" in value:
        import aws_sdk_service_quotas.types.error_reason

        out["ErrorReason"] = (
            aws_sdk_service_quotas.types.error_reason.serialize_aws_json_1_1(
                value["error_reason"]
            )
        )
    if "quota_applied_at_level" in value:
        import aws_sdk_service_quotas.types.applied_level_enum

        out["QuotaAppliedAtLevel"] = (
            aws_sdk_service_quotas.types.applied_level_enum.serialize_aws_json_1_1(
                value["quota_applied_at_level"]
            )
        )
    if "quota_context" in value:
        import aws_sdk_service_quotas.types.quota_context_info

        out["QuotaContext"] = (
            aws_sdk_service_quotas.types.quota_context_info.serialize_aws_json_1_1(
                value["quota_context"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceQuota:
    out: ServiceQuota = {}  # type: ignore[typeddict-item]
    if "ServiceCode" in data:
        out["service_code"] = data["ServiceCode"]
    if "ServiceName" in data:
        out["service_name"] = data["ServiceName"]
    if "QuotaArn" in data:
        out["quota_arn"] = data["QuotaArn"]
    if "QuotaCode" in data:
        out["quota_code"] = data["QuotaCode"]
    if "QuotaName" in data:
        out["quota_name"] = data["QuotaName"]
    if "Value" in data:
        out["value"] = data["Value"]
    if "Unit" in data:
        out["unit"] = data["Unit"]
    if "Adjustable" in data:
        out["adjustable"] = data["Adjustable"]
    else:
        out["adjustable"] = False
    if "GlobalQuota" in data:
        out["global_quota"] = data["GlobalQuota"]
    else:
        out["global_quota"] = False
    if "UsageMetric" in data:
        import aws_sdk_service_quotas.types.metric_info

        out["usage_metric"] = (
            aws_sdk_service_quotas.types.metric_info.deserialize_aws_json_1_1(
                data["UsageMetric"]
            )
        )
    if "Period" in data:
        import aws_sdk_service_quotas.types.quota_period

        out["period"] = (
            aws_sdk_service_quotas.types.quota_period.deserialize_aws_json_1_1(
                data["Period"]
            )
        )
    if "ErrorReason" in data:
        import aws_sdk_service_quotas.types.error_reason

        out["error_reason"] = (
            aws_sdk_service_quotas.types.error_reason.deserialize_aws_json_1_1(
                data["ErrorReason"]
            )
        )
    if "QuotaAppliedAtLevel" in data:
        import aws_sdk_service_quotas.types.applied_level_enum

        out["quota_applied_at_level"] = (
            aws_sdk_service_quotas.types.applied_level_enum.deserialize_aws_json_1_1(
                data["QuotaAppliedAtLevel"]
            )
        )
    if "QuotaContext" in data:
        import aws_sdk_service_quotas.types.quota_context_info

        out["quota_context"] = (
            aws_sdk_service_quotas.types.quota_context_info.deserialize_aws_json_1_1(
                data["QuotaContext"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    return out
