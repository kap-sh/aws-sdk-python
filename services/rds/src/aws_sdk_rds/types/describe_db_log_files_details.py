"""Generated from Smithy shape ``com.amazonaws.rds#DescribeDBLogFilesDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.long
    import aws_sdk_rds.types.string


class DescribeDBLogFilesDetails(TypedDict, closed=True):
    log_file_name: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The name of the log file for the specified DB instance.</p>"""
    last_written: NotRequired["aws_sdk_rds.types.long.Long"]
    """<p>A POSIX timestamp when the last log entry was written.</p>"""
    size: NotRequired["aws_sdk_rds.types.long.Long"]
    """<p>The size, in bytes, of the log file for the specified DB instance.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeDBLogFilesDetails, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "log_file_name" in value:
        pairs.append((f"{prefix}.LogFileName", str(value["log_file_name"])))
    if "last_written" in value:
        pairs.append((f"{prefix}.LastWritten", str(value["last_written"])))
    if "size" in value:
        pairs.append((f"{prefix}.Size", str(value["size"])))


def deserialize_query(el: Element) -> DescribeDBLogFilesDetails:
    out: DescribeDBLogFilesDetails = {}  # type: ignore[typeddict-item]
    child_log_file_name = el.find("LogFileName")
    if child_log_file_name is not None:
        out["log_file_name"] = str(child_log_file_name.text or "")
    child_last_written = el.find("LastWritten")
    if child_last_written is not None:
        out["last_written"] = int(child_last_written.text or "")
    child_size = el.find("Size")
    if child_size is not None:
        out["size"] = int(child_size.text or "")
    return out
