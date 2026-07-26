"""Generated from Smithy shape ``com.amazonaws.kafka#UpdateConnectivityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__string
    import capo_kafka.types.connectivity_info
    import capo_kafka.types.zookeeper_access


class UpdateConnectivityRequest(TypedDict, closed=True):
    cluster_arn: "capo_kafka.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the configuration.</p>"""
    connectivity_info: NotRequired[
        "capo_kafka.types.connectivity_info.ConnectivityInfo"
    ]
    """<p>Information about the broker access configuration.</p>"""
    current_version: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The version of the MSK cluster to update. Cluster versions aren't simple numbers. You can describe an MSK cluster to find its version. When this update operation is successful, it generates a new cluster version.</p>"""
    zookeeper_access: NotRequired["capo_kafka.types.zookeeper_access.ZookeeperAccess"]
    """<p>Access control settings for zookeeper</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConnectivityRequest) -> dict:
    out: dict = {}
    if "connectivity_info" in value:
        import capo_kafka.types.connectivity_info

        out["connectivityInfo"] = capo_kafka.types.connectivity_info.serialize_json(
            value["connectivity_info"]
        )
    if "current_version" in value:
        out["currentVersion"] = value["current_version"]
    if "zookeeper_access" in value:
        import capo_kafka.types.zookeeper_access

        out["zookeeperAccess"] = capo_kafka.types.zookeeper_access.serialize_json(
            value["zookeeper_access"]
        )
    return out


def deserialize_json(data: dict) -> UpdateConnectivityRequest:
    out: UpdateConnectivityRequest = {}  # type: ignore[typeddict-item]
    if "connectivityInfo" in data:
        import capo_kafka.types.connectivity_info

        out["connectivity_info"] = capo_kafka.types.connectivity_info.deserialize_json(
            data["connectivityInfo"]
        )
    if "currentVersion" in data:
        out["current_version"] = data["currentVersion"]
    if "zookeeperAccess" in data:
        import capo_kafka.types.zookeeper_access

        out["zookeeper_access"] = capo_kafka.types.zookeeper_access.deserialize_json(
            data["zookeeperAccess"]
        )
    return out
