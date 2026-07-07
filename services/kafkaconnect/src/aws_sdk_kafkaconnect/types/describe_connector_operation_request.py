"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#DescribeConnectorOperationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.__string


class DescribeConnectorOperationRequest(TypedDict, closed=True):
    connector_operation_arn: "aws_sdk_kafkaconnect.types.__string.__string"
    """<p>ARN of the connector operation to be described.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeConnectorOperationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeConnectorOperationRequest:
    out: DescribeConnectorOperationRequest = {}  # type: ignore[typeddict-item]
    return out
