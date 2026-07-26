"""Generated from Smithy shape ``com.amazonaws.kafka#GetCompatibleKafkaVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__string


class GetCompatibleKafkaVersionsRequest(TypedDict, closed=True):
    cluster_arn: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the cluster check.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCompatibleKafkaVersionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCompatibleKafkaVersionsRequest:
    out: GetCompatibleKafkaVersionsRequest = {}  # type: ignore[typeddict-item]
    return out
