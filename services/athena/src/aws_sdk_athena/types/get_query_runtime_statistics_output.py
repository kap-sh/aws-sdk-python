"""Generated from Smithy shape ``com.amazonaws.athena#GetQueryRuntimeStatisticsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_athena.types.query_runtime_statistics


class GetQueryRuntimeStatisticsOutput(TypedDict):
    query_runtime_statistics: NotRequired[
        "aws_sdk_athena.types.query_runtime_statistics.QueryRuntimeStatistics"
    ]
    """<p>Runtime statistics about the query execution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetQueryRuntimeStatisticsOutput) -> dict:
    out: dict = {}
    if "query_runtime_statistics" in value:
        import aws_sdk_athena.types.query_runtime_statistics

        out["QueryRuntimeStatistics"] = (
            aws_sdk_athena.types.query_runtime_statistics.serialize_aws_json_1_1(
                value["query_runtime_statistics"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetQueryRuntimeStatisticsOutput:
    out: GetQueryRuntimeStatisticsOutput = {}  # type: ignore[typeddict-item]
    if "QueryRuntimeStatistics" in data:
        import aws_sdk_athena.types.query_runtime_statistics

        out["query_runtime_statistics"] = (
            aws_sdk_athena.types.query_runtime_statistics.deserialize_aws_json_1_1(
                data["QueryRuntimeStatistics"]
            )
        )
    return out
