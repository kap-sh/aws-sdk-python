"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#ListConnectorsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafkaconnect.types.__list_of_connector_summary
    import capo_kafkaconnect.types.__string


class ListConnectorsResponse(TypedDict, closed=True):
    connectors: NotRequired[
        "capo_kafkaconnect.types.__list_of_connector_summary.__listOfConnectorSummary"
    ]
    """<p>An array of connector descriptions.</p>"""
    next_token: NotRequired["capo_kafkaconnect.types.__string.__string"]
    """<p>If the response of a ListConnectors operation is truncated, it will include a NextToken. Send this NextToken in a subsequent request to continue listing from where it left off.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConnectorsResponse) -> dict:
    out: dict = {}
    if "connectors" in value:
        import capo_kafkaconnect.types.__list_of_connector_summary

        out["connectors"] = (
            capo_kafkaconnect.types.__list_of_connector_summary.serialize_json(
                value["connectors"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListConnectorsResponse:
    out: ListConnectorsResponse = {}  # type: ignore[typeddict-item]
    if "connectors" in data:
        import capo_kafkaconnect.types.__list_of_connector_summary

        out["connectors"] = (
            capo_kafkaconnect.types.__list_of_connector_summary.deserialize_json(
                data["connectors"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
