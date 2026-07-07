"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2ClientVpnEndpointClientLoginBannerOptionsDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.non_empty_string


class AwsEc2ClientVpnEndpointClientLoginBannerOptionsDetails(TypedDict, closed=True):
    enabled: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p> Current state of text banner feature. </p>"""
    banner_text: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> Customizable text that will be displayed in a banner on Amazon Web Services provided clients when a VPN session is established. </p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEc2ClientVpnEndpointClientLoginBannerOptionsDetails,
) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "banner_text" in value:
        out["BannerText"] = value["banner_text"]
    return out


def deserialize_json(
    data: dict,
) -> AwsEc2ClientVpnEndpointClientLoginBannerOptionsDetails:
    out: AwsEc2ClientVpnEndpointClientLoginBannerOptionsDetails = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    if "BannerText" in data:
        out["banner_text"] = data["BannerText"]
    return out
