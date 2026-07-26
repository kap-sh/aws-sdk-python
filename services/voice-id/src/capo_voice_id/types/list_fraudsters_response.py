"""Generated from Smithy shape ``com.amazonaws.voiceid#ListFraudstersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_voice_id.types.fraudster_summaries
    import capo_voice_id.types.string


class ListFraudstersResponse(TypedDict, closed=True):
    fraudster_summaries: NotRequired[
        "capo_voice_id.types.fraudster_summaries.FraudsterSummaries"
    ]
    """<p>A list that contains details about each fraudster in the Amazon Web Services account. </p>"""
    next_token: NotRequired["capo_voice_id.types.string.String"]
    """<p>If <code>NextToken</code> is returned, there are more results available. The value of <code>NextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListFraudstersResponse) -> dict:
    out: dict = {}
    if "fraudster_summaries" in value:
        import capo_voice_id.types.fraudster_summaries

        out["FraudsterSummaries"] = (
            capo_voice_id.types.fraudster_summaries.serialize_aws_json_1_0(
                value["fraudster_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListFraudstersResponse:
    out: ListFraudstersResponse = {}  # type: ignore[typeddict-item]
    if "FraudsterSummaries" in data:
        import capo_voice_id.types.fraudster_summaries

        out["fraudster_summaries"] = (
            capo_voice_id.types.fraudster_summaries.deserialize_aws_json_1_0(
                data["FraudsterSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
