"""Generated from Smithy shape ``com.amazonaws.neptune#PendingCloudwatchLogsExports``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import capo_neptune.types.log_type_list


class PendingCloudwatchLogsExports(TypedDict, closed=True):
    log_types_to_enable: NotRequired["capo_neptune.types.log_type_list.LogTypeList"]
    """<p>Log types that are in the process of being deactivated. After they are deactivated, these log types aren't exported to CloudWatch Logs.</p>"""
    log_types_to_disable: NotRequired["capo_neptune.types.log_type_list.LogTypeList"]
    """<p>Log types that are in the process of being enabled. After they are enabled, these log types are exported to CloudWatch Logs.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PendingCloudwatchLogsExports, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "log_types_to_enable" in value:
        import capo_neptune.types.log_type_list

        capo_neptune.types.log_type_list.serialize_query(
            value["log_types_to_enable"], pairs, f"{key_prefix}LogTypesToEnable"
        )
    if "log_types_to_disable" in value:
        import capo_neptune.types.log_type_list

        capo_neptune.types.log_type_list.serialize_query(
            value["log_types_to_disable"], pairs, f"{key_prefix}LogTypesToDisable"
        )


def deserialize_query(el: Element) -> PendingCloudwatchLogsExports:
    out: PendingCloudwatchLogsExports = {}  # type: ignore[typeddict-item]
    child_log_types_to_enable = el.find("LogTypesToEnable")
    if child_log_types_to_enable is not None:
        import capo_neptune.types.log_type_list

        out["log_types_to_enable"] = capo_neptune.types.log_type_list.deserialize_query(
            child_log_types_to_enable
        )
    child_log_types_to_disable = el.find("LogTypesToDisable")
    if child_log_types_to_disable is not None:
        import capo_neptune.types.log_type_list

        out["log_types_to_disable"] = (
            capo_neptune.types.log_type_list.deserialize_query(
                child_log_types_to_disable
            )
        )
    return out
