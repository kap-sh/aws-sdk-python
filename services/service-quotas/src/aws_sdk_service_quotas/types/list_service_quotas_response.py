"""Generated from Smithy shape ``com.amazonaws.servicequotas#ListServiceQuotasResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_service_quotas.types.next_token
    import aws_sdk_service_quotas.types.service_quota_list_definition


class ListServiceQuotasResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_service_quotas.types.next_token.NextToken"]
    """<p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the <code>NextToken</code> response element comes back as <code>null</code>.</p>"""
    quotas: NotRequired[
        "aws_sdk_service_quotas.types.service_quota_list_definition.ServiceQuotaListDefinition"
    ]
    """<p>Information about the quotas.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListServiceQuotasResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "quotas" in value:
        import aws_sdk_service_quotas.types.service_quota_list_definition

        out["Quotas"] = (
            aws_sdk_service_quotas.types.service_quota_list_definition.serialize_aws_json_1_1(
                value["quotas"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListServiceQuotasResponse:
    out: ListServiceQuotasResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Quotas" in data:
        import aws_sdk_service_quotas.types.service_quota_list_definition

        out["quotas"] = (
            aws_sdk_service_quotas.types.service_quota_list_definition.deserialize_aws_json_1_1(
                data["Quotas"]
            )
        )
    return out
