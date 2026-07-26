"""Generated from Smithy shape ``com.amazonaws.quicksight#SnapshotAnonymousUserRedacted``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.session_tag_key_list


class SnapshotAnonymousUserRedacted(TypedDict, closed=True):
    row_level_permission_tag_keys: NotRequired[
        "capo_quicksight.types.session_tag_key_list.SessionTagKeyList"
    ]
    """<p>The tag keys for the <code>RowLevelPermissionTags</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SnapshotAnonymousUserRedacted) -> dict:
    out: dict = {}
    if "row_level_permission_tag_keys" in value:
        import capo_quicksight.types.session_tag_key_list

        out["RowLevelPermissionTagKeys"] = (
            capo_quicksight.types.session_tag_key_list.serialize_json(
                value["row_level_permission_tag_keys"]
            )
        )
    return out


def deserialize_json(data: dict) -> SnapshotAnonymousUserRedacted:
    out: SnapshotAnonymousUserRedacted = {}  # type: ignore[typeddict-item]
    if "RowLevelPermissionTagKeys" in data:
        import capo_quicksight.types.session_tag_key_list

        out["row_level_permission_tag_keys"] = (
            capo_quicksight.types.session_tag_key_list.deserialize_json(
                data["RowLevelPermissionTagKeys"]
            )
        )
    return out
