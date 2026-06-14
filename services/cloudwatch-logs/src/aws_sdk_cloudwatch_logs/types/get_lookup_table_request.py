"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#GetLookupTableRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.arn


class GetLookupTableRequest(TypedDict):
    lookup_table_arn: "aws_sdk_cloudwatch_logs.types.arn.Arn"
    """<p>The ARN of the lookup table to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetLookupTableRequest) -> dict:
    out: dict = {}
    out["lookupTableArn"] = value["lookup_table_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetLookupTableRequest:
    out: GetLookupTableRequest = {}  # type: ignore[typeddict-item]
    if "lookupTableArn" in data:
        out["lookup_table_arn"] = data["lookupTableArn"]
    else:
        raise DeserializationError("GetLookupTableRequest.lookup_table_arn required")
    return out
