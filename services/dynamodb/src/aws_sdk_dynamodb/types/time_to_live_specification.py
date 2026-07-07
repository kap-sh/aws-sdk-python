"""Generated from Smithy shape ``com.amazonaws.dynamodb#TimeToLiveSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.time_to_live_attribute_name
    import aws_sdk_dynamodb.types.time_to_live_enabled


class TimeToLiveSpecification(TypedDict, closed=True):
    enabled: "aws_sdk_dynamodb.types.time_to_live_enabled.TimeToLiveEnabled"
    """<p>Indicates whether TTL is to be enabled (true) or disabled (false) on the table.</p>"""
    attribute_name: (
        "aws_sdk_dynamodb.types.time_to_live_attribute_name.TimeToLiveAttributeName"
    )
    """<p>The name of the TTL attribute used to store the expiration time for items in the table.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TimeToLiveSpecification) -> dict:
    out: dict = {}
    out["Enabled"] = value["enabled"]
    out["AttributeName"] = value["attribute_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TimeToLiveSpecification:
    out: TimeToLiveSpecification = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    else:
        raise DeserializationError("TimeToLiveSpecification.enabled required")
    if "AttributeName" in data:
        out["attribute_name"] = data["AttributeName"]
    else:
        raise DeserializationError("TimeToLiveSpecification.attribute_name required")
    return out
