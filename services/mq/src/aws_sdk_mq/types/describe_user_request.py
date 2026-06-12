"""Generated from Smithy shape ``com.amazonaws.mq#DescribeUserRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mq.types.__string


class DescribeUserRequest(TypedDict):
    broker_id: "aws_sdk_mq.types.__string.__string"
    """<p>The unique ID that Amazon MQ generates for the broker.</p>"""
    username: "aws_sdk_mq.types.__string.__string"
    """<p>The username of the ActiveMQ user. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 2-100 characters long.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeUserRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeUserRequest:
    out: DescribeUserRequest = {}  # type: ignore[typeddict-item]
    return out
