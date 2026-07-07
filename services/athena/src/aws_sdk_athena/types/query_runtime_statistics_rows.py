"""Generated from Smithy shape ``com.amazonaws.athena#QueryRuntimeStatisticsRows``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_athena.types.long


class QueryRuntimeStatisticsRows(TypedDict, closed=True):
    input_rows: NotRequired["aws_sdk_athena.types.long.Long"]
    """<p>The number of rows read to execute the query.</p>"""
    input_bytes: NotRequired["aws_sdk_athena.types.long.Long"]
    """<p>The number of bytes read to execute the query.</p>"""
    output_bytes: NotRequired["aws_sdk_athena.types.long.Long"]
    """<p>The number of bytes returned by the query.</p>"""
    output_rows: NotRequired["aws_sdk_athena.types.long.Long"]
    """<p>The number of rows returned by the query.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryRuntimeStatisticsRows) -> dict:
    out: dict = {}
    if "input_rows" in value:
        out["InputRows"] = value["input_rows"]
    if "input_bytes" in value:
        out["InputBytes"] = value["input_bytes"]
    if "output_bytes" in value:
        out["OutputBytes"] = value["output_bytes"]
    if "output_rows" in value:
        out["OutputRows"] = value["output_rows"]
    return out


def deserialize_aws_json_1_1(data: dict) -> QueryRuntimeStatisticsRows:
    out: QueryRuntimeStatisticsRows = {}  # type: ignore[typeddict-item]
    if "InputRows" in data:
        out["input_rows"] = data["InputRows"]
    if "InputBytes" in data:
        out["input_bytes"] = data["InputBytes"]
    if "OutputBytes" in data:
        out["output_bytes"] = data["OutputBytes"]
    if "OutputRows" in data:
        out["output_rows"] = data["OutputRows"]
    return out
