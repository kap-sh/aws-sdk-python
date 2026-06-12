"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#ListConnectorOperationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.__string
    import aws_sdk_kafkaconnect.types.max_results


class ListConnectorOperationsRequest(TypedDict):
    connector_arn: "aws_sdk_kafkaconnect.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the connector for which to list operations.</p>"""
    max_results: NotRequired["aws_sdk_kafkaconnect.types.max_results.MaxResults"]
    """<p>Maximum number of connector operations to fetch in one get request.</p>"""
    next_token: NotRequired["aws_sdk_kafkaconnect.types.__string.__string"]
    """<p>If the response is truncated, it includes a NextToken. Send this NextToken in a subsequent request to continue listing from where it left off.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConnectorOperationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListConnectorOperationsRequest:
    out: ListConnectorOperationsRequest = {}  # type: ignore[typeddict-item]
    return out
