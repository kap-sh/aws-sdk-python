"""Generated from Smithy shape ``com.amazonaws.xray#SamplingRuleRecord``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_xray.types.sampling_rule
    import capo_xray.types.timestamp


class SamplingRuleRecord(TypedDict, closed=True):
    sampling_rule: NotRequired["capo_xray.types.sampling_rule.SamplingRule"]
    """<p>The sampling rule.</p>"""
    created_at: NotRequired["capo_xray.types.timestamp.Timestamp"]
    """<p>When the rule was created.</p>"""
    modified_at: NotRequired["capo_xray.types.timestamp.Timestamp"]
    """<p>When the rule was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SamplingRuleRecord) -> dict:
    out: dict = {}
    if "sampling_rule" in value:
        import capo_xray.types.sampling_rule

        out["SamplingRule"] = capo_xray.types.sampling_rule.serialize_json(
            value["sampling_rule"]
        )
    if "created_at" in value:
        import capo_xray.types.timestamp

        out["CreatedAt"] = capo_xray.types.timestamp.serialize_json(value["created_at"])
    if "modified_at" in value:
        import capo_xray.types.timestamp

        out["ModifiedAt"] = capo_xray.types.timestamp.serialize_json(
            value["modified_at"]
        )
    return out


def deserialize_json(data: dict) -> SamplingRuleRecord:
    out: SamplingRuleRecord = {}  # type: ignore[typeddict-item]
    if "SamplingRule" in data:
        import capo_xray.types.sampling_rule

        out["sampling_rule"] = capo_xray.types.sampling_rule.deserialize_json(
            data["SamplingRule"]
        )
    if "CreatedAt" in data:
        import capo_xray.types.timestamp

        out["created_at"] = capo_xray.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    if "ModifiedAt" in data:
        import capo_xray.types.timestamp

        out["modified_at"] = capo_xray.types.timestamp.deserialize_json(
            data["ModifiedAt"]
        )
    return out
