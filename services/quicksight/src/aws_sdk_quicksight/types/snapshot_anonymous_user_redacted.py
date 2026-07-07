"""Generated from Smithy shape ``com.amazonaws.quicksight#SnapshotAnonymousUserRedacted``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.session_tag_key_list


class SnapshotAnonymousUserRedacted(TypedDict, closed=True):
    row_level_permission_tag_keys: NotRequired[
        "aws_sdk_quicksight.types.session_tag_key_list.SessionTagKeyList"
    ]
    """<p>The tag keys for the <code>RowLevelPermissionTags</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SnapshotAnonymousUserRedacted) -> dict:
    out: dict = {}
    if "row_level_permission_tag_keys" in value:
        import aws_sdk_quicksight.types.session_tag_key_list

        out["RowLevelPermissionTagKeys"] = (
            aws_sdk_quicksight.types.session_tag_key_list.serialize_json(
                value["row_level_permission_tag_keys"]
            )
        )
    return out


def deserialize_json(data: dict) -> SnapshotAnonymousUserRedacted:
    out: SnapshotAnonymousUserRedacted = {}  # type: ignore[typeddict-item]
    if "RowLevelPermissionTagKeys" in data:
        import aws_sdk_quicksight.types.session_tag_key_list

        out["row_level_permission_tag_keys"] = (
            aws_sdk_quicksight.types.session_tag_key_list.deserialize_json(
                data["RowLevelPermissionTagKeys"]
            )
        )
    return out
