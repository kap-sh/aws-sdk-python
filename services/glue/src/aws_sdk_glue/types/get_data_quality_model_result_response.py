"""Generated from Smithy shape ``com.amazonaws.glue#GetDataQualityModelResultResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.statistic_model_results
    import aws_sdk_glue.types.timestamp


class GetDataQualityModelResultResponse(TypedDict, closed=True):
    completed_on: NotRequired["aws_sdk_glue.types.timestamp.Timestamp"]
    """<p>The timestamp when the data quality model training completed.</p>"""
    model: NotRequired[
        "aws_sdk_glue.types.statistic_model_results.StatisticModelResults"
    ]
    """<p>A list of <code>StatisticModelResult</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDataQualityModelResultResponse) -> dict:
    out: dict = {}
    if "completed_on" in value:
        import aws_sdk_glue.types.timestamp

        out["CompletedOn"] = aws_sdk_glue.types.timestamp.serialize_aws_json_1_1(
            value["completed_on"]
        )
    if "model" in value:
        import aws_sdk_glue.types.statistic_model_results

        out["Model"] = (
            aws_sdk_glue.types.statistic_model_results.serialize_aws_json_1_1(
                value["model"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDataQualityModelResultResponse:
    out: GetDataQualityModelResultResponse = {}  # type: ignore[typeddict-item]
    if "CompletedOn" in data:
        import aws_sdk_glue.types.timestamp

        out["completed_on"] = aws_sdk_glue.types.timestamp.deserialize_aws_json_1_1(
            data["CompletedOn"]
        )
    if "Model" in data:
        import aws_sdk_glue.types.statistic_model_results

        out["model"] = (
            aws_sdk_glue.types.statistic_model_results.deserialize_aws_json_1_1(
                data["Model"]
            )
        )
    return out
