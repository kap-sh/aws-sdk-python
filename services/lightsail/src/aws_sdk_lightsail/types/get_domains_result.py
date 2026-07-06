"""Generated from Smithy shape ``com.amazonaws.lightsail#GetDomainsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.domain_list
    import aws_sdk_lightsail.types.string


class GetDomainsResult(TypedDict, closed=True):
    domains: NotRequired["aws_sdk_lightsail.types.domain_list.DomainList"]
    """<p>An array of key-value pairs containing information about each of the domain entries in the user's account.</p>"""
    next_page_token: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The token to advance to the next page of results from your request.</p> <p>A next page token is not returned if there are no more results to display.</p> <p>To get the next page of results, perform another <code>GetDomains</code> request and specify the next page token using the <code>pageToken</code> parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDomainsResult) -> dict:
    out: dict = {}
    if "domains" in value:
        import aws_sdk_lightsail.types.domain_list

        out["domains"] = aws_sdk_lightsail.types.domain_list.serialize_aws_json_1_1(
            value["domains"]
        )
    if "next_page_token" in value:
        out["nextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDomainsResult:
    out: GetDomainsResult = {}  # type: ignore[typeddict-item]
    if "domains" in data:
        import aws_sdk_lightsail.types.domain_list

        out["domains"] = aws_sdk_lightsail.types.domain_list.deserialize_aws_json_1_1(
            data["domains"]
        )
    if "nextPageToken" in data:
        out["next_page_token"] = data["nextPageToken"]
    return out
