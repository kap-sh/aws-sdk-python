"""Generated from Smithy shape ``com.amazonaws.appflow#ListConnectorEntitiesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appflow.types.connector_entity_map
    import aws_sdk_appflow.types.next_token


class ListConnectorEntitiesResponse(TypedDict, closed=True):
    connector_entity_map: (
        "aws_sdk_appflow.types.connector_entity_map.ConnectorEntityMap"
    )
    """<p> The response of <code>ListConnectorEntities</code> lists entities grouped by category. This map's key represents the group name, and its value contains the list of entities belonging to that group. </p>"""
    next_token: NotRequired["aws_sdk_appflow.types.next_token.NextToken"]
    """<p>A token that you specify in your next <code>ListConnectorEntities</code> operation to get the next page of results in paginated response. The <code>ListConnectorEntities</code> operation provides this token if the response is too big for the page size.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConnectorEntitiesResponse) -> dict:
    out: dict = {}
    import aws_sdk_appflow.types.connector_entity_map

    out["connectorEntityMap"] = (
        aws_sdk_appflow.types.connector_entity_map.serialize_json(
            value["connector_entity_map"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListConnectorEntitiesResponse:
    out: ListConnectorEntitiesResponse = {}  # type: ignore[typeddict-item]
    if "connectorEntityMap" in data:
        import aws_sdk_appflow.types.connector_entity_map

        out["connector_entity_map"] = (
            aws_sdk_appflow.types.connector_entity_map.deserialize_json(
                data["connectorEntityMap"]
            )
        )
    else:
        raise DeserializationError(
            "ListConnectorEntitiesResponse.connector_entity_map required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
