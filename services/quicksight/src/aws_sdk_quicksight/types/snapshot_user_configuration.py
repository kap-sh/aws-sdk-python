"""Generated from Smithy shape ``com.amazonaws.quicksight#SnapshotUserConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.snapshot_anonymous_user_list


class SnapshotUserConfiguration(TypedDict):
    anonymous_users: NotRequired[
        "aws_sdk_quicksight.types.snapshot_anonymous_user_list.SnapshotAnonymousUserList"
    ]
    """<p>An array of records that describe the anonymous users that the dashboard snapshot is generated for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SnapshotUserConfiguration) -> dict:
    out: dict = {}
    if "anonymous_users" in value:
        import aws_sdk_quicksight.types.snapshot_anonymous_user_list

        out["AnonymousUsers"] = (
            aws_sdk_quicksight.types.snapshot_anonymous_user_list.serialize_json(
                value["anonymous_users"]
            )
        )
    return out


def deserialize_json(data: dict) -> SnapshotUserConfiguration:
    out: SnapshotUserConfiguration = {}  # type: ignore[typeddict-item]
    if "AnonymousUsers" in data:
        import aws_sdk_quicksight.types.snapshot_anonymous_user_list

        out["anonymous_users"] = (
            aws_sdk_quicksight.types.snapshot_anonymous_user_list.deserialize_json(
                data["AnonymousUsers"]
            )
        )
    return out
