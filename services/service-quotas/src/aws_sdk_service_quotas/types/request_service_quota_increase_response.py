"""Generated from Smithy shape ``com.amazonaws.servicequotas#RequestServiceQuotaIncreaseResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_quotas.types.requested_service_quota_change


class RequestServiceQuotaIncreaseResponse(TypedDict):
    requested_quota: NotRequired[
        "aws_sdk_service_quotas.types.requested_service_quota_change.RequestedServiceQuotaChange"
    ]
    """<p>Information about the quota increase request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RequestServiceQuotaIncreaseResponse) -> dict:
    out: dict = {}
    if "requested_quota" in value:
        import aws_sdk_service_quotas.types.requested_service_quota_change

        out["RequestedQuota"] = (
            aws_sdk_service_quotas.types.requested_service_quota_change.serialize_aws_json_1_1(
                value["requested_quota"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RequestServiceQuotaIncreaseResponse:
    out: RequestServiceQuotaIncreaseResponse = {}  # type: ignore[typeddict-item]
    if "RequestedQuota" in data:
        import aws_sdk_service_quotas.types.requested_service_quota_change

        out["requested_quota"] = (
            aws_sdk_service_quotas.types.requested_service_quota_change.deserialize_aws_json_1_1(
                data["RequestedQuota"]
            )
        )
    return out
