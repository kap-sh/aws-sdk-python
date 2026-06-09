"""Generated from Smithy shape ``com.amazonaws.dynamodb#Endpoint``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.long
    import aws_sdk_dynamodb.types.string


class Endpoint(TypedDict):
    address: "aws_sdk_dynamodb.types.string.String"
    """<p>IP address of the endpoint.</p>"""
    cache_period_in_minutes: "aws_sdk_dynamodb.types.long.Long"
    """<p>Endpoint cache time to live (TTL) value.</p>"""


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
