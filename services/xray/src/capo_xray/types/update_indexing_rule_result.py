"""Generated from Smithy shape ``com.amazonaws.xray#UpdateIndexingRuleResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_xray.types.indexing_rule


class UpdateIndexingRuleResult(TypedDict, closed=True):
    indexing_rule: NotRequired["capo_xray.types.indexing_rule.IndexingRule"]
    """<p> Updated indexing rule. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIndexingRuleResult) -> dict:
    out: dict = {}
    if "indexing_rule" in value:
        import capo_xray.types.indexing_rule

        out["IndexingRule"] = capo_xray.types.indexing_rule.serialize_json(
            value["indexing_rule"]
        )
    return out


def deserialize_json(data: dict) -> UpdateIndexingRuleResult:
    out: UpdateIndexingRuleResult = {}  # type: ignore[typeddict-item]
    if "IndexingRule" in data:
        import capo_xray.types.indexing_rule

        out["indexing_rule"] = capo_xray.types.indexing_rule.deserialize_json(
            data["IndexingRule"]
        )
    return out
