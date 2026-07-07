"""Generated from Smithy shape ``com.amazonaws.elasticache#CacheParameterGroupStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.cache_node_ids_list
    import aws_sdk_elasticache.types.string


class CacheParameterGroupStatus(TypedDict, closed=True):
    cache_parameter_group_name: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The name of the cache parameter group.</p>"""
    parameter_apply_status: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The status of parameter updates.</p>"""
    cache_node_ids_to_reboot: NotRequired[
        "aws_sdk_elasticache.types.cache_node_ids_list.CacheNodeIdsList"
    ]
    """<p>A list of the cache node IDs which need to be rebooted for parameter changes to be applied. A node ID is a numeric identifier (0001, 0002, etc.).</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CacheParameterGroupStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cache_parameter_group_name" in value:
        pairs.append(
            (
                f"{prefix}.CacheParameterGroupName",
                str(value["cache_parameter_group_name"]),
            )
        )
    if "parameter_apply_status" in value:
        pairs.append(
            (f"{prefix}.ParameterApplyStatus", str(value["parameter_apply_status"]))
        )
    if "cache_node_ids_to_reboot" in value:
        import aws_sdk_elasticache.types.cache_node_ids_list

        aws_sdk_elasticache.types.cache_node_ids_list.serialize_query(
            value["cache_node_ids_to_reboot"], pairs, f"{prefix}.CacheNodeIdsToReboot"
        )


def deserialize_query(el: Element) -> CacheParameterGroupStatus:
    out: CacheParameterGroupStatus = {}  # type: ignore[typeddict-item]
    child_cache_parameter_group_name = el.find("CacheParameterGroupName")
    if child_cache_parameter_group_name is not None:
        out["cache_parameter_group_name"] = str(
            child_cache_parameter_group_name.text or ""
        )
    child_parameter_apply_status = el.find("ParameterApplyStatus")
    if child_parameter_apply_status is not None:
        out["parameter_apply_status"] = str(child_parameter_apply_status.text or "")
    child_cache_node_ids_to_reboot = el.find("CacheNodeIdsToReboot")
    if child_cache_node_ids_to_reboot is not None:
        import aws_sdk_elasticache.types.cache_node_ids_list

        out["cache_node_ids_to_reboot"] = (
            aws_sdk_elasticache.types.cache_node_ids_list.deserialize_query(
                child_cache_node_ids_to_reboot
            )
        )
    return out
