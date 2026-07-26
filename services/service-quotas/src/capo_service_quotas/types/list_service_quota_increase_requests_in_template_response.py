"""Generated from Smithy shape ``com.amazonaws.servicequotas#ListServiceQuotaIncreaseRequestsInTemplateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_quotas.types.next_token
    import capo_service_quotas.types.service_quota_increase_request_in_template_list


class ListServiceQuotaIncreaseRequestsInTemplateResponse(TypedDict, closed=True):
    service_quota_increase_request_in_template_list: NotRequired[
        "capo_service_quotas.types.service_quota_increase_request_in_template_list.ServiceQuotaIncreaseRequestInTemplateList"
    ]
    """<p>Information about the quota increase requests.</p>"""
    next_token: NotRequired["capo_service_quotas.types.next_token.NextToken"]
    """<p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the <code>NextToken</code> response element comes back as <code>null</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: ListServiceQuotaIncreaseRequestsInTemplateResponse,
) -> dict:
    out: dict = {}
    if "service_quota_increase_request_in_template_list" in value:
        import capo_service_quotas.types.service_quota_increase_request_in_template_list

        out["ServiceQuotaIncreaseRequestInTemplateList"] = (
            capo_service_quotas.types.service_quota_increase_request_in_template_list.serialize_aws_json_1_1(
                value["service_quota_increase_request_in_template_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> ListServiceQuotaIncreaseRequestsInTemplateResponse:
    out: ListServiceQuotaIncreaseRequestsInTemplateResponse = {}  # type: ignore[typeddict-item]
    if "ServiceQuotaIncreaseRequestInTemplateList" in data:
        import capo_service_quotas.types.service_quota_increase_request_in_template_list

        out["service_quota_increase_request_in_template_list"] = (
            capo_service_quotas.types.service_quota_increase_request_in_template_list.deserialize_aws_json_1_1(
                data["ServiceQuotaIncreaseRequestInTemplateList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
