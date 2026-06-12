"""Generated from Smithy shape ``com.amazonaws.wickr#GetGuestUserHistoryCountResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_wickr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wickr.types.guest_user_history_count_list


class GetGuestUserHistoryCountResponse(TypedDict):
    history: (
        "aws_sdk_wickr.types.guest_user_history_count_list.GuestUserHistoryCountList"
    )
    """<p>A list of historical guest user counts, organized by month and billing period.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetGuestUserHistoryCountResponse) -> dict:
    out: dict = {}
    import aws_sdk_wickr.types.guest_user_history_count_list

    out["history"] = aws_sdk_wickr.types.guest_user_history_count_list.serialize_json(
        value["history"]
    )
    return out


def deserialize_json(data: dict) -> GetGuestUserHistoryCountResponse:
    out: GetGuestUserHistoryCountResponse = {}  # type: ignore[typeddict-item]
    if "history" in data:
        import aws_sdk_wickr.types.guest_user_history_count_list

        out["history"] = (
            aws_sdk_wickr.types.guest_user_history_count_list.deserialize_json(
                data["history"]
            )
        )
    else:
        raise DeserializationError("GetGuestUserHistoryCountResponse.history required")
    return out
