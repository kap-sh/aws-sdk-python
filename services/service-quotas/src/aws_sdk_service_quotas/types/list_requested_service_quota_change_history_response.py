"""Generated from Smithy shape ``com.amazonaws.servicequotas#ListRequestedServiceQuotaChangeHistoryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_service_quotas.types.next_token
    import aws_sdk_service_quotas.types.requested_service_quota_change_history_list_definition


class ListRequestedServiceQuotaChangeHistoryResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_service_quotas.types.next_token.NextToken"]
    """<p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the <code>NextToken</code> response element comes back as <code>null</code>.</p>"""
    requested_quotas: NotRequired[
        "aws_sdk_service_quotas.types.requested_service_quota_change_history_list_definition.RequestedServiceQuotaChangeHistoryListDefinition"
    ]
    """<p>Information about the quota increase requests.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: ListRequestedServiceQuotaChangeHistoryResponse,
) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "requested_quotas" in value:
        import aws_sdk_service_quotas.types.requested_service_quota_change_history_list_definition

        out["RequestedQuotas"] = (
            aws_sdk_service_quotas.types.requested_service_quota_change_history_list_definition.serialize_aws_json_1_1(
                value["requested_quotas"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> ListRequestedServiceQuotaChangeHistoryResponse:
    out: ListRequestedServiceQuotaChangeHistoryResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "RequestedQuotas" in data:
        import aws_sdk_service_quotas.types.requested_service_quota_change_history_list_definition

        out["requested_quotas"] = (
            aws_sdk_service_quotas.types.requested_service_quota_change_history_list_definition.deserialize_aws_json_1_1(
                data["RequestedQuotas"]
            )
        )
    return out
