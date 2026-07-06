"""Generated from Smithy shape ``com.amazonaws.networkmanager#GetSitesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.next_token
    import aws_sdk_networkmanager.types.site_list


class GetSitesResponse(TypedDict, closed=True):
    sites: NotRequired["aws_sdk_networkmanager.types.site_list.SiteList"]
    """<p>The sites.</p>"""
    next_token: NotRequired["aws_sdk_networkmanager.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSitesResponse) -> dict:
    out: dict = {}
    if "sites" in value:
        import aws_sdk_networkmanager.types.site_list

        out["Sites"] = aws_sdk_networkmanager.types.site_list.serialize_json(
            value["sites"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetSitesResponse:
    out: GetSitesResponse = {}  # type: ignore[typeddict-item]
    if "Sites" in data:
        import aws_sdk_networkmanager.types.site_list

        out["sites"] = aws_sdk_networkmanager.types.site_list.deserialize_json(
            data["Sites"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
