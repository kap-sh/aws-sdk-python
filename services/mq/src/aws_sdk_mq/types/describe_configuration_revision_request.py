"""Generated from Smithy shape ``com.amazonaws.mq#DescribeConfigurationRevisionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_mq.types.__string


class DescribeConfigurationRevisionRequest(TypedDict, closed=True):
    configuration_id: "aws_sdk_mq.types.__string.__string"
    """<p>The unique ID that Amazon MQ generates for the configuration.</p>"""
    configuration_revision: "aws_sdk_mq.types.__string.__string"
    """<p>The revision of the configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeConfigurationRevisionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeConfigurationRevisionRequest:
    out: DescribeConfigurationRevisionRequest = {}  # type: ignore[typeddict-item]
    return out
