"""Generated from Smithy shape ``com.amazonaws.mq#DescribeConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_mq.types.__string


class DescribeConfigurationRequest(TypedDict, closed=True):
    configuration_id: "aws_sdk_mq.types.__string.__string"
    """<p>The unique ID that Amazon MQ generates for the configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeConfigurationRequest:
    out: DescribeConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
