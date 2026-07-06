"""Generated from Smithy shape ``com.amazonaws.glue#GetDataQualityModelResultRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.hash_string


class GetDataQualityModelResultRequest(TypedDict, closed=True):
    statistic_id: "aws_sdk_glue.types.hash_string.HashString"
    """<p>The Statistic ID.</p>"""
    profile_id: "aws_sdk_glue.types.hash_string.HashString"
    """<p>The Profile ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDataQualityModelResultRequest) -> dict:
    out: dict = {}
    out["StatisticId"] = value["statistic_id"]
    out["ProfileId"] = value["profile_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDataQualityModelResultRequest:
    out: GetDataQualityModelResultRequest = {}  # type: ignore[typeddict-item]
    if "StatisticId" in data:
        out["statistic_id"] = data["StatisticId"]
    else:
        raise DeserializationError(
            "GetDataQualityModelResultRequest.statistic_id required"
        )
    if "ProfileId" in data:
        out["profile_id"] = data["ProfileId"]
    else:
        raise DeserializationError(
            "GetDataQualityModelResultRequest.profile_id required"
        )
    return out
