"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#GetLogGroupFieldsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.log_group_field_list


class GetLogGroupFieldsResponse(TypedDict):
    log_group_fields: NotRequired[
        "aws_sdk_cloudwatch_logs.types.log_group_field_list.LogGroupFieldList"
    ]
    """<p>The array of fields found in the query. Each object in the array contains the name of the field, along with the percentage of time it appeared in the log events that were queried.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetLogGroupFieldsResponse) -> dict:
    out: dict = {}
    if "log_group_fields" in value:
        import aws_sdk_cloudwatch_logs.types.log_group_field_list

        out["logGroupFields"] = (
            aws_sdk_cloudwatch_logs.types.log_group_field_list.serialize_aws_json_1_1(
                value["log_group_fields"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetLogGroupFieldsResponse:
    out: GetLogGroupFieldsResponse = {}  # type: ignore[typeddict-item]
    if "logGroupFields" in data:
        import aws_sdk_cloudwatch_logs.types.log_group_field_list

        out["log_group_fields"] = (
            aws_sdk_cloudwatch_logs.types.log_group_field_list.deserialize_aws_json_1_1(
                data["logGroupFields"]
            )
        )
    return out
