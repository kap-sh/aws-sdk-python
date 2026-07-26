"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityRulesetFilterCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.data_quality_target_table
    import capo_glue.types.description_string
    import capo_glue.types.name_string
    import capo_glue.types.timestamp


class DataQualityRulesetFilterCriteria(TypedDict, closed=True):
    name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The name of the ruleset filter criteria.</p>"""
    description: NotRequired["capo_glue.types.description_string.DescriptionString"]
    """<p>The description of the ruleset filter criteria.</p>"""
    created_before: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>Filter on rulesets created before this date.</p>"""
    created_after: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>Filter on rulesets created after this date.</p>"""
    last_modified_before: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>Filter on rulesets last modified before this date.</p>"""
    last_modified_after: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>Filter on rulesets last modified after this date.</p>"""
    target_table: NotRequired[
        "capo_glue.types.data_quality_target_table.DataQualityTargetTable"
    ]
    """<p>The name and database name of the target table.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityRulesetFilterCriteria) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "created_before" in value:
        import capo_glue.types.timestamp

        out["CreatedBefore"] = capo_glue.types.timestamp.serialize_aws_json_1_1(
            value["created_before"]
        )
    if "created_after" in value:
        import capo_glue.types.timestamp

        out["CreatedAfter"] = capo_glue.types.timestamp.serialize_aws_json_1_1(
            value["created_after"]
        )
    if "last_modified_before" in value:
        import capo_glue.types.timestamp

        out["LastModifiedBefore"] = capo_glue.types.timestamp.serialize_aws_json_1_1(
            value["last_modified_before"]
        )
    if "last_modified_after" in value:
        import capo_glue.types.timestamp

        out["LastModifiedAfter"] = capo_glue.types.timestamp.serialize_aws_json_1_1(
            value["last_modified_after"]
        )
    if "target_table" in value:
        import capo_glue.types.data_quality_target_table

        out["TargetTable"] = (
            capo_glue.types.data_quality_target_table.serialize_aws_json_1_1(
                value["target_table"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DataQualityRulesetFilterCriteria:
    out: DataQualityRulesetFilterCriteria = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "CreatedBefore" in data:
        import capo_glue.types.timestamp

        out["created_before"] = capo_glue.types.timestamp.deserialize_aws_json_1_1(
            data["CreatedBefore"]
        )
    if "CreatedAfter" in data:
        import capo_glue.types.timestamp

        out["created_after"] = capo_glue.types.timestamp.deserialize_aws_json_1_1(
            data["CreatedAfter"]
        )
    if "LastModifiedBefore" in data:
        import capo_glue.types.timestamp

        out["last_modified_before"] = (
            capo_glue.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedBefore"]
            )
        )
    if "LastModifiedAfter" in data:
        import capo_glue.types.timestamp

        out["last_modified_after"] = capo_glue.types.timestamp.deserialize_aws_json_1_1(
            data["LastModifiedAfter"]
        )
    if "TargetTable" in data:
        import capo_glue.types.data_quality_target_table

        out["target_table"] = (
            capo_glue.types.data_quality_target_table.deserialize_aws_json_1_1(
                data["TargetTable"]
            )
        )
    return out
