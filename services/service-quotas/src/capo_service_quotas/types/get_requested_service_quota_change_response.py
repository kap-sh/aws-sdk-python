"""Generated from Smithy shape ``com.amazonaws.servicequotas#GetRequestedServiceQuotaChangeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_quotas.types.requested_service_quota_change


class GetRequestedServiceQuotaChangeResponse(TypedDict, closed=True):
    requested_quota: NotRequired[
        "capo_service_quotas.types.requested_service_quota_change.RequestedServiceQuotaChange"
    ]
    """<p>Information about the quota increase request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRequestedServiceQuotaChangeResponse) -> dict:
    out: dict = {}
    if "requested_quota" in value:
        import capo_service_quotas.types.requested_service_quota_change

        out["RequestedQuota"] = (
            capo_service_quotas.types.requested_service_quota_change.serialize_aws_json_1_1(
                value["requested_quota"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRequestedServiceQuotaChangeResponse:
    out: GetRequestedServiceQuotaChangeResponse = {}  # type: ignore[typeddict-item]
    if "RequestedQuota" in data:
        import capo_service_quotas.types.requested_service_quota_change

        out["requested_quota"] = (
            capo_service_quotas.types.requested_service_quota_change.deserialize_aws_json_1_1(
                data["RequestedQuota"]
            )
        )
    return out
