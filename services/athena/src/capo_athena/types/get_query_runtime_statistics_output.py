"""Generated from Smithy shape ``com.amazonaws.athena#GetQueryRuntimeStatisticsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.query_runtime_statistics


class GetQueryRuntimeStatisticsOutput(TypedDict, closed=True):
    query_runtime_statistics: NotRequired[
        "capo_athena.types.query_runtime_statistics.QueryRuntimeStatistics"
    ]
    """<p>Runtime statistics about the query execution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetQueryRuntimeStatisticsOutput) -> dict:
    out: dict = {}
    if "query_runtime_statistics" in value:
        import capo_athena.types.query_runtime_statistics

        out["QueryRuntimeStatistics"] = (
            capo_athena.types.query_runtime_statistics.serialize_aws_json_1_1(
                value["query_runtime_statistics"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetQueryRuntimeStatisticsOutput:
    out: GetQueryRuntimeStatisticsOutput = {}  # type: ignore[typeddict-item]
    if "QueryRuntimeStatistics" in data:
        import capo_athena.types.query_runtime_statistics

        out["query_runtime_statistics"] = (
            capo_athena.types.query_runtime_statistics.deserialize_aws_json_1_1(
                data["QueryRuntimeStatistics"]
            )
        )
    return out
