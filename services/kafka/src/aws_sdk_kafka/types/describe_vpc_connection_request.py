"""Generated from Smithy shape ``com.amazonaws.kafka#DescribeVpcConnectionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__string


class DescribeVpcConnectionRequest(TypedDict):
    arn: "aws_sdk_kafka.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) that uniquely identifies a MSK VPC connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeVpcConnectionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeVpcConnectionRequest:
    out: DescribeVpcConnectionRequest = {}  # type: ignore[typeddict-item]
    return out
