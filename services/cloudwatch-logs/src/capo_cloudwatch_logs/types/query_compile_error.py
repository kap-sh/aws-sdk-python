"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#QueryCompileError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.message
    import capo_cloudwatch_logs.types.query_compile_error_location


class QueryCompileError(TypedDict, closed=True):
    location: NotRequired[
        "capo_cloudwatch_logs.types.query_compile_error_location.QueryCompileErrorLocation"
    ]
    """<p>Reserved.</p>"""
    message: NotRequired["capo_cloudwatch_logs.types.message.Message"]
    """<p>Reserved.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryCompileError) -> dict:
    out: dict = {}
    if "location" in value:
        import capo_cloudwatch_logs.types.query_compile_error_location

        out["location"] = (
            capo_cloudwatch_logs.types.query_compile_error_location.serialize_aws_json_1_1(
                value["location"]
            )
        )
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> QueryCompileError:
    out: QueryCompileError = {}  # type: ignore[typeddict-item]
    if "location" in data:
        import capo_cloudwatch_logs.types.query_compile_error_location

        out["location"] = (
            capo_cloudwatch_logs.types.query_compile_error_location.deserialize_aws_json_1_1(
                data["location"]
            )
        )
    if "message" in data:
        out["message"] = data["message"]
    return out
