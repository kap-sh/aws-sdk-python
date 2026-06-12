"""Generated from Smithy shape ``com.amazonaws.glue#GetDataQualityModelRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.hash_string


class GetDataQualityModelRequest(TypedDict):
    statistic_id: NotRequired["aws_sdk_glue.types.hash_string.HashString"]
    """<p>The Statistic ID.</p>"""
    profile_id: "aws_sdk_glue.types.hash_string.HashString"
    """<p>The Profile ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDataQualityModelRequest) -> dict:
    out: dict = {}
    if "statistic_id" in value:
        out["StatisticId"] = value["statistic_id"]
    out["ProfileId"] = value["profile_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDataQualityModelRequest:
    out: GetDataQualityModelRequest = {}  # type: ignore[typeddict-item]
    if "StatisticId" in data:
        out["statistic_id"] = data["StatisticId"]
    if "ProfileId" in data:
        out["profile_id"] = data["ProfileId"]
    else:
        raise DeserializationError("GetDataQualityModelRequest.profile_id required")
    return out
