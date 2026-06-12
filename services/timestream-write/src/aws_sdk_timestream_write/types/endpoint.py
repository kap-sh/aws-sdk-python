"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#Endpoint``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_timestream_write.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_timestream_write.types.long
    import aws_sdk_timestream_write.types.string


class Endpoint(TypedDict):
    address: "aws_sdk_timestream_write.types.string.String"
    """<p>An endpoint address.</p>"""
    cache_period_in_minutes: "aws_sdk_timestream_write.types.long.Long"
    """<p>The TTL for the endpoint, in minutes.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Endpoint) -> dict:
    out: dict = {}
    out["Address"] = value["address"]
    out["CachePeriodInMinutes"] = value.get("cache_period_in_minutes", 0)
    return out


def deserialize_aws_json_1_0(data: dict) -> Endpoint:
    out: Endpoint = {}  # type: ignore[typeddict-item]
    if "Address" in data:
        out["address"] = data["Address"]
    else:
        raise DeserializationError("Endpoint.address required")
    if "CachePeriodInMinutes" in data:
        out["cache_period_in_minutes"] = data["CachePeriodInMinutes"]
    else:
        out["cache_period_in_minutes"] = 0
    return out
