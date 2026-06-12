"""Generated from Smithy shape ``com.amazonaws.firehose#DatabaseColumnList``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_firehose.types.database_column_include_or_exclude_list


class DatabaseColumnList(TypedDict):
    include: NotRequired[
        "aws_sdk_firehose.types.database_column_include_or_exclude_list.DatabaseColumnIncludeOrExcludeList"
    ]
    """<p> The list of column patterns in source database to be included for Firehose to read from. </p> <p>Amazon Data Firehose is in preview release and is subject to change.</p>"""
    exclude: NotRequired[
        "aws_sdk_firehose.types.database_column_include_or_exclude_list.DatabaseColumnIncludeOrExcludeList"
    ]
    """<p> The list of column patterns in source database to be excluded for Firehose to read from. </p> <p>Amazon Data Firehose is in preview release and is subject to change.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatabaseColumnList) -> dict:
    out: dict = {}
    if "include" in value:
        import aws_sdk_firehose.types.database_column_include_or_exclude_list

        out["Include"] = (
            aws_sdk_firehose.types.database_column_include_or_exclude_list.serialize_aws_json_1_1(
                value["include"]
            )
        )
    if "exclude" in value:
        import aws_sdk_firehose.types.database_column_include_or_exclude_list

        out["Exclude"] = (
            aws_sdk_firehose.types.database_column_include_or_exclude_list.serialize_aws_json_1_1(
                value["exclude"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DatabaseColumnList:
    out: DatabaseColumnList = {}  # type: ignore[typeddict-item]
    if "Include" in data:
        import aws_sdk_firehose.types.database_column_include_or_exclude_list

        out["include"] = (
            aws_sdk_firehose.types.database_column_include_or_exclude_list.deserialize_aws_json_1_1(
                data["Include"]
            )
        )
    if "Exclude" in data:
        import aws_sdk_firehose.types.database_column_include_or_exclude_list

        out["exclude"] = (
            aws_sdk_firehose.types.database_column_include_or_exclude_list.deserialize_aws_json_1_1(
                data["Exclude"]
            )
        )
    return out
