"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityRuleRecommendationRunFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.data_source
    import capo_glue.types.timestamp


class DataQualityRuleRecommendationRunFilter(TypedDict, closed=True):
    data_source: "capo_glue.types.data_source.DataSource"
    """<p>Filter based on a specified data source (Glue table).</p>"""
    started_before: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>Filter based on time for results started before provided time.</p>"""
    started_after: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>Filter based on time for results started after provided time.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityRuleRecommendationRunFilter) -> dict:
    out: dict = {}
    import capo_glue.types.data_source

    out["DataSource"] = capo_glue.types.data_source.serialize_aws_json_1_1(
        value["data_source"]
    )
    if "started_before" in value:
        import capo_glue.types.timestamp

        out["StartedBefore"] = capo_glue.types.timestamp.serialize_aws_json_1_1(
            value["started_before"]
        )
    if "started_after" in value:
        import capo_glue.types.timestamp

        out["StartedAfter"] = capo_glue.types.timestamp.serialize_aws_json_1_1(
            value["started_after"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DataQualityRuleRecommendationRunFilter:
    out: DataQualityRuleRecommendationRunFilter = {}  # type: ignore[typeddict-item]
    if "DataSource" in data:
        import capo_glue.types.data_source

        out["data_source"] = capo_glue.types.data_source.deserialize_aws_json_1_1(
            data["DataSource"]
        )
    else:
        raise DeserializationError(
            "DataQualityRuleRecommendationRunFilter.data_source required"
        )
    if "StartedBefore" in data:
        import capo_glue.types.timestamp

        out["started_before"] = capo_glue.types.timestamp.deserialize_aws_json_1_1(
            data["StartedBefore"]
        )
    if "StartedAfter" in data:
        import capo_glue.types.timestamp

        out["started_after"] = capo_glue.types.timestamp.deserialize_aws_json_1_1(
            data["StartedAfter"]
        )
    return out
