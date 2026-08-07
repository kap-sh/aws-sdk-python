"""Generated from Smithy shape ``com.amazonaws.sns#ListEndpointsByPlatformApplicationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sns._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sns.types.list_of_endpoints
    import capo_sns.types.string


class ListEndpointsByPlatformApplicationResponse(TypedDict, closed=True):
    endpoints: NotRequired["capo_sns.types.list_of_endpoints.ListOfEndpoints"]
    """<p>Endpoints returned for <code>ListEndpointsByPlatformApplication</code> action.</p>"""
    next_token: NotRequired["capo_sns.types.string.String"]
    """<p> <code>NextToken</code> string is returned when calling <code>ListEndpointsByPlatformApplication</code> action if additional records are available after the first page results.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListEndpointsByPlatformApplicationResponse,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "endpoints" in value:
        import capo_sns.types.list_of_endpoints

        capo_sns.types.list_of_endpoints.serialize_query(
            value["endpoints"], pairs, f"{key_prefix}Endpoints"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ListEndpointsByPlatformApplicationResponse:
    out: ListEndpointsByPlatformApplicationResponse = {}  # type: ignore[typeddict-item]
    child_endpoints = el.find("Endpoints")
    if child_endpoints is not None:
        import capo_sns.types.list_of_endpoints

        out["endpoints"] = capo_sns.types.list_of_endpoints.deserialize_query(
            child_endpoints
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
