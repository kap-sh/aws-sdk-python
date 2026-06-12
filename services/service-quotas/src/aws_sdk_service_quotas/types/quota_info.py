"""Generated from Smithy shape ``com.amazonaws.servicequotas#QuotaInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_quotas.types.quota_code
    import aws_sdk_service_quotas.types.quota_name


class QuotaInfo(TypedDict):
    quota_code: NotRequired["aws_sdk_service_quotas.types.quota_code.QuotaCode"]
    """<p>The Service Quotas code for the Amazon Web Services service monitored with Automatic Management.</p>"""
    quota_name: NotRequired["aws_sdk_service_quotas.types.quota_name.QuotaName"]
    """<p>The Service Quotas name for the Amazon Web Services service monitored with Automatic Management.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QuotaInfo) -> dict:
    out: dict = {}
    if "quota_code" in value:
        out["QuotaCode"] = value["quota_code"]
    if "quota_name" in value:
        out["QuotaName"] = value["quota_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> QuotaInfo:
    out: QuotaInfo = {}  # type: ignore[typeddict-item]
    if "QuotaCode" in data:
        out["quota_code"] = data["QuotaCode"]
    if "QuotaName" in data:
        out["quota_name"] = data["QuotaName"]
    return out
