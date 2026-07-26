"""Generated from Smithy shape ``com.amazonaws.networkmanager#ProposedSegmentChange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.constrained_string
    import capo_networkmanager.types.integer
    import capo_networkmanager.types.tag_list


class ProposedSegmentChange(TypedDict, closed=True):
    tags: NotRequired["capo_networkmanager.types.tag_list.TagList"]
    """<p>The list of key-value tags that changed for the segment.</p>"""
    attachment_policy_rule_number: NotRequired[
        "capo_networkmanager.types.integer.Integer"
    ]
    """<p>The rule number in the policy document that applies to this change.</p>"""
    segment_name: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The name of the segment to change.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProposedSegmentChange) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_networkmanager.types.tag_list

        out["Tags"] = capo_networkmanager.types.tag_list.serialize_json(value["tags"])
    if "attachment_policy_rule_number" in value:
        out["AttachmentPolicyRuleNumber"] = value["attachment_policy_rule_number"]
    if "segment_name" in value:
        out["SegmentName"] = value["segment_name"]
    return out


def deserialize_json(data: dict) -> ProposedSegmentChange:
    out: ProposedSegmentChange = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import capo_networkmanager.types.tag_list

        out["tags"] = capo_networkmanager.types.tag_list.deserialize_json(data["Tags"])
    if "AttachmentPolicyRuleNumber" in data:
        out["attachment_policy_rule_number"] = data["AttachmentPolicyRuleNumber"]
    if "SegmentName" in data:
        out["segment_name"] = data["SegmentName"]
    return out
