"""Generated from Smithy shape ``com.amazonaws.securitylake#ListLogSourcesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securitylake.types.log_source_list
    import capo_securitylake.types.next_token


class ListLogSourcesResponse(TypedDict, closed=True):
    sources: NotRequired["capo_securitylake.types.log_source_list.LogSourceList"]
    """<p>The list of log sources in your organization that send data to the data lake.</p>"""
    next_token: NotRequired["capo_securitylake.types.next_token.NextToken"]
    """<p>If nextToken is returned, there are more results available. You can repeat the call using the returned token to retrieve the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLogSourcesResponse) -> dict:
    out: dict = {}
    if "sources" in value:
        import capo_securitylake.types.log_source_list

        out["sources"] = capo_securitylake.types.log_source_list.serialize_json(
            value["sources"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListLogSourcesResponse:
    out: ListLogSourcesResponse = {}  # type: ignore[typeddict-item]
    if "sources" in data:
        import capo_securitylake.types.log_source_list

        out["sources"] = capo_securitylake.types.log_source_list.deserialize_json(
            data["sources"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
