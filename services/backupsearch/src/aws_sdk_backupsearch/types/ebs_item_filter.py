"""Generated from Smithy shape ``com.amazonaws.backupsearch#EBSItemFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_backupsearch.types.long_condition_list
    import aws_sdk_backupsearch.types.string_condition_list
    import aws_sdk_backupsearch.types.time_condition_list


class EBSItemFilter(TypedDict, closed=True):
    file_paths: NotRequired[
        "aws_sdk_backupsearch.types.string_condition_list.StringConditionList"
    ]
    """<p>You can include 1 to 10 values.</p> <p>If one file path is included, the results will return only items that match the file path.</p> <p>If more than one file path is included, the results will return all items that match any of the file paths.</p>"""
    sizes: NotRequired[
        "aws_sdk_backupsearch.types.long_condition_list.LongConditionList"
    ]
    """<p>You can include 1 to 10 values.</p> <p>If one is included, the results will return only items that match.</p> <p>If more than one is included, the results will return all items that match any of the included values.</p>"""
    creation_times: NotRequired[
        "aws_sdk_backupsearch.types.time_condition_list.TimeConditionList"
    ]
    """<p>You can include 1 to 10 values.</p> <p>If one is included, the results will return only items that match.</p> <p>If more than one is included, the results will return all items that match any of the included values.</p>"""
    last_modification_times: NotRequired[
        "aws_sdk_backupsearch.types.time_condition_list.TimeConditionList"
    ]
    """<p>You can include 1 to 10 values.</p> <p>If one is included, the results will return only items that match.</p> <p>If more than one is included, the results will return all items that match any of the included values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EBSItemFilter) -> dict:
    out: dict = {}
    if "file_paths" in value:
        import aws_sdk_backupsearch.types.string_condition_list

        out["FilePaths"] = (
            aws_sdk_backupsearch.types.string_condition_list.serialize_json(
                value["file_paths"]
            )
        )
    if "sizes" in value:
        import aws_sdk_backupsearch.types.long_condition_list

        out["Sizes"] = aws_sdk_backupsearch.types.long_condition_list.serialize_json(
            value["sizes"]
        )
    if "creation_times" in value:
        import aws_sdk_backupsearch.types.time_condition_list

        out["CreationTimes"] = (
            aws_sdk_backupsearch.types.time_condition_list.serialize_json(
                value["creation_times"]
            )
        )
    if "last_modification_times" in value:
        import aws_sdk_backupsearch.types.time_condition_list

        out["LastModificationTimes"] = (
            aws_sdk_backupsearch.types.time_condition_list.serialize_json(
                value["last_modification_times"]
            )
        )
    return out


def deserialize_json(data: dict) -> EBSItemFilter:
    out: EBSItemFilter = {}  # type: ignore[typeddict-item]
    if "FilePaths" in data:
        import aws_sdk_backupsearch.types.string_condition_list

        out["file_paths"] = (
            aws_sdk_backupsearch.types.string_condition_list.deserialize_json(
                data["FilePaths"]
            )
        )
    if "Sizes" in data:
        import aws_sdk_backupsearch.types.long_condition_list

        out["sizes"] = aws_sdk_backupsearch.types.long_condition_list.deserialize_json(
            data["Sizes"]
        )
    if "CreationTimes" in data:
        import aws_sdk_backupsearch.types.time_condition_list

        out["creation_times"] = (
            aws_sdk_backupsearch.types.time_condition_list.deserialize_json(
                data["CreationTimes"]
            )
        )
    if "LastModificationTimes" in data:
        import aws_sdk_backupsearch.types.time_condition_list

        out["last_modification_times"] = (
            aws_sdk_backupsearch.types.time_condition_list.deserialize_json(
                data["LastModificationTimes"]
            )
        )
    return out
