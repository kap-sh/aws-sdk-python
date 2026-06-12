"""Generated from Smithy shape ``com.amazonaws.emr#ListClustersInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.cluster_state_list
    import aws_sdk_emr.types.date
    import aws_sdk_emr.types.marker


class ListClustersInput(TypedDict):
    created_after: NotRequired["aws_sdk_emr.types.date.Date"]
    """<p>The creation date and time beginning value filter for listing clusters.</p>"""
    created_before: NotRequired["aws_sdk_emr.types.date.Date"]
    """<p>The creation date and time end value filter for listing clusters.</p>"""
    cluster_states: NotRequired["aws_sdk_emr.types.cluster_state_list.ClusterStateList"]
    """<p>The cluster state filters to apply when listing clusters. Clusters that change state while this action runs may be not be returned as expected in the list of clusters.</p>"""
    marker: NotRequired["aws_sdk_emr.types.marker.Marker"]
    """<p>The pagination token that indicates the next set of results to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListClustersInput) -> dict:
    out: dict = {}
    if "created_after" in value:
        import aws_sdk_emr.types.date

        out["CreatedAfter"] = aws_sdk_emr.types.date.serialize_aws_json_1_1(
            value["created_after"]
        )
    if "created_before" in value:
        import aws_sdk_emr.types.date

        out["CreatedBefore"] = aws_sdk_emr.types.date.serialize_aws_json_1_1(
            value["created_before"]
        )
    if "cluster_states" in value:
        import aws_sdk_emr.types.cluster_state_list

        out["ClusterStates"] = (
            aws_sdk_emr.types.cluster_state_list.serialize_aws_json_1_1(
                value["cluster_states"]
            )
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListClustersInput:
    out: ListClustersInput = {}  # type: ignore[typeddict-item]
    if "CreatedAfter" in data:
        import aws_sdk_emr.types.date

        out["created_after"] = aws_sdk_emr.types.date.deserialize_aws_json_1_1(
            data["CreatedAfter"]
        )
    if "CreatedBefore" in data:
        import aws_sdk_emr.types.date

        out["created_before"] = aws_sdk_emr.types.date.deserialize_aws_json_1_1(
            data["CreatedBefore"]
        )
    if "ClusterStates" in data:
        import aws_sdk_emr.types.cluster_state_list

        out["cluster_states"] = (
            aws_sdk_emr.types.cluster_state_list.deserialize_aws_json_1_1(
                data["ClusterStates"]
            )
        )
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
