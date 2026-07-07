"""Generated from Smithy shape ``com.amazonaws.kafka#DescribeConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__string


class DescribeConfigurationRequest(TypedDict, closed=True):
    arn: "aws_sdk_kafka.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) that uniquely identifies an MSK configuration and all of its revisions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeConfigurationRequest:
    out: DescribeConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
