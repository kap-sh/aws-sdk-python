"""Generated from Smithy shape ``com.amazonaws.glue#GetDataQualityResultRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.hash_string


class GetDataQualityResultRequest(TypedDict):
    result_id: "aws_sdk_glue.types.hash_string.HashString"
    """<p>A unique result ID for the data quality result.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDataQualityResultRequest) -> dict:
    out: dict = {}
    out["ResultId"] = value["result_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDataQualityResultRequest:
    out: GetDataQualityResultRequest = {}  # type: ignore[typeddict-item]
    if "ResultId" in data:
        out["result_id"] = data["ResultId"]
    else:
        raise DeserializationError("GetDataQualityResultRequest.result_id required")
    return out
