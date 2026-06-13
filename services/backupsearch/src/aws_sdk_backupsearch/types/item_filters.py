"""Generated from Smithy shape ``com.amazonaws.backupsearch#ItemFilters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_backupsearch.types.ebs_item_filters
    import aws_sdk_backupsearch.types.s3_item_filters


class ItemFilters(TypedDict):
    s3_item_filters: NotRequired[
        "aws_sdk_backupsearch.types.s3_item_filters.S3ItemFilters"
    ]
    """<p>This array can contain CreationTimes, ETags, ObjectKeys, Sizes, or VersionIds objects.</p>"""
    ebs_item_filters: NotRequired[
        "aws_sdk_backupsearch.types.ebs_item_filters.EBSItemFilters"
    ]
    """<p>This array can contain CreationTimes, FilePaths, LastModificationTimes, or Sizes objects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ItemFilters) -> dict:
    out: dict = {}
    if "s3_item_filters" in value:
        import aws_sdk_backupsearch.types.s3_item_filters

        out["S3ItemFilters"] = (
            aws_sdk_backupsearch.types.s3_item_filters.serialize_json(
                value["s3_item_filters"]
            )
        )
    if "ebs_item_filters" in value:
        import aws_sdk_backupsearch.types.ebs_item_filters

        out["EBSItemFilters"] = (
            aws_sdk_backupsearch.types.ebs_item_filters.serialize_json(
                value["ebs_item_filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> ItemFilters:
    out: ItemFilters = {}  # type: ignore[typeddict-item]
    if "S3ItemFilters" in data:
        import aws_sdk_backupsearch.types.s3_item_filters

        out["s3_item_filters"] = (
            aws_sdk_backupsearch.types.s3_item_filters.deserialize_json(
                data["S3ItemFilters"]
            )
        )
    if "EBSItemFilters" in data:
        import aws_sdk_backupsearch.types.ebs_item_filters

        out["ebs_item_filters"] = (
            aws_sdk_backupsearch.types.ebs_item_filters.deserialize_json(
                data["EBSItemFilters"]
            )
        )
    return out
