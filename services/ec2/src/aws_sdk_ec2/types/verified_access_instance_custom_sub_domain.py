"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessInstanceCustomSubDomain``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.value_string_list


class VerifiedAccessInstanceCustomSubDomain(TypedDict):
    sub_domain: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The subdomain.</p>"""
    nameservers: NotRequired["aws_sdk_ec2.types.value_string_list.ValueStringList"]
    """<p>The name servers.</p>"""
