"""Generated from Smithy shape ``com.amazonaws.xray#GetIndexingRulesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_xray.types.indexing_rule_list
    import aws_sdk_xray.types.string


class GetIndexingRulesResult(TypedDict):
    indexing_rules: NotRequired[
        "aws_sdk_xray.types.indexing_rule_list.IndexingRuleList"
    ]
    """<p> Retrieves all indexing rules.</p>"""
    next_token: NotRequired["aws_sdk_xray.types.string.String"]
    """<p> Specify the pagination token returned by a previous request to retrieve the next page of indexes. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIndexingRulesResult) -> dict:
    out: dict = {}
    if "indexing_rules" in value:
        import aws_sdk_xray.types.indexing_rule_list

        out["IndexingRules"] = aws_sdk_xray.types.indexing_rule_list.serialize_json(
            value["indexing_rules"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetIndexingRulesResult:
    out: GetIndexingRulesResult = {}  # type: ignore[typeddict-item]
    if "IndexingRules" in data:
        import aws_sdk_xray.types.indexing_rule_list

        out["indexing_rules"] = aws_sdk_xray.types.indexing_rule_list.deserialize_json(
            data["IndexingRules"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
