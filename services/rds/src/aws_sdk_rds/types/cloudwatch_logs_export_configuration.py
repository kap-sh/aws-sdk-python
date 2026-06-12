"""Generated from Smithy shape ``com.amazonaws.rds#CloudwatchLogsExportConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.log_type_list


class CloudwatchLogsExportConfiguration(TypedDict):
    enable_log_types: NotRequired["aws_sdk_rds.types.log_type_list.LogTypeList"]
    """<p>The list of log types to enable.</p> <p>The following values are valid for each DB engine:</p> <ul> <li> <p>Aurora MySQL - <code>audit | error | general | slowquery</code> </p> </li> <li> <p>Aurora PostgreSQL - <code>postgresql</code> </p> </li> <li> <p>RDS for MySQL - <code>error | general | slowquery</code> </p> </li> <li> <p>RDS for PostgreSQL - <code>postgresql | upgrade</code> </p> </li> </ul>"""
    disable_log_types: NotRequired["aws_sdk_rds.types.log_type_list.LogTypeList"]
    """<p>The list of log types to disable.</p> <p>The following values are valid for each DB engine:</p> <ul> <li> <p>Aurora MySQL - <code>audit | error | general | slowquery</code> </p> </li> <li> <p>Aurora PostgreSQL - <code>postgresql</code> </p> </li> <li> <p>RDS for MySQL - <code>error | general | slowquery</code> </p> </li> <li> <p>RDS for PostgreSQL - <code>postgresql | upgrade</code> </p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CloudwatchLogsExportConfiguration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "enable_log_types" in value:
        import aws_sdk_rds.types.log_type_list

        aws_sdk_rds.types.log_type_list.serialize_query(
            value["enable_log_types"], pairs, f"{prefix}.EnableLogTypes"
        )
    if "disable_log_types" in value:
        import aws_sdk_rds.types.log_type_list

        aws_sdk_rds.types.log_type_list.serialize_query(
            value["disable_log_types"], pairs, f"{prefix}.DisableLogTypes"
        )


def deserialize_query(el: Element) -> CloudwatchLogsExportConfiguration:
    out: CloudwatchLogsExportConfiguration = {}  # type: ignore[typeddict-item]
    child_enable_log_types = el.find("EnableLogTypes")
    if child_enable_log_types is not None:
        import aws_sdk_rds.types.log_type_list

        out["enable_log_types"] = aws_sdk_rds.types.log_type_list.deserialize_query(
            child_enable_log_types
        )
    child_disable_log_types = el.find("DisableLogTypes")
    if child_disable_log_types is not None:
        import aws_sdk_rds.types.log_type_list

        out["disable_log_types"] = aws_sdk_rds.types.log_type_list.deserialize_query(
            child_disable_log_types
        )
    return out
