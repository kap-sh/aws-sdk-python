"""Generated from Smithy shape ``com.amazonaws.athena#QueryRuntimeStatistics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_athena.types.query_runtime_statistics_rows
    import aws_sdk_athena.types.query_runtime_statistics_timeline
    import aws_sdk_athena.types.query_stage


class QueryRuntimeStatistics(TypedDict, closed=True):
    timeline: NotRequired[
        "aws_sdk_athena.types.query_runtime_statistics_timeline.QueryRuntimeStatisticsTimeline"
    ]
    rows: NotRequired[
        "aws_sdk_athena.types.query_runtime_statistics_rows.QueryRuntimeStatisticsRows"
    ]
    output_stage: NotRequired["aws_sdk_athena.types.query_stage.QueryStage"]
    """<p>Stage statistics such as input and output rows and bytes, execution time, and stage state. This information also includes substages and the query stage plan.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryRuntimeStatistics) -> dict:
    out: dict = {}
    if "timeline" in value:
        import aws_sdk_athena.types.query_runtime_statistics_timeline

        out["Timeline"] = (
            aws_sdk_athena.types.query_runtime_statistics_timeline.serialize_aws_json_1_1(
                value["timeline"]
            )
        )
    if "rows" in value:
        import aws_sdk_athena.types.query_runtime_statistics_rows

        out["Rows"] = (
            aws_sdk_athena.types.query_runtime_statistics_rows.serialize_aws_json_1_1(
                value["rows"]
            )
        )
    if "output_stage" in value:
        import aws_sdk_athena.types.query_stage

        out["OutputStage"] = aws_sdk_athena.types.query_stage.serialize_aws_json_1_1(
            value["output_stage"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> QueryRuntimeStatistics:
    out: QueryRuntimeStatistics = {}  # type: ignore[typeddict-item]
    if "Timeline" in data:
        import aws_sdk_athena.types.query_runtime_statistics_timeline

        out["timeline"] = (
            aws_sdk_athena.types.query_runtime_statistics_timeline.deserialize_aws_json_1_1(
                data["Timeline"]
            )
        )
    if "Rows" in data:
        import aws_sdk_athena.types.query_runtime_statistics_rows

        out["rows"] = (
            aws_sdk_athena.types.query_runtime_statistics_rows.deserialize_aws_json_1_1(
                data["Rows"]
            )
        )
    if "OutputStage" in data:
        import aws_sdk_athena.types.query_stage

        out["output_stage"] = aws_sdk_athena.types.query_stage.deserialize_aws_json_1_1(
            data["OutputStage"]
        )
    return out
