"""Generated from Smithy shape ``com.amazonaws.kafka#GetBootstrapBrokersRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__string


class GetBootstrapBrokersRequest(TypedDict):
    cluster_arn: "aws_sdk_kafka.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBootstrapBrokersRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetBootstrapBrokersRequest:
    out: GetBootstrapBrokersRequest = {}  # type: ignore[typeddict-item]
    return out
