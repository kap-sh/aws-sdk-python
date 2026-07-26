"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#ListConnectorOperationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafkaconnect.types.__list_of_connector_operation_summary
    import capo_kafkaconnect.types.__string


class ListConnectorOperationsResponse(TypedDict, closed=True):
    connector_operations: NotRequired[
        "capo_kafkaconnect.types.__list_of_connector_operation_summary.__listOfConnectorOperationSummary"
    ]
    """<p>An array of connector operation descriptions.</p>"""
    next_token: NotRequired["capo_kafkaconnect.types.__string.__string"]
    """<p>If the response is truncated, it includes a NextToken. Send this NextToken in a subsequent request to continue listing from where it left off.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConnectorOperationsResponse) -> dict:
    out: dict = {}
    if "connector_operations" in value:
        import capo_kafkaconnect.types.__list_of_connector_operation_summary

        out["connectorOperations"] = (
            capo_kafkaconnect.types.__list_of_connector_operation_summary.serialize_json(
                value["connector_operations"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListConnectorOperationsResponse:
    out: ListConnectorOperationsResponse = {}  # type: ignore[typeddict-item]
    if "connectorOperations" in data:
        import capo_kafkaconnect.types.__list_of_connector_operation_summary

        out["connector_operations"] = (
            capo_kafkaconnect.types.__list_of_connector_operation_summary.deserialize_json(
                data["connectorOperations"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
