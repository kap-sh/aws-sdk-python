"""Generated from Smithy shape ``com.amazonaws.servicequotas#GetServiceQuotaIncreaseRequestFromTemplateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_service_quotas.types.service_quota_increase_request_in_template


class GetServiceQuotaIncreaseRequestFromTemplateResponse(TypedDict, closed=True):
    service_quota_increase_request_in_template: NotRequired[
        "aws_sdk_service_quotas.types.service_quota_increase_request_in_template.ServiceQuotaIncreaseRequestInTemplate"
    ]
    """<p>Information about the quota increase request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: GetServiceQuotaIncreaseRequestFromTemplateResponse,
) -> dict:
    out: dict = {}
    if "service_quota_increase_request_in_template" in value:
        import aws_sdk_service_quotas.types.service_quota_increase_request_in_template

        out["ServiceQuotaIncreaseRequestInTemplate"] = (
            aws_sdk_service_quotas.types.service_quota_increase_request_in_template.serialize_aws_json_1_1(
                value["service_quota_increase_request_in_template"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> GetServiceQuotaIncreaseRequestFromTemplateResponse:
    out: GetServiceQuotaIncreaseRequestFromTemplateResponse = {}  # type: ignore[typeddict-item]
    if "ServiceQuotaIncreaseRequestInTemplate" in data:
        import aws_sdk_service_quotas.types.service_quota_increase_request_in_template

        out["service_quota_increase_request_in_template"] = (
            aws_sdk_service_quotas.types.service_quota_increase_request_in_template.deserialize_aws_json_1_1(
                data["ServiceQuotaIncreaseRequestInTemplate"]
            )
        )
    return out
