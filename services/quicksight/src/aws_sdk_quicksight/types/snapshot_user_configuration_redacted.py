"""Generated from Smithy shape ``com.amazonaws.quicksight#SnapshotUserConfigurationRedacted``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.snapshot_anonymous_user_redacted_list


class SnapshotUserConfigurationRedacted(TypedDict, closed=True):
    anonymous_users: NotRequired[
        "aws_sdk_quicksight.types.snapshot_anonymous_user_redacted_list.SnapshotAnonymousUserRedactedList"
    ]
    """<p> An array of records that describe anonymous users that the dashboard snapshot is generated for. Sensitive user information is excluded. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SnapshotUserConfigurationRedacted) -> dict:
    out: dict = {}
    if "anonymous_users" in value:
        import aws_sdk_quicksight.types.snapshot_anonymous_user_redacted_list

        out["AnonymousUsers"] = (
            aws_sdk_quicksight.types.snapshot_anonymous_user_redacted_list.serialize_json(
                value["anonymous_users"]
            )
        )
    return out


def deserialize_json(data: dict) -> SnapshotUserConfigurationRedacted:
    out: SnapshotUserConfigurationRedacted = {}  # type: ignore[typeddict-item]
    if "AnonymousUsers" in data:
        import aws_sdk_quicksight.types.snapshot_anonymous_user_redacted_list

        out["anonymous_users"] = (
            aws_sdk_quicksight.types.snapshot_anonymous_user_redacted_list.deserialize_json(
                data["AnonymousUsers"]
            )
        )
    return out
