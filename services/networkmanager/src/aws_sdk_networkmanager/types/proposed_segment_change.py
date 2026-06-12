"""Generated from Smithy shape ``com.amazonaws.networkmanager#ProposedSegmentChange``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.constrained_string
    import aws_sdk_networkmanager.types.integer
    import aws_sdk_networkmanager.types.tag_list


class ProposedSegmentChange(TypedDict):
    tags: NotRequired["aws_sdk_networkmanager.types.tag_list.TagList"]
    """<p>The list of key-value tags that changed for the segment.</p>"""
    attachment_policy_rule_number: NotRequired[
        "aws_sdk_networkmanager.types.integer.Integer"
    ]
    """<p>The rule number in the policy document that applies to this change.</p>"""
    segment_name: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The name of the segment to change.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProposedSegmentChange) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_networkmanager.types.tag_list

        out["Tags"] = aws_sdk_networkmanager.types.tag_list.serialize_json(
            value["tags"]
        )
    if "attachment_policy_rule_number" in value:
        out["AttachmentPolicyRuleNumber"] = value["attachment_policy_rule_number"]
    if "segment_name" in value:
        out["SegmentName"] = value["segment_name"]
    return out


def deserialize_json(data: dict) -> ProposedSegmentChange:
    out: ProposedSegmentChange = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_networkmanager.types.tag_list

        out["tags"] = aws_sdk_networkmanager.types.tag_list.deserialize_json(
            data["Tags"]
        )
    if "AttachmentPolicyRuleNumber" in data:
        out["attachment_policy_rule_number"] = data["AttachmentPolicyRuleNumber"]
    if "SegmentName" in data:
        out["segment_name"] = data["SegmentName"]
    return out
