"""Generated from Smithy shape ``com.amazonaws.xray#IndexingRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_xray.types.indexing_rule_value
    import capo_xray.types.rule_name
    import capo_xray.types.timestamp


class IndexingRule(TypedDict, closed=True):
    name: NotRequired["capo_xray.types.rule_name.RuleName"]
    """<p> The name of the indexing rule. </p>"""
    modified_at: NotRequired["capo_xray.types.timestamp.Timestamp"]
    """<p> Displays when the rule was last modified, in Unix time seconds. </p>"""
    rule: NotRequired["capo_xray.types.indexing_rule_value.IndexingRuleValue"]
    """<p> The indexing rule. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IndexingRule) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "modified_at" in value:
        import capo_xray.types.timestamp

        out["ModifiedAt"] = capo_xray.types.timestamp.serialize_json(
            value["modified_at"]
        )
    if "rule" in value:
        import capo_xray.types.indexing_rule_value

        out["Rule"] = capo_xray.types.indexing_rule_value.serialize_json(value["rule"])
    return out


def deserialize_json(data: dict) -> IndexingRule:
    out: IndexingRule = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "ModifiedAt" in data:
        import capo_xray.types.timestamp

        out["modified_at"] = capo_xray.types.timestamp.deserialize_json(
            data["ModifiedAt"]
        )
    if "Rule" in data:
        import capo_xray.types.indexing_rule_value

        out["rule"] = capo_xray.types.indexing_rule_value.deserialize_json(data["Rule"])
    return out
