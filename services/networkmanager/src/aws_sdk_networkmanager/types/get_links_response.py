"""Generated from Smithy shape ``com.amazonaws.networkmanager#GetLinksResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.link_list
    import aws_sdk_networkmanager.types.next_token


class GetLinksResponse(TypedDict, closed=True):
    links: NotRequired["aws_sdk_networkmanager.types.link_list.LinkList"]
    """<p>The links.</p>"""
    next_token: NotRequired["aws_sdk_networkmanager.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLinksResponse) -> dict:
    out: dict = {}
    if "links" in value:
        import aws_sdk_networkmanager.types.link_list

        out["Links"] = aws_sdk_networkmanager.types.link_list.serialize_json(
            value["links"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetLinksResponse:
    out: GetLinksResponse = {}  # type: ignore[typeddict-item]
    if "Links" in data:
        import aws_sdk_networkmanager.types.link_list

        out["links"] = aws_sdk_networkmanager.types.link_list.deserialize_json(
            data["Links"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
