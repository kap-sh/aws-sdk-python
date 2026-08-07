"""Generated from Smithy shape ``com.amazonaws.docdb#CloudwatchLogsExportConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import capo_docdb.types.log_type_list


class CloudwatchLogsExportConfiguration(TypedDict, closed=True):
    enable_log_types: NotRequired["capo_docdb.types.log_type_list.LogTypeList"]
    """<p>The list of log types to enable.</p>"""
    disable_log_types: NotRequired["capo_docdb.types.log_type_list.LogTypeList"]
    """<p>The list of log types to disable.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CloudwatchLogsExportConfiguration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "enable_log_types" in value:
        import capo_docdb.types.log_type_list

        capo_docdb.types.log_type_list.serialize_query(
            value["enable_log_types"], pairs, f"{key_prefix}EnableLogTypes"
        )
    if "disable_log_types" in value:
        import capo_docdb.types.log_type_list

        capo_docdb.types.log_type_list.serialize_query(
            value["disable_log_types"], pairs, f"{key_prefix}DisableLogTypes"
        )


def deserialize_query(el: Element) -> CloudwatchLogsExportConfiguration:
    out: CloudwatchLogsExportConfiguration = {}  # type: ignore[typeddict-item]
    child_enable_log_types = el.find("EnableLogTypes")
    if child_enable_log_types is not None:
        import capo_docdb.types.log_type_list

        out["enable_log_types"] = capo_docdb.types.log_type_list.deserialize_query(
            child_enable_log_types
        )
    child_disable_log_types = el.find("DisableLogTypes")
    if child_disable_log_types is not None:
        import capo_docdb.types.log_type_list

        out["disable_log_types"] = capo_docdb.types.log_type_list.deserialize_query(
            child_disable_log_types
        )
    return out
