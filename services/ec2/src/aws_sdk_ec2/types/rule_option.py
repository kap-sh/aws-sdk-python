"""Generated from Smithy shape ``com.amazonaws.ec2#RuleOption``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.string_list


class RuleOption(TypedDict):
    keyword: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Suricata keyword.</p>"""
    settings: NotRequired["aws_sdk_ec2.types.string_list.StringList"]
    """<p>The settings for the keyword.</p>"""
