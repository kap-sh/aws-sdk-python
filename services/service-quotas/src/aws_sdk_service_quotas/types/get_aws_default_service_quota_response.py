"""Generated from Smithy shape ``com.amazonaws.servicequotas#GetAWSDefaultServiceQuotaResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_quotas.types.service_quota


class GetAWSDefaultServiceQuotaResponse(TypedDict):
    quota: NotRequired["aws_sdk_service_quotas.types.service_quota.ServiceQuota"]
    """<p>Information about the quota.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAWSDefaultServiceQuotaResponse) -> dict:
    out: dict = {}
    if "quota" in value:
        import aws_sdk_service_quotas.types.service_quota

        out["Quota"] = (
            aws_sdk_service_quotas.types.service_quota.serialize_aws_json_1_1(
                value["quota"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAWSDefaultServiceQuotaResponse:
    out: GetAWSDefaultServiceQuotaResponse = {}  # type: ignore[typeddict-item]
    if "Quota" in data:
        import aws_sdk_service_quotas.types.service_quota

        out["quota"] = (
            aws_sdk_service_quotas.types.service_quota.deserialize_aws_json_1_1(
                data["Quota"]
            )
        )
    return out
