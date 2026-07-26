"""Generated from Smithy shape ``com.amazonaws.firehose#DatabaseTableList``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_firehose.types.database_table_include_or_exclude_list


class DatabaseTableList(TypedDict, closed=True):
    include: NotRequired[
        "capo_firehose.types.database_table_include_or_exclude_list.DatabaseTableIncludeOrExcludeList"
    ]
    """<p>The list of table patterns in source database endpoint to be included for Firehose to read from. </p> <p>Amazon Data Firehose is in preview release and is subject to change.</p>"""
    exclude: NotRequired[
        "capo_firehose.types.database_table_include_or_exclude_list.DatabaseTableIncludeOrExcludeList"
    ]
    """<p>The list of table patterns in source database endpoint to be excluded for Firehose to read from. </p> <p>Amazon Data Firehose is in preview release and is subject to change.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatabaseTableList) -> dict:
    out: dict = {}
    if "include" in value:
        import capo_firehose.types.database_table_include_or_exclude_list

        out["Include"] = (
            capo_firehose.types.database_table_include_or_exclude_list.serialize_aws_json_1_1(
                value["include"]
            )
        )
    if "exclude" in value:
        import capo_firehose.types.database_table_include_or_exclude_list

        out["Exclude"] = (
            capo_firehose.types.database_table_include_or_exclude_list.serialize_aws_json_1_1(
                value["exclude"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DatabaseTableList:
    out: DatabaseTableList = {}  # type: ignore[typeddict-item]
    if "Include" in data:
        import capo_firehose.types.database_table_include_or_exclude_list

        out["include"] = (
            capo_firehose.types.database_table_include_or_exclude_list.deserialize_aws_json_1_1(
                data["Include"]
            )
        )
    if "Exclude" in data:
        import capo_firehose.types.database_table_include_or_exclude_list

        out["exclude"] = (
            capo_firehose.types.database_table_include_or_exclude_list.deserialize_aws_json_1_1(
                data["Exclude"]
            )
        )
    return out
