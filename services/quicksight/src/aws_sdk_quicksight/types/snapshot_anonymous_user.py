"""Generated from Smithy shape ``com.amazonaws.quicksight#SnapshotAnonymousUser``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.session_tag_list


class SnapshotAnonymousUser(TypedDict):
    row_level_permission_tags: NotRequired[
        "aws_sdk_quicksight.types.session_tag_list.SessionTagList"
    ]
    """<p>The tags to be used for row-level security (RLS). Make sure that the relevant datasets have RLS tags configured before you start a snapshot export job. You can configure the RLS tags of a dataset with a <code>DataSet$RowLevelPermissionTagConfiguration</code> API call.</p> <p>These are not the tags that are used for Amazon Web Services resource tagging. For more information on row level security in Amazon Quick Sight, see <a href=\"https://docs.aws.amazon.com/quicksight/latest/user/quicksight-dev-rls-tags.html\">Using Row-Level Security (RLS) with Tags</a>in the <i>Amazon Quick User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SnapshotAnonymousUser) -> dict:
    out: dict = {}
    if "row_level_permission_tags" in value:
        import aws_sdk_quicksight.types.session_tag_list

        out["RowLevelPermissionTags"] = (
            aws_sdk_quicksight.types.session_tag_list.serialize_json(
                value["row_level_permission_tags"]
            )
        )
    return out


def deserialize_json(data: dict) -> SnapshotAnonymousUser:
    out: SnapshotAnonymousUser = {}  # type: ignore[typeddict-item]
    if "RowLevelPermissionTags" in data:
        import aws_sdk_quicksight.types.session_tag_list

        out["row_level_permission_tags"] = (
            aws_sdk_quicksight.types.session_tag_list.deserialize_json(
                data["RowLevelPermissionTags"]
            )
        )
    return out
