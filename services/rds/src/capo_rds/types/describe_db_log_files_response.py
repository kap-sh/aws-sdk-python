"""Generated from Smithy shape ``com.amazonaws.rds#DescribeDBLogFilesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.describe_db_log_files_list
    import capo_rds.types.string


class DescribeDBLogFilesResponse(TypedDict, closed=True):
    describe_db_log_files: NotRequired[
        "capo_rds.types.describe_db_log_files_list.DescribeDBLogFilesList"
    ]
    """<p>The DB log files returned.</p>"""
    marker: NotRequired["capo_rds.types.string.String"]
    """<p>A pagination token that can be used in a later <code>DescribeDBLogFiles</code> request.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeDBLogFilesResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "describe_db_log_files" in value:
        import capo_rds.types.describe_db_log_files_list

        capo_rds.types.describe_db_log_files_list.serialize_query(
            value["describe_db_log_files"], pairs, f"{prefix}.DescribeDBLogFiles"
        )
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))


def deserialize_query(el: Element) -> DescribeDBLogFilesResponse:
    out: DescribeDBLogFilesResponse = {}  # type: ignore[typeddict-item]
    child_describe_db_log_files = el.find("DescribeDBLogFiles")
    if child_describe_db_log_files is not None:
        import capo_rds.types.describe_db_log_files_list

        out["describe_db_log_files"] = (
            capo_rds.types.describe_db_log_files_list.deserialize_query(
                child_describe_db_log_files
            )
        )
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
