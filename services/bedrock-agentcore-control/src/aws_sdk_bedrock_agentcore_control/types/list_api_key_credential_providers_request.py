"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListApiKeyCredentialProvidersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.max_results


class ListApiKeyCredentialProvidersRequest(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>Pagination token.</p>"""
    max_results: "aws_sdk_bedrock_agentcore_control.types.max_results.MaxResults"
    """<p>Maximum number of results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListApiKeyCredentialProvidersRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    out["maxResults"] = value.get("max_results", 10)
    return out


def deserialize_json(data: dict) -> ListApiKeyCredentialProvidersRequest:
    out: ListApiKeyCredentialProvidersRequest = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    else:
        out["max_results"] = 10
    return out
