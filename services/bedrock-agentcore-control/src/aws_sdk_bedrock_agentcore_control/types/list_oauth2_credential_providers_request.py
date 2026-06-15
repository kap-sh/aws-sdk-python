"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListOauth2CredentialProvidersRequest``."""

from typing import TypedDict

from typing_extensions import NotRequired


class ListOauth2CredentialProvidersRequest(TypedDict):
    next_token: NotRequired["str"]
    """<p>Pagination token.</p>"""
    max_results: "int"
    """<p>Maximum number of results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListOauth2CredentialProvidersRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    out["maxResults"] = value.get("max_results", 10)
    return out


def deserialize_json(data: dict) -> ListOauth2CredentialProvidersRequest:
    out: ListOauth2CredentialProvidersRequest = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    else:
        out["max_results"] = 10
    return out
