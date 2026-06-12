"""Generated from Smithy shape ``com.amazonaws.kafka#DescribeConfigurationRevisionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__long
    import aws_sdk_kafka.types.__string


class DescribeConfigurationRevisionRequest(TypedDict):
    arn: "aws_sdk_kafka.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) that uniquely identifies an MSK configuration and all of its revisions.</p>"""
    revision: "aws_sdk_kafka.types.__long.__long"
    """<p>A string that uniquely identifies a revision of an MSK configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeConfigurationRevisionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeConfigurationRevisionRequest:
    out: DescribeConfigurationRevisionRequest = {}  # type: ignore[typeddict-item]
    return out
