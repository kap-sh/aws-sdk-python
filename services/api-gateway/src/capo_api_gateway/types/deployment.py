"""Generated from Smithy shape ``com.amazonaws.apigateway#Deployment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.path_to_map_of_method_snapshot
    import capo_api_gateway.types.string
    import capo_api_gateway.types.timestamp


class Deployment(TypedDict, closed=True):
    id: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The identifier for the deployment resource.</p>"""
    description: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The description for the deployment resource.</p>"""
    created_date: NotRequired["capo_api_gateway.types.timestamp.Timestamp"]
    """<p>The date and time that the deployment resource was created.</p>"""
    api_summary: NotRequired[
        "capo_api_gateway.types.path_to_map_of_method_snapshot.PathToMapOfMethodSnapshot"
    ]
    """<p>A summary of the RestApi at the date and time that the deployment resource was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Deployment) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "description" in value:
        out["description"] = value["description"]
    if "created_date" in value:
        import capo_api_gateway.types.timestamp

        out["createdDate"] = capo_api_gateway.types.timestamp.serialize_json(
            value["created_date"]
        )
    if "api_summary" in value:
        import capo_api_gateway.types.path_to_map_of_method_snapshot

        out["apiSummary"] = (
            capo_api_gateway.types.path_to_map_of_method_snapshot.serialize_json(
                value["api_summary"]
            )
        )
    return out


def deserialize_json(data: dict) -> Deployment:
    out: Deployment = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "description" in data:
        out["description"] = data["description"]
    if "createdDate" in data:
        import capo_api_gateway.types.timestamp

        out["created_date"] = capo_api_gateway.types.timestamp.deserialize_json(
            data["createdDate"]
        )
    if "apiSummary" in data:
        import capo_api_gateway.types.path_to_map_of_method_snapshot

        out["api_summary"] = (
            capo_api_gateway.types.path_to_map_of_method_snapshot.deserialize_json(
                data["apiSummary"]
            )
        )
    return out
