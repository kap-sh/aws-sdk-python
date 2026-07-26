"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#KinesisFirehoseInputUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.resource_arn


class KinesisFirehoseInputUpdate(TypedDict, closed=True):
    resource_arn_update: "capo_kinesis_analytics_v2.types.resource_arn.ResourceARN"
    """<p>The Amazon Resource Name (ARN) of the input delivery stream to read.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KinesisFirehoseInputUpdate) -> dict:
    out: dict = {}
    out["ResourceARNUpdate"] = value["resource_arn_update"]
    return out


def deserialize_aws_json_1_1(data: dict) -> KinesisFirehoseInputUpdate:
    out: KinesisFirehoseInputUpdate = {}  # type: ignore[typeddict-item]
    if "ResourceARNUpdate" in data:
        out["resource_arn_update"] = data["ResourceARNUpdate"]
    else:
        raise DeserializationError(
            "KinesisFirehoseInputUpdate.resource_arn_update required"
        )
    return out
