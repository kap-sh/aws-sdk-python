"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#GetLogFieldsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.log_fields_list


class GetLogFieldsResponse(TypedDict):
    log_fields: NotRequired[
        "aws_sdk_cloudwatch_logs.types.log_fields_list.LogFieldsList"
    ]
    """<p>The list of log fields for the specified data source, including field names and their data types.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetLogFieldsResponse) -> dict:
    out: dict = {}
    if "log_fields" in value:
        import aws_sdk_cloudwatch_logs.types.log_fields_list

        out["logFields"] = (
            aws_sdk_cloudwatch_logs.types.log_fields_list.serialize_aws_json_1_1(
                value["log_fields"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetLogFieldsResponse:
    out: GetLogFieldsResponse = {}  # type: ignore[typeddict-item]
    if "logFields" in data:
        import aws_sdk_cloudwatch_logs.types.log_fields_list

        out["log_fields"] = (
            aws_sdk_cloudwatch_logs.types.log_fields_list.deserialize_aws_json_1_1(
                data["logFields"]
            )
        )
    return out
