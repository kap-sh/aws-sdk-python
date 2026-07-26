"""Generated from Smithy shape ``com.amazonaws.rds#DescribeDBLogFilesList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.describe_db_log_files_details

DescribeDBLogFilesList: TypeAlias = list[
    "capo_rds.types.describe_db_log_files_details.DescribeDBLogFilesDetails"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeDBLogFilesList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.describe_db_log_files_details

    for n, item in enumerate(value, 1):
        capo_rds.types.describe_db_log_files_details.serialize_query(
            item, pairs, f"{prefix}.DescribeDBLogFilesDetails.{n}"
        )


def deserialize_query(el: Element) -> DescribeDBLogFilesList:
    import capo_rds.types.describe_db_log_files_details

    out: DescribeDBLogFilesList = []
    for child in el.findall("DescribeDBLogFilesDetails"):
        out.append(
            capo_rds.types.describe_db_log_files_details.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: DescribeDBLogFilesList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.describe_db_log_files_details

    for n, item in enumerate(value, 1):
        capo_rds.types.describe_db_log_files_details.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> DescribeDBLogFilesList:
    import capo_rds.types.describe_db_log_files_details

    out: DescribeDBLogFilesList = []
    for child in parent.findall(tag):
        out.append(
            capo_rds.types.describe_db_log_files_details.deserialize_query(child)
        )
    return out
