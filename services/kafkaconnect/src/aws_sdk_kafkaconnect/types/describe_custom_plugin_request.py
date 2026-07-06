"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#DescribeCustomPluginRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.__string


class DescribeCustomPluginRequest(TypedDict, closed=True):
    custom_plugin_arn: "aws_sdk_kafkaconnect.types.__string.__string"
    """<p>Returns information about a custom plugin.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeCustomPluginRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeCustomPluginRequest:
    out: DescribeCustomPluginRequest = {}  # type: ignore[typeddict-item]
    return out
