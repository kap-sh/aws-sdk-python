"""Generated from Smithy shape ``com.amazonaws.medialive#ListClusterAlertsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__list_of_cluster_alert
    import capo_medialive.types.__string


class ListClusterAlertsResponse(TypedDict, closed=True):
    alerts: NotRequired[
        "capo_medialive.types.__list_of_cluster_alert.__listOfClusterAlert"
    ]
    """The alerts found for this cluster"""
    next_token: NotRequired["capo_medialive.types.__string.__string"]
    """The token to use to retrieve the next page of results"""


# --- restJson1 ser/de ---
def serialize_json(value: ListClusterAlertsResponse) -> dict:
    out: dict = {}
    if "alerts" in value:
        import capo_medialive.types.__list_of_cluster_alert

        out["alerts"] = capo_medialive.types.__list_of_cluster_alert.serialize_json(
            value["alerts"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListClusterAlertsResponse:
    out: ListClusterAlertsResponse = {}  # type: ignore[typeddict-item]
    if "alerts" in data:
        import capo_medialive.types.__list_of_cluster_alert

        out["alerts"] = capo_medialive.types.__list_of_cluster_alert.deserialize_json(
            data["alerts"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
