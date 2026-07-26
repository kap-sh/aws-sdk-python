"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#ListConnectorOperationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafkaconnect.types.__string
    import capo_kafkaconnect.types.max_results


class ListConnectorOperationsRequest(TypedDict, closed=True):
    connector_arn: "capo_kafkaconnect.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the connector for which to list operations.</p>"""
    max_results: NotRequired["capo_kafkaconnect.types.max_results.MaxResults"]
    """<p>Maximum number of connector operations to fetch in one get request.</p>"""
    next_token: NotRequired["capo_kafkaconnect.types.__string.__string"]
    """<p>If the response is truncated, it includes a NextToken. Send this NextToken in a subsequent request to continue listing from where it left off.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConnectorOperationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListConnectorOperationsRequest:
    out: ListConnectorOperationsRequest = {}  # type: ignore[typeddict-item]
    return out
