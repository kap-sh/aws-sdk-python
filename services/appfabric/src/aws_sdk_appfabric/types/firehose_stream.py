"""Generated from Smithy shape ``com.amazonaws.appfabric#FirehoseStream``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_appfabric.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appfabric.types.string64


class FirehoseStream(TypedDict, closed=True):
    stream_name: "aws_sdk_appfabric.types.string64.String64"
    """<p>The name of the Amazon Kinesis Data Firehose delivery stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FirehoseStream) -> dict:
    out: dict = {}
    out["streamName"] = value["stream_name"]
    return out


def deserialize_json(data: dict) -> FirehoseStream:
    out: FirehoseStream = {}  # type: ignore[typeddict-item]
    if "streamName" in data:
        out["stream_name"] = data["streamName"]
    else:
        raise DeserializationError("FirehoseStream.stream_name required")
    return out
