"""Generated from Smithy shape ``com.amazonaws.docdb#CloudwatchLogsExportConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_docdb.types.log_type_list


class CloudwatchLogsExportConfiguration(TypedDict):
    enable_log_types: NotRequired["aws_sdk_docdb.types.log_type_list.LogTypeList"]
    """<p>The list of log types to enable.</p>"""
    disable_log_types: NotRequired["aws_sdk_docdb.types.log_type_list.LogTypeList"]
    """<p>The list of log types to disable.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CloudwatchLogsExportConfiguration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "enable_log_types" in value:
        import aws_sdk_docdb.types.log_type_list

        aws_sdk_docdb.types.log_type_list.serialize_query(
            value["enable_log_types"], pairs, f"{prefix}.EnableLogTypes"
        )
    if "disable_log_types" in value:
        import aws_sdk_docdb.types.log_type_list

        aws_sdk_docdb.types.log_type_list.serialize_query(
            value["disable_log_types"], pairs, f"{prefix}.DisableLogTypes"
        )


def deserialize_query(el: Element) -> CloudwatchLogsExportConfiguration:
    out: CloudwatchLogsExportConfiguration = {}  # type: ignore[typeddict-item]
    child_enable_log_types = el.find("EnableLogTypes")
    if child_enable_log_types is not None:
        import aws_sdk_docdb.types.log_type_list

        out["enable_log_types"] = aws_sdk_docdb.types.log_type_list.deserialize_query(
            child_enable_log_types
        )
    child_disable_log_types = el.find("DisableLogTypes")
    if child_disable_log_types is not None:
        import aws_sdk_docdb.types.log_type_list

        out["disable_log_types"] = aws_sdk_docdb.types.log_type_list.deserialize_query(
            child_disable_log_types
        )
    return out
