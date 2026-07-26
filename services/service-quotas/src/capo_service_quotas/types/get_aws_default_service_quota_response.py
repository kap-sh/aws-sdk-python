"""Generated from Smithy shape ``com.amazonaws.servicequotas#GetAWSDefaultServiceQuotaResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_quotas.types.service_quota


class GetAWSDefaultServiceQuotaResponse(TypedDict, closed=True):
    quota: NotRequired["capo_service_quotas.types.service_quota.ServiceQuota"]
    """<p>Information about the quota.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAWSDefaultServiceQuotaResponse) -> dict:
    out: dict = {}
    if "quota" in value:
        import capo_service_quotas.types.service_quota

        out["Quota"] = capo_service_quotas.types.service_quota.serialize_aws_json_1_1(
            value["quota"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAWSDefaultServiceQuotaResponse:
    out: GetAWSDefaultServiceQuotaResponse = {}  # type: ignore[typeddict-item]
    if "Quota" in data:
        import capo_service_quotas.types.service_quota

        out["quota"] = capo_service_quotas.types.service_quota.deserialize_aws_json_1_1(
            data["Quota"]
        )
    return out
