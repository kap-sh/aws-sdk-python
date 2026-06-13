"""Generated from Smithy shape ``com.amazonaws.backupsearch#S3ItemFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_backupsearch.types.long_condition_list
    import aws_sdk_backupsearch.types.string_condition_list
    import aws_sdk_backupsearch.types.time_condition_list


class S3ItemFilter(TypedDict):
    object_keys: NotRequired[
        "aws_sdk_backupsearch.types.string_condition_list.StringConditionList"
    ]
    """<p>You can include 1 to 10 values.</p> <p>If one value is included, the results will return only items that match the value.</p> <p>If more than one value is included, the results will return all items that match any of the values.</p>"""
    sizes: NotRequired[
        "aws_sdk_backupsearch.types.long_condition_list.LongConditionList"
    ]
    """<p>You can include 1 to 10 values.</p> <p>If one value is included, the results will return only items that match the value.</p> <p>If more than one value is included, the results will return all items that match any of the values.</p>"""
    creation_times: NotRequired[
        "aws_sdk_backupsearch.types.time_condition_list.TimeConditionList"
    ]
    """<p>You can include 1 to 10 values.</p> <p>If one value is included, the results will return only items that match the value.</p> <p>If more than one value is included, the results will return all items that match any of the values.</p>"""
    version_ids: NotRequired[
        "aws_sdk_backupsearch.types.string_condition_list.StringConditionList"
    ]
    """<p>You can include 1 to 10 values.</p> <p>If one value is included, the results will return only items that match the value.</p> <p>If more than one value is included, the results will return all items that match any of the values.</p>"""
    e_tags: NotRequired[
        "aws_sdk_backupsearch.types.string_condition_list.StringConditionList"
    ]
    """<p>You can include 1 to 10 values.</p> <p>If one value is included, the results will return only items that match the value.</p> <p>If more than one value is included, the results will return all items that match any of the values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3ItemFilter) -> dict:
    out: dict = {}
    if "object_keys" in value:
        import aws_sdk_backupsearch.types.string_condition_list

        out["ObjectKeys"] = (
            aws_sdk_backupsearch.types.string_condition_list.serialize_json(
                value["object_keys"]
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
    if "version_ids" in value:
        import aws_sdk_backupsearch.types.string_condition_list

        out["VersionIds"] = (
            aws_sdk_backupsearch.types.string_condition_list.serialize_json(
                value["version_ids"]
            )
        )
    if "e_tags" in value:
        import aws_sdk_backupsearch.types.string_condition_list

        out["ETags"] = aws_sdk_backupsearch.types.string_condition_list.serialize_json(
            value["e_tags"]
        )
    return out


def deserialize_json(data: dict) -> S3ItemFilter:
    out: S3ItemFilter = {}  # type: ignore[typeddict-item]
    if "ObjectKeys" in data:
        import aws_sdk_backupsearch.types.string_condition_list

        out["object_keys"] = (
            aws_sdk_backupsearch.types.string_condition_list.deserialize_json(
                data["ObjectKeys"]
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
    if "VersionIds" in data:
        import aws_sdk_backupsearch.types.string_condition_list

        out["version_ids"] = (
            aws_sdk_backupsearch.types.string_condition_list.deserialize_json(
                data["VersionIds"]
            )
        )
    if "ETags" in data:
        import aws_sdk_backupsearch.types.string_condition_list

        out["e_tags"] = (
            aws_sdk_backupsearch.types.string_condition_list.deserialize_json(
                data["ETags"]
            )
        )
    return out
