"""Generated from Smithy shape ``com.amazonaws.pinpoint#UpdateEmailChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.email_channel_request


class UpdateEmailChannelRequest(TypedDict, closed=True):
    application_id: "capo_pinpoint.types.__string.__string"
    """<p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>"""
    email_channel_request: NotRequired[
        "capo_pinpoint.types.email_channel_request.EmailChannelRequest"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEmailChannelRequest) -> dict:
    out: dict = {}
    if "email_channel_request" in value:
        import capo_pinpoint.types.email_channel_request

        out["EmailChannelRequest"] = (
            capo_pinpoint.types.email_channel_request.serialize_json(
                value["email_channel_request"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateEmailChannelRequest:
    out: UpdateEmailChannelRequest = {}  # type: ignore[typeddict-item]
    if "EmailChannelRequest" in data:
        import capo_pinpoint.types.email_channel_request

        out["email_channel_request"] = (
            capo_pinpoint.types.email_channel_request.deserialize_json(
                data["EmailChannelRequest"]
            )
        )
    return out
