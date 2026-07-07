"""Generated from Smithy shape ``com.amazonaws.glue#ListDataQualityRulesetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.data_quality_ruleset_list
    import aws_sdk_glue.types.pagination_token


class ListDataQualityRulesetsResponse(TypedDict, closed=True):
    rulesets: NotRequired[
        "aws_sdk_glue.types.data_quality_ruleset_list.DataQualityRulesetList"
    ]
    """<p>A paginated list of rulesets for the specified list of Glue tables.</p>"""
    next_token: NotRequired["aws_sdk_glue.types.pagination_token.PaginationToken"]
    """<p>A pagination token, if more results are available.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDataQualityRulesetsResponse) -> dict:
    out: dict = {}
    if "rulesets" in value:
        import aws_sdk_glue.types.data_quality_ruleset_list

        out["Rulesets"] = (
            aws_sdk_glue.types.data_quality_ruleset_list.serialize_aws_json_1_1(
                value["rulesets"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDataQualityRulesetsResponse:
    out: ListDataQualityRulesetsResponse = {}  # type: ignore[typeddict-item]
    if "Rulesets" in data:
        import aws_sdk_glue.types.data_quality_ruleset_list

        out["rulesets"] = (
            aws_sdk_glue.types.data_quality_ruleset_list.deserialize_aws_json_1_1(
                data["Rulesets"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
