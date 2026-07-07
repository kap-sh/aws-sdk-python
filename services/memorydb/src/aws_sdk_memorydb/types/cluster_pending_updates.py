"""Generated from Smithy shape ``com.amazonaws.memorydb#ClusterPendingUpdates``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.ac_ls_update_status
    import aws_sdk_memorydb.types.pending_modified_service_update_list
    import aws_sdk_memorydb.types.resharding_status


class ClusterPendingUpdates(TypedDict, closed=True):
    resharding: NotRequired["aws_sdk_memorydb.types.resharding_status.ReshardingStatus"]
    """<p>The status of an online resharding operation.</p>"""
    ac_ls: NotRequired["aws_sdk_memorydb.types.ac_ls_update_status.ACLsUpdateStatus"]
    """<p>A list of ACLs associated with the cluster that are being updated</p>"""
    service_updates: NotRequired[
        "aws_sdk_memorydb.types.pending_modified_service_update_list.PendingModifiedServiceUpdateList"
    ]
    """<p>A list of service updates being applied to the cluster</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterPendingUpdates) -> dict:
    out: dict = {}
    if "resharding" in value:
        import aws_sdk_memorydb.types.resharding_status

        out["Resharding"] = (
            aws_sdk_memorydb.types.resharding_status.serialize_aws_json_1_1(
                value["resharding"]
            )
        )
    if "ac_ls" in value:
        import aws_sdk_memorydb.types.ac_ls_update_status

        out["ACLs"] = aws_sdk_memorydb.types.ac_ls_update_status.serialize_aws_json_1_1(
            value["ac_ls"]
        )
    if "service_updates" in value:
        import aws_sdk_memorydb.types.pending_modified_service_update_list

        out["ServiceUpdates"] = (
            aws_sdk_memorydb.types.pending_modified_service_update_list.serialize_aws_json_1_1(
                value["service_updates"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterPendingUpdates:
    out: ClusterPendingUpdates = {}  # type: ignore[typeddict-item]
    if "Resharding" in data:
        import aws_sdk_memorydb.types.resharding_status

        out["resharding"] = (
            aws_sdk_memorydb.types.resharding_status.deserialize_aws_json_1_1(
                data["Resharding"]
            )
        )
    if "ACLs" in data:
        import aws_sdk_memorydb.types.ac_ls_update_status

        out["ac_ls"] = (
            aws_sdk_memorydb.types.ac_ls_update_status.deserialize_aws_json_1_1(
                data["ACLs"]
            )
        )
    if "ServiceUpdates" in data:
        import aws_sdk_memorydb.types.pending_modified_service_update_list

        out["service_updates"] = (
            aws_sdk_memorydb.types.pending_modified_service_update_list.deserialize_aws_json_1_1(
                data["ServiceUpdates"]
            )
        )
    return out
