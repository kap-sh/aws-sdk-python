"""Generated from Smithy shape ``com.amazonaws.kafka#GetCompatibleKafkaVersionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__string


class GetCompatibleKafkaVersionsRequest(TypedDict):
    cluster_arn: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the cluster check.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCompatibleKafkaVersionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCompatibleKafkaVersionsRequest:
    out: GetCompatibleKafkaVersionsRequest = {}  # type: ignore[typeddict-item]
    return out
