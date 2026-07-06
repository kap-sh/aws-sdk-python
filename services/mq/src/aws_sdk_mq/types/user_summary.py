"""Generated from Smithy shape ``com.amazonaws.mq#UserSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mq.types.__string
    import aws_sdk_mq.types.change_type


class UserSummary(TypedDict, closed=True):
    pending_change: NotRequired["aws_sdk_mq.types.change_type.ChangeType"]
    """<p>The type of change pending for the broker user.</p>"""
    username: NotRequired["aws_sdk_mq.types.__string.__string"]
    """<p>Required. The username of the broker user. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 2-100 characters long.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserSummary) -> dict:
    out: dict = {}
    if "pending_change" in value:
        import aws_sdk_mq.types.change_type

        out["pendingChange"] = aws_sdk_mq.types.change_type.serialize_json(
            value["pending_change"]
        )
    if "username" in value:
        out["username"] = value["username"]
    return out


def deserialize_json(data: dict) -> UserSummary:
    out: UserSummary = {}  # type: ignore[typeddict-item]
    if "pendingChange" in data:
        import aws_sdk_mq.types.change_type

        out["pending_change"] = aws_sdk_mq.types.change_type.deserialize_json(
            data["pendingChange"]
        )
    if "username" in data:
        out["username"] = data["username"]
    return out
