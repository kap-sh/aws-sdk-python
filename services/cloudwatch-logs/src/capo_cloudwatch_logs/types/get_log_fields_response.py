"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#GetLogFieldsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.log_fields_list


class GetLogFieldsResponse(TypedDict, closed=True):
    log_fields: NotRequired["capo_cloudwatch_logs.types.log_fields_list.LogFieldsList"]
    """<p>The list of log fields for the specified data source, including field names and their data types.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetLogFieldsResponse) -> dict:
    out: dict = {}
    if "log_fields" in value:
        import capo_cloudwatch_logs.types.log_fields_list

        out["logFields"] = (
            capo_cloudwatch_logs.types.log_fields_list.serialize_aws_json_1_1(
                value["log_fields"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetLogFieldsResponse:
    out: GetLogFieldsResponse = {}  # type: ignore[typeddict-item]
    if data.get("logFields") is not None:
        import capo_cloudwatch_logs.types.log_fields_list

        out["log_fields"] = (
            capo_cloudwatch_logs.types.log_fields_list.deserialize_aws_json_1_1(
                data["logFields"]
            )
        )
    return out
