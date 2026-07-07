"""Generated from Smithy shape ``com.amazonaws.mailmanager#ArchiveFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.archive_filter_conditions


class ArchiveFilters(TypedDict, closed=True):
    include: NotRequired[
        "aws_sdk_mailmanager.types.archive_filter_conditions.ArchiveFilterConditions"
    ]
    """<p>The filter conditions for emails to include.</p>"""
    unless: NotRequired[
        "aws_sdk_mailmanager.types.archive_filter_conditions.ArchiveFilterConditions"
    ]
    """<p>The filter conditions for emails to exclude.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ArchiveFilters) -> dict:
    out: dict = {}
    if "include" in value:
        import aws_sdk_mailmanager.types.archive_filter_conditions

        out["Include"] = (
            aws_sdk_mailmanager.types.archive_filter_conditions.serialize_aws_json_1_0(
                value["include"]
            )
        )
    if "unless" in value:
        import aws_sdk_mailmanager.types.archive_filter_conditions

        out["Unless"] = (
            aws_sdk_mailmanager.types.archive_filter_conditions.serialize_aws_json_1_0(
                value["unless"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ArchiveFilters:
    out: ArchiveFilters = {}  # type: ignore[typeddict-item]
    if "Include" in data:
        import aws_sdk_mailmanager.types.archive_filter_conditions

        out["include"] = (
            aws_sdk_mailmanager.types.archive_filter_conditions.deserialize_aws_json_1_0(
                data["Include"]
            )
        )
    if "Unless" in data:
        import aws_sdk_mailmanager.types.archive_filter_conditions

        out["unless"] = (
            aws_sdk_mailmanager.types.archive_filter_conditions.deserialize_aws_json_1_0(
                data["Unless"]
            )
        )
    return out
