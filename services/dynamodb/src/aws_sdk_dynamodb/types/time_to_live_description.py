"""Generated from Smithy shape ``com.amazonaws.dynamodb#TimeToLiveDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.time_to_live_attribute_name
    import aws_sdk_dynamodb.types.time_to_live_status


class TimeToLiveDescription(TypedDict):
    time_to_live_status: NotRequired[
        "aws_sdk_dynamodb.types.time_to_live_status.TimeToLiveStatus"
    ]
    """<p> The TTL status for the table.</p>"""
    attribute_name: NotRequired[
        "aws_sdk_dynamodb.types.time_to_live_attribute_name.TimeToLiveAttributeName"
    ]
    """<p> The name of the TTL attribute for items in the table.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TimeToLiveDescription) -> dict:
    out: dict = {}
    if "time_to_live_status" in value:
        import aws_sdk_dynamodb.types.time_to_live_status

        out["TimeToLiveStatus"] = (
            aws_sdk_dynamodb.types.time_to_live_status.serialize_aws_json_1_0(
                value["time_to_live_status"]
            )
        )
    if "attribute_name" in value:
        out["AttributeName"] = value["attribute_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TimeToLiveDescription:
    out: TimeToLiveDescription = {}  # type: ignore[typeddict-item]
    if "TimeToLiveStatus" in data:
        import aws_sdk_dynamodb.types.time_to_live_status

        out["time_to_live_status"] = (
            aws_sdk_dynamodb.types.time_to_live_status.deserialize_aws_json_1_0(
                data["TimeToLiveStatus"]
            )
        )
    if "AttributeName" in data:
        out["attribute_name"] = data["AttributeName"]
    return out
