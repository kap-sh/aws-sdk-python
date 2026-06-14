"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListBrowserProfilesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.browser_profile_summaries
    import aws_sdk_bedrock_agentcore_control.types.next_token


class ListBrowserProfilesResponse(TypedDict):
    profile_summaries: "aws_sdk_bedrock_agentcore_control.types.browser_profile_summaries.BrowserProfileSummaries"
    """<p>The list of browser profile summaries.</p>"""
    next_token: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.next_token.NextToken"
    ]
    """<p>A token to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBrowserProfilesResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore_control.types.browser_profile_summaries

    out["profileSummaries"] = (
        aws_sdk_bedrock_agentcore_control.types.browser_profile_summaries.serialize_json(
            value["profile_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListBrowserProfilesResponse:
    out: ListBrowserProfilesResponse = {}  # type: ignore[typeddict-item]
    if "profileSummaries" in data:
        import aws_sdk_bedrock_agentcore_control.types.browser_profile_summaries

        out["profile_summaries"] = (
            aws_sdk_bedrock_agentcore_control.types.browser_profile_summaries.deserialize_json(
                data["profileSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListBrowserProfilesResponse.profile_summaries required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
