"""Generated from Smithy shape ``com.amazonaws.servicequotas#QuotaUtilizationInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_quotas.types.applied_value
    import capo_service_quotas.types.default_value
    import capo_service_quotas.types.quota_adjustable
    import capo_service_quotas.types.quota_code
    import capo_service_quotas.types.quota_metric_namespace
    import capo_service_quotas.types.quota_name
    import capo_service_quotas.types.service_code
    import capo_service_quotas.types.service_name
    import capo_service_quotas.types.utilization_pct


class QuotaUtilizationInfo(TypedDict, closed=True):
    quota_code: NotRequired["capo_service_quotas.types.quota_code.QuotaCode"]
    """<p>The quota identifier.</p>"""
    service_code: NotRequired["capo_service_quotas.types.service_code.ServiceCode"]
    """<p>The service identifier.</p>"""
    quota_name: NotRequired["capo_service_quotas.types.quota_name.QuotaName"]
    """<p>The quota name.</p>"""
    namespace: NotRequired[
        "capo_service_quotas.types.quota_metric_namespace.QuotaMetricNamespace"
    ]
    """<p>The namespace of the metric used to track quota usage.</p>"""
    utilization: NotRequired["capo_service_quotas.types.utilization_pct.UtilizationPct"]
    """<p>The utilization percentage of the quota, calculated as (current usage / applied value) × 100. Values range from 0.0 to 100.0 or higher if usage exceeds the quota limit.</p>"""
    default_value: NotRequired["capo_service_quotas.types.default_value.DefaultValue"]
    """<p>The default value of the quota.</p>"""
    applied_value: NotRequired["capo_service_quotas.types.applied_value.AppliedValue"]
    """<p>The applied value of the quota, which may be higher than the default value if a quota increase has been requested and approved.</p>"""
    service_name: NotRequired["capo_service_quotas.types.service_name.ServiceName"]
    """<p>The service name.</p>"""
    adjustable: "capo_service_quotas.types.quota_adjustable.QuotaAdjustable"
    """<p>Indicates whether the quota value can be increased.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QuotaUtilizationInfo) -> dict:
    out: dict = {}
    if "quota_code" in value:
        out["QuotaCode"] = value["quota_code"]
    if "service_code" in value:
        out["ServiceCode"] = value["service_code"]
    if "quota_name" in value:
        out["QuotaName"] = value["quota_name"]
    if "namespace" in value:
        out["Namespace"] = value["namespace"]
    if "utilization" in value:
        out["Utilization"] = value["utilization"]
    if "default_value" in value:
        out["DefaultValue"] = value["default_value"]
    if "applied_value" in value:
        out["AppliedValue"] = value["applied_value"]
    if "service_name" in value:
        out["ServiceName"] = value["service_name"]
    out["Adjustable"] = value.get("adjustable", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> QuotaUtilizationInfo:
    out: QuotaUtilizationInfo = {}  # type: ignore[typeddict-item]
    if "QuotaCode" in data:
        out["quota_code"] = data["QuotaCode"]
    if "ServiceCode" in data:
        out["service_code"] = data["ServiceCode"]
    if "QuotaName" in data:
        out["quota_name"] = data["QuotaName"]
    if "Namespace" in data:
        out["namespace"] = data["Namespace"]
    if "Utilization" in data:
        out["utilization"] = data["Utilization"]
    if "DefaultValue" in data:
        out["default_value"] = data["DefaultValue"]
    if "AppliedValue" in data:
        out["applied_value"] = data["AppliedValue"]
    if "ServiceName" in data:
        out["service_name"] = data["ServiceName"]
    if "Adjustable" in data:
        out["adjustable"] = data["Adjustable"]
    else:
        out["adjustable"] = False
    return out
