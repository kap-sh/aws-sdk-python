"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityRulesetEvaluationRunFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.data_source
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.timestamp


class DataQualityRulesetEvaluationRunFilter(TypedDict):
    data_source: "aws_sdk_glue.types.data_source.DataSource"
    """<p>Filter based on a data source (an Glue table) associated with the run.</p>"""
    started_before: NotRequired["aws_sdk_glue.types.timestamp.Timestamp"]
    """<p>Filter results by runs that started before this time.</p>"""
    started_after: NotRequired["aws_sdk_glue.types.timestamp.Timestamp"]
    """<p>Filter results by runs that started after this time.</p>"""
    ruleset_name: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>Filter results by the name of the ruleset.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityRulesetEvaluationRunFilter) -> dict:
    out: dict = {}
    import aws_sdk_glue.types.data_source

    out["DataSource"] = aws_sdk_glue.types.data_source.serialize_aws_json_1_1(
        value["data_source"]
    )
    if "started_before" in value:
        import aws_sdk_glue.types.timestamp

        out["StartedBefore"] = aws_sdk_glue.types.timestamp.serialize_aws_json_1_1(
            value["started_before"]
        )
    if "started_after" in value:
        import aws_sdk_glue.types.timestamp

        out["StartedAfter"] = aws_sdk_glue.types.timestamp.serialize_aws_json_1_1(
            value["started_after"]
        )
    if "ruleset_name" in value:
        out["RulesetName"] = value["ruleset_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DataQualityRulesetEvaluationRunFilter:
    out: DataQualityRulesetEvaluationRunFilter = {}  # type: ignore[typeddict-item]
    if "DataSource" in data:
        import aws_sdk_glue.types.data_source

        out["data_source"] = aws_sdk_glue.types.data_source.deserialize_aws_json_1_1(
            data["DataSource"]
        )
    else:
        raise DeserializationError(
            "DataQualityRulesetEvaluationRunFilter.data_source required"
        )
    if "StartedBefore" in data:
        import aws_sdk_glue.types.timestamp

        out["started_before"] = aws_sdk_glue.types.timestamp.deserialize_aws_json_1_1(
            data["StartedBefore"]
        )
    if "StartedAfter" in data:
        import aws_sdk_glue.types.timestamp

        out["started_after"] = aws_sdk_glue.types.timestamp.deserialize_aws_json_1_1(
            data["StartedAfter"]
        )
    if "RulesetName" in data:
        out["ruleset_name"] = data["RulesetName"]
    return out
