"""Generated from Smithy shape ``com.amazonaws.pinpoint#UpdateAdmChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.adm_channel_request


class UpdateAdmChannelRequest(TypedDict, closed=True):
    adm_channel_request: NotRequired[
        "capo_pinpoint.types.adm_channel_request.ADMChannelRequest"
    ]
    application_id: "capo_pinpoint.types.__string.__string"
    """<p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAdmChannelRequest) -> dict:
    out: dict = {}
    if "adm_channel_request" in value:
        import capo_pinpoint.types.adm_channel_request

        out["ADMChannelRequest"] = (
            capo_pinpoint.types.adm_channel_request.serialize_json(
                value["adm_channel_request"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateAdmChannelRequest:
    out: UpdateAdmChannelRequest = {}  # type: ignore[typeddict-item]
    if "ADMChannelRequest" in data:
        import capo_pinpoint.types.adm_channel_request

        out["adm_channel_request"] = (
            capo_pinpoint.types.adm_channel_request.deserialize_json(
                data["ADMChannelRequest"]
            )
        )
    return out
