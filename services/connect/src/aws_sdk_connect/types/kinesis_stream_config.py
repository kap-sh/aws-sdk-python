"""Generated from Smithy shape ``com.amazonaws.connect#KinesisStreamConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn


class KinesisStreamConfig(TypedDict, closed=True):
    stream_arn: "aws_sdk_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the data stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KinesisStreamConfig) -> dict:
    out: dict = {}
    out["StreamArn"] = value["stream_arn"]
    return out


def deserialize_json(data: dict) -> KinesisStreamConfig:
    out: KinesisStreamConfig = {}  # type: ignore[typeddict-item]
    if "StreamArn" in data:
        out["stream_arn"] = data["StreamArn"]
    else:
        raise DeserializationError("KinesisStreamConfig.stream_arn required")
    return out
