"""Generated from Smithy shape ``com.amazonaws.kafka#DescribeVpcConnectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__string


class DescribeVpcConnectionRequest(TypedDict, closed=True):
    arn: "aws_sdk_kafka.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) that uniquely identifies a MSK VPC connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeVpcConnectionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeVpcConnectionRequest:
    out: DescribeVpcConnectionRequest = {}  # type: ignore[typeddict-item]
    return out
