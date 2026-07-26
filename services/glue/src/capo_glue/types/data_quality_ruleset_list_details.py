"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityRulesetListDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.data_quality_target_table
    import capo_glue.types.description_string
    import capo_glue.types.hash_string
    import capo_glue.types.name_string
    import capo_glue.types.nullable_integer
    import capo_glue.types.timestamp


class DataQualityRulesetListDetails(TypedDict, closed=True):
    name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The name of the data quality ruleset.</p>"""
    description: NotRequired["capo_glue.types.description_string.DescriptionString"]
    """<p>A description of the data quality ruleset.</p>"""
    created_on: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>The date and time the data quality ruleset was created.</p>"""
    last_modified_on: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>The date and time the data quality ruleset was last modified.</p>"""
    target_table: NotRequired[
        "capo_glue.types.data_quality_target_table.DataQualityTargetTable"
    ]
    """<p>An object representing an Glue table.</p>"""
    recommendation_run_id: NotRequired["capo_glue.types.hash_string.HashString"]
    """<p>When a ruleset was created from a recommendation run, this run ID is generated to link the two together.</p>"""
    rule_count: NotRequired["capo_glue.types.nullable_integer.NullableInteger"]
    """<p>The number of rules in the ruleset.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityRulesetListDetails) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "created_on" in value:
        import capo_glue.types.timestamp

        out["CreatedOn"] = capo_glue.types.timestamp.serialize_aws_json_1_1(
            value["created_on"]
        )
    if "last_modified_on" in value:
        import capo_glue.types.timestamp

        out["LastModifiedOn"] = capo_glue.types.timestamp.serialize_aws_json_1_1(
            value["last_modified_on"]
        )
    if "target_table" in value:
        import capo_glue.types.data_quality_target_table

        out["TargetTable"] = (
            capo_glue.types.data_quality_target_table.serialize_aws_json_1_1(
                value["target_table"]
            )
        )
    if "recommendation_run_id" in value:
        out["RecommendationRunId"] = value["recommendation_run_id"]
    if "rule_count" in value:
        out["RuleCount"] = value["rule_count"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DataQualityRulesetListDetails:
    out: DataQualityRulesetListDetails = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "CreatedOn" in data:
        import capo_glue.types.timestamp

        out["created_on"] = capo_glue.types.timestamp.deserialize_aws_json_1_1(
            data["CreatedOn"]
        )
    if "LastModifiedOn" in data:
        import capo_glue.types.timestamp

        out["last_modified_on"] = capo_glue.types.timestamp.deserialize_aws_json_1_1(
            data["LastModifiedOn"]
        )
    if "TargetTable" in data:
        import capo_glue.types.data_quality_target_table

        out["target_table"] = (
            capo_glue.types.data_quality_target_table.deserialize_aws_json_1_1(
                data["TargetTable"]
            )
        )
    if "RecommendationRunId" in data:
        out["recommendation_run_id"] = data["RecommendationRunId"]
    if "RuleCount" in data:
        out["rule_count"] = data["RuleCount"]
    return out
