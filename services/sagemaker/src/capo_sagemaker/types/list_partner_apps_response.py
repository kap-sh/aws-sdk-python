"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListPartnerAppsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.next_token
    import capo_sagemaker.types.partner_app_summaries


class ListPartnerAppsResponse(TypedDict, closed=True):
    summaries: NotRequired[
        "capo_sagemaker.types.partner_app_summaries.PartnerAppSummaries"
    ]
    """<p>The information related to each of the SageMaker Partner AI Apps in an account.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>If the previous response was truncated, you will receive this token. Use it in your next request to receive the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPartnerAppsResponse) -> dict:
    out: dict = {}
    if "summaries" in value:
        import capo_sagemaker.types.partner_app_summaries

        out["Summaries"] = (
            capo_sagemaker.types.partner_app_summaries.serialize_aws_json_1_1(
                value["summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPartnerAppsResponse:
    out: ListPartnerAppsResponse = {}  # type: ignore[typeddict-item]
    if "Summaries" in data:
        import capo_sagemaker.types.partner_app_summaries

        out["summaries"] = (
            capo_sagemaker.types.partner_app_summaries.deserialize_aws_json_1_1(
                data["Summaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
