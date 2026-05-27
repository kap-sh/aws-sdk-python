"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteTrafficMirrorFilterRuleResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class DeleteTrafficMirrorFilterRuleResult(TypedDict):
    traffic_mirror_filter_rule_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the deleted Traffic Mirror rule.</p>"""
