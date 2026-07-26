"""Generated from Smithy shape ``com.amazonaws.glue#GetDataQualityRulesetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.data_quality_ruleset_string
    import capo_glue.types.data_quality_target_table
    import capo_glue.types.description_string
    import capo_glue.types.hash_string
    import capo_glue.types.name_string
    import capo_glue.types.timestamp


class GetDataQualityRulesetResponse(TypedDict, closed=True):
    name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The name of the ruleset.</p>"""
    description: NotRequired["capo_glue.types.description_string.DescriptionString"]
    """<p>A description of the ruleset.</p>"""
    ruleset: NotRequired[
        "capo_glue.types.data_quality_ruleset_string.DataQualityRulesetString"
    ]
    """<p>A Data Quality Definition Language (DQDL) ruleset. For more information, see the Glue developer guide.</p>"""
    target_table: NotRequired[
        "capo_glue.types.data_quality_target_table.DataQualityTargetTable"
    ]
    """<p>The name and database name of the target table.</p>"""
    created_on: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>A timestamp. The time and date that this data quality ruleset was created.</p>"""
    last_modified_on: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>A timestamp. The last point in time when this data quality ruleset was modified.</p>"""
    recommendation_run_id: NotRequired["capo_glue.types.hash_string.HashString"]
    """<p>When a ruleset was created from a recommendation run, this run ID is generated to link the two together.</p>"""
    data_quality_security_configuration: NotRequired[
        "capo_glue.types.name_string.NameString"
    ]
    """<p>The name of the security configuration created with the data quality encryption option.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDataQualityRulesetResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "ruleset" in value:
        out["Ruleset"] = value["ruleset"]
    if "target_table" in value:
        import capo_glue.types.data_quality_target_table

        out["TargetTable"] = (
            capo_glue.types.data_quality_target_table.serialize_aws_json_1_1(
                value["target_table"]
            )
        )
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
    if "recommendation_run_id" in value:
        out["RecommendationRunId"] = value["recommendation_run_id"]
    if "data_quality_security_configuration" in value:
        out["DataQualitySecurityConfiguration"] = value[
            "data_quality_security_configuration"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDataQualityRulesetResponse:
    out: GetDataQualityRulesetResponse = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Ruleset" in data:
        out["ruleset"] = data["Ruleset"]
    if "TargetTable" in data:
        import capo_glue.types.data_quality_target_table

        out["target_table"] = (
            capo_glue.types.data_quality_target_table.deserialize_aws_json_1_1(
                data["TargetTable"]
            )
        )
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
    if "RecommendationRunId" in data:
        out["recommendation_run_id"] = data["RecommendationRunId"]
    if "DataQualitySecurityConfiguration" in data:
        out["data_quality_security_configuration"] = data[
            "DataQualitySecurityConfiguration"
        ]
    return out
