"""Generated from Smithy shape ``com.amazonaws.kafka#DeleteVpcConnectionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__string


class DeleteVpcConnectionRequest(TypedDict):
    arn: "aws_sdk_kafka.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) that uniquely identifies an MSK VPC connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteVpcConnectionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteVpcConnectionRequest:
    out: DeleteVpcConnectionRequest = {}  # type: ignore[typeddict-item]
    return out
