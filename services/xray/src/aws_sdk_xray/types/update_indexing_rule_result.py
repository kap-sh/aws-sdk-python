"""Generated from Smithy shape ``com.amazonaws.xray#UpdateIndexingRuleResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_xray.types.indexing_rule


class UpdateIndexingRuleResult(TypedDict):
    indexing_rule: NotRequired["aws_sdk_xray.types.indexing_rule.IndexingRule"]
    """<p> Updated indexing rule. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIndexingRuleResult) -> dict:
    out: dict = {}
    if "indexing_rule" in value:
        import aws_sdk_xray.types.indexing_rule

        out["IndexingRule"] = aws_sdk_xray.types.indexing_rule.serialize_json(
            value["indexing_rule"]
        )
    return out


def deserialize_json(data: dict) -> UpdateIndexingRuleResult:
    out: UpdateIndexingRuleResult = {}  # type: ignore[typeddict-item]
    if "IndexingRule" in data:
        import aws_sdk_xray.types.indexing_rule

        out["indexing_rule"] = aws_sdk_xray.types.indexing_rule.deserialize_json(
            data["IndexingRule"]
        )
    return out
