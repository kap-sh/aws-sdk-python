"""Generated from Smithy shape ``com.amazonaws.lightsail#GetStaticIpsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.static_ip_list
    import capo_lightsail.types.string


class GetStaticIpsResult(TypedDict, closed=True):
    static_ips: NotRequired["capo_lightsail.types.static_ip_list.StaticIpList"]
    """<p>An array of key-value pairs containing information about your get static IPs request.</p>"""
    next_page_token: NotRequired["capo_lightsail.types.string.string"]
    """<p>The token to advance to the next page of results from your request.</p> <p>A next page token is not returned if there are no more results to display.</p> <p>To get the next page of results, perform another <code>GetStaticIps</code> request and specify the next page token using the <code>pageToken</code> parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetStaticIpsResult) -> dict:
    out: dict = {}
    if "static_ips" in value:
        import capo_lightsail.types.static_ip_list

        out["staticIps"] = capo_lightsail.types.static_ip_list.serialize_aws_json_1_1(
            value["static_ips"]
        )
    if "next_page_token" in value:
        out["nextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetStaticIpsResult:
    out: GetStaticIpsResult = {}  # type: ignore[typeddict-item]
    if "staticIps" in data:
        import capo_lightsail.types.static_ip_list

        out["static_ips"] = (
            capo_lightsail.types.static_ip_list.deserialize_aws_json_1_1(
                data["staticIps"]
            )
        )
    if "nextPageToken" in data:
        out["next_page_token"] = data["nextPageToken"]
    return out
