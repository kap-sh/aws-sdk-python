"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#DescribeConnectorRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.__string


class DescribeConnectorRequest(TypedDict):
    connector_arn: "aws_sdk_kafkaconnect.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the connector that you want to describe.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeConnectorRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeConnectorRequest:
    out: DescribeConnectorRequest = {}  # type: ignore[typeddict-item]
    return out
