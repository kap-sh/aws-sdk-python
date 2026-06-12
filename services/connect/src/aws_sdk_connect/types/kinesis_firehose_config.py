"""Generated from Smithy shape ``com.amazonaws.connect#KinesisFirehoseConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn


class KinesisFirehoseConfig(TypedDict):
    firehose_arn: "aws_sdk_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the delivery stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KinesisFirehoseConfig) -> dict:
    out: dict = {}
    out["FirehoseArn"] = value["firehose_arn"]
    return out


def deserialize_json(data: dict) -> KinesisFirehoseConfig:
    out: KinesisFirehoseConfig = {}  # type: ignore[typeddict-item]
    if "FirehoseArn" in data:
        out["firehose_arn"] = data["FirehoseArn"]
    else:
        raise DeserializationError("KinesisFirehoseConfig.firehose_arn required")
    return out
