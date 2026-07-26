"""Generated from Smithy shape ``com.amazonaws.memorydb#ServiceUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.service_update_status
    import capo_memorydb.types.service_update_type
    import capo_memorydb.types.string
    import capo_memorydb.types.t_stamp


class ServiceUpdate(TypedDict, closed=True):
    cluster_name: NotRequired["capo_memorydb.types.string.String"]
    """<p>The name of the cluster to which the service update applies</p>"""
    service_update_name: NotRequired["capo_memorydb.types.string.String"]
    """<p>The unique ID of the service update</p>"""
    release_date: NotRequired["capo_memorydb.types.t_stamp.TStamp"]
    """<p>The date when the service update is initially available</p>"""
    description: NotRequired["capo_memorydb.types.string.String"]
    """<p>Provides details of the service update</p>"""
    status: NotRequired["capo_memorydb.types.service_update_status.ServiceUpdateStatus"]
    """<p>The status of the service update</p>"""
    type: NotRequired["capo_memorydb.types.service_update_type.ServiceUpdateType"]
    """<p>Reflects the nature of the service update</p>"""
    engine: NotRequired["capo_memorydb.types.string.String"]
    """<p>The name of the engine for which a service update is available.</p>"""
    nodes_updated: NotRequired["capo_memorydb.types.string.String"]
    """<p>A list of nodes updated by the service update</p>"""
    auto_update_start_date: NotRequired["capo_memorydb.types.t_stamp.TStamp"]
    """<p>The date at which the service update will be automatically applied</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceUpdate) -> dict:
    out: dict = {}
    if "cluster_name" in value:
        out["ClusterName"] = value["cluster_name"]
    if "service_update_name" in value:
        out["ServiceUpdateName"] = value["service_update_name"]
    if "release_date" in value:
        import capo_memorydb.types.t_stamp

        out["ReleaseDate"] = capo_memorydb.types.t_stamp.serialize_aws_json_1_1(
            value["release_date"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "status" in value:
        import capo_memorydb.types.service_update_status

        out["Status"] = (
            capo_memorydb.types.service_update_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "type" in value:
        import capo_memorydb.types.service_update_type

        out["Type"] = capo_memorydb.types.service_update_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "engine" in value:
        out["Engine"] = value["engine"]
    if "nodes_updated" in value:
        out["NodesUpdated"] = value["nodes_updated"]
    if "auto_update_start_date" in value:
        import capo_memorydb.types.t_stamp

        out["AutoUpdateStartDate"] = capo_memorydb.types.t_stamp.serialize_aws_json_1_1(
            value["auto_update_start_date"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceUpdate:
    out: ServiceUpdate = {}  # type: ignore[typeddict-item]
    if "ClusterName" in data:
        out["cluster_name"] = data["ClusterName"]
    if "ServiceUpdateName" in data:
        out["service_update_name"] = data["ServiceUpdateName"]
    if "ReleaseDate" in data:
        import capo_memorydb.types.t_stamp

        out["release_date"] = capo_memorydb.types.t_stamp.deserialize_aws_json_1_1(
            data["ReleaseDate"]
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "Status" in data:
        import capo_memorydb.types.service_update_status

        out["status"] = (
            capo_memorydb.types.service_update_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "Type" in data:
        import capo_memorydb.types.service_update_type

        out["type"] = capo_memorydb.types.service_update_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if "Engine" in data:
        out["engine"] = data["Engine"]
    if "NodesUpdated" in data:
        out["nodes_updated"] = data["NodesUpdated"]
    if "AutoUpdateStartDate" in data:
        import capo_memorydb.types.t_stamp

        out["auto_update_start_date"] = (
            capo_memorydb.types.t_stamp.deserialize_aws_json_1_1(
                data["AutoUpdateStartDate"]
            )
        )
    return out
