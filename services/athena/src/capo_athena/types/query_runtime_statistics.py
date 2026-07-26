"""Generated from Smithy shape ``com.amazonaws.athena#QueryRuntimeStatistics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.query_runtime_statistics_rows
    import capo_athena.types.query_runtime_statistics_timeline
    import capo_athena.types.query_stage


class QueryRuntimeStatistics(TypedDict, closed=True):
    timeline: NotRequired[
        "capo_athena.types.query_runtime_statistics_timeline.QueryRuntimeStatisticsTimeline"
    ]
    rows: NotRequired[
        "capo_athena.types.query_runtime_statistics_rows.QueryRuntimeStatisticsRows"
    ]
    output_stage: NotRequired["capo_athena.types.query_stage.QueryStage"]
    """<p>Stage statistics such as input and output rows and bytes, execution time, and stage state. This information also includes substages and the query stage plan.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryRuntimeStatistics) -> dict:
    out: dict = {}
    if "timeline" in value:
        import capo_athena.types.query_runtime_statistics_timeline

        out["Timeline"] = (
            capo_athena.types.query_runtime_statistics_timeline.serialize_aws_json_1_1(
                value["timeline"]
            )
        )
    if "rows" in value:
        import capo_athena.types.query_runtime_statistics_rows

        out["Rows"] = (
            capo_athena.types.query_runtime_statistics_rows.serialize_aws_json_1_1(
                value["rows"]
            )
        )
    if "output_stage" in value:
        import capo_athena.types.query_stage

        out["OutputStage"] = capo_athena.types.query_stage.serialize_aws_json_1_1(
            value["output_stage"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> QueryRuntimeStatistics:
    out: QueryRuntimeStatistics = {}  # type: ignore[typeddict-item]
    if "Timeline" in data:
        import capo_athena.types.query_runtime_statistics_timeline

        out["timeline"] = (
            capo_athena.types.query_runtime_statistics_timeline.deserialize_aws_json_1_1(
                data["Timeline"]
            )
        )
    if "Rows" in data:
        import capo_athena.types.query_runtime_statistics_rows

        out["rows"] = (
            capo_athena.types.query_runtime_statistics_rows.deserialize_aws_json_1_1(
                data["Rows"]
            )
        )
    if "OutputStage" in data:
        import capo_athena.types.query_stage

        out["output_stage"] = capo_athena.types.query_stage.deserialize_aws_json_1_1(
            data["OutputStage"]
        )
    return out
