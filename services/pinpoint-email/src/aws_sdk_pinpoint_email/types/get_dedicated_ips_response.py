"""Generated from Smithy shape ``com.amazonaws.pinpointemail#GetDedicatedIpsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint_email.types.dedicated_ip_list
    import aws_sdk_pinpoint_email.types.next_token


class GetDedicatedIpsResponse(TypedDict, closed=True):
    dedicated_ips: NotRequired[
        "aws_sdk_pinpoint_email.types.dedicated_ip_list.DedicatedIpList"
    ]
    """<p>A list of dedicated IP addresses that are reserved for use by your Amazon Pinpoint account.</p>"""
    next_token: NotRequired["aws_sdk_pinpoint_email.types.next_token.NextToken"]
    """<p>A token that indicates that there are additional dedicated IP addresses to list. To view additional addresses, issue another request to <code>GetDedicatedIps</code>, passing this token in the <code>NextToken</code> parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDedicatedIpsResponse) -> dict:
    out: dict = {}
    if "dedicated_ips" in value:
        import aws_sdk_pinpoint_email.types.dedicated_ip_list

        out["DedicatedIps"] = (
            aws_sdk_pinpoint_email.types.dedicated_ip_list.serialize_json(
                value["dedicated_ips"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetDedicatedIpsResponse:
    out: GetDedicatedIpsResponse = {}  # type: ignore[typeddict-item]
    if "DedicatedIps" in data:
        import aws_sdk_pinpoint_email.types.dedicated_ip_list

        out["dedicated_ips"] = (
            aws_sdk_pinpoint_email.types.dedicated_ip_list.deserialize_json(
                data["DedicatedIps"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
