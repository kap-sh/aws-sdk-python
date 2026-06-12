"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListAccessPoliciesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.access_policy_summaries
    import aws_sdk_iotsitewise.types.next_token


class ListAccessPoliciesResponse(TypedDict):
    access_policy_summaries: (
        "aws_sdk_iotsitewise.types.access_policy_summaries.AccessPolicySummaries"
    )
    """<p>A list that summarizes each access policy.</p>"""
    next_token: NotRequired["aws_sdk_iotsitewise.types.next_token.NextToken"]
    """<p>The token for the next set of results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAccessPoliciesResponse) -> dict:
    out: dict = {}
    import aws_sdk_iotsitewise.types.access_policy_summaries

    out["accessPolicySummaries"] = (
        aws_sdk_iotsitewise.types.access_policy_summaries.serialize_json(
            value["access_policy_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAccessPoliciesResponse:
    out: ListAccessPoliciesResponse = {}  # type: ignore[typeddict-item]
    if "accessPolicySummaries" in data:
        import aws_sdk_iotsitewise.types.access_policy_summaries

        out["access_policy_summaries"] = (
            aws_sdk_iotsitewise.types.access_policy_summaries.deserialize_json(
                data["accessPolicySummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListAccessPoliciesResponse.access_policy_summaries required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
