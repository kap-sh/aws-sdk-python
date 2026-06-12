"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ListProfileSharesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.next_token
    import aws_sdk_wellarchitected.types.profile_share_summaries


class ListProfileSharesOutput(TypedDict):
    profile_share_summaries: NotRequired[
        "aws_sdk_wellarchitected.types.profile_share_summaries.ProfileShareSummaries"
    ]
    """<p>Profile share summaries.</p>"""
    next_token: NotRequired["aws_sdk_wellarchitected.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListProfileSharesOutput) -> dict:
    out: dict = {}
    if "profile_share_summaries" in value:
        import aws_sdk_wellarchitected.types.profile_share_summaries

        out["ProfileShareSummaries"] = (
            aws_sdk_wellarchitected.types.profile_share_summaries.serialize_json(
                value["profile_share_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListProfileSharesOutput:
    out: ListProfileSharesOutput = {}  # type: ignore[typeddict-item]
    if "ProfileShareSummaries" in data:
        import aws_sdk_wellarchitected.types.profile_share_summaries

        out["profile_share_summaries"] = (
            aws_sdk_wellarchitected.types.profile_share_summaries.deserialize_json(
                data["ProfileShareSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
