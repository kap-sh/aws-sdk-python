"""Generated from Smithy shape ``com.amazonaws.docdb#PendingCloudwatchLogsExports``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_docdb.types.log_type_list


class PendingCloudwatchLogsExports(TypedDict, closed=True):
    log_types_to_enable: NotRequired["aws_sdk_docdb.types.log_type_list.LogTypeList"]
    """<p>Log types that are in the process of being deactivated. After they are deactivated, these log types aren't exported to CloudWatch Logs.</p>"""
    log_types_to_disable: NotRequired["aws_sdk_docdb.types.log_type_list.LogTypeList"]
    """<p>Log types that are in the process of being enabled. After they are enabled, these log types are exported to Amazon CloudWatch Logs.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PendingCloudwatchLogsExports, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "log_types_to_enable" in value:
        import aws_sdk_docdb.types.log_type_list

        aws_sdk_docdb.types.log_type_list.serialize_query(
            value["log_types_to_enable"], pairs, f"{prefix}.LogTypesToEnable"
        )
    if "log_types_to_disable" in value:
        import aws_sdk_docdb.types.log_type_list

        aws_sdk_docdb.types.log_type_list.serialize_query(
            value["log_types_to_disable"], pairs, f"{prefix}.LogTypesToDisable"
        )


def deserialize_query(el: Element) -> PendingCloudwatchLogsExports:
    out: PendingCloudwatchLogsExports = {}  # type: ignore[typeddict-item]
    child_log_types_to_enable = el.find("LogTypesToEnable")
    if child_log_types_to_enable is not None:
        import aws_sdk_docdb.types.log_type_list

        out["log_types_to_enable"] = (
            aws_sdk_docdb.types.log_type_list.deserialize_query(
                child_log_types_to_enable
            )
        )
    child_log_types_to_disable = el.find("LogTypesToDisable")
    if child_log_types_to_disable is not None:
        import aws_sdk_docdb.types.log_type_list

        out["log_types_to_disable"] = (
            aws_sdk_docdb.types.log_type_list.deserialize_query(
                child_log_types_to_disable
            )
        )
    return out
