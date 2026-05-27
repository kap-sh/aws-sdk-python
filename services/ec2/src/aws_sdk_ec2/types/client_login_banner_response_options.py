"""Generated from Smithy shape ``com.amazonaws.ec2#ClientLoginBannerResponseOptions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string


class ClientLoginBannerResponseOptions(TypedDict):
    enabled: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Current state of text banner feature.</p> <p>Valid values: <code>true | false</code> </p>"""
    banner_text: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Customizable text that will be displayed in a banner on Amazon Web Services provided clients when a VPN session is established. UTF-8 encoded characters only. Maximum of 1400 characters.</p>"""
