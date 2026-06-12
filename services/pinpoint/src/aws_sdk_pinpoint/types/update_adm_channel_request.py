"""Generated from Smithy shape ``com.amazonaws.pinpoint#UpdateAdmChannelRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.adm_channel_request


class UpdateAdmChannelRequest(TypedDict):
    adm_channel_request: NotRequired[
        "aws_sdk_pinpoint.types.adm_channel_request.ADMChannelRequest"
    ]
    application_id: "aws_sdk_pinpoint.types.__string.__string"
    """<p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAdmChannelRequest) -> dict:
    out: dict = {}
    if "adm_channel_request" in value:
        import aws_sdk_pinpoint.types.adm_channel_request

        out["ADMChannelRequest"] = (
            aws_sdk_pinpoint.types.adm_channel_request.serialize_json(
                value["adm_channel_request"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateAdmChannelRequest:
    out: UpdateAdmChannelRequest = {}  # type: ignore[typeddict-item]
    if "ADMChannelRequest" in data:
        import aws_sdk_pinpoint.types.adm_channel_request

        out["adm_channel_request"] = (
            aws_sdk_pinpoint.types.adm_channel_request.deserialize_json(
                data["ADMChannelRequest"]
            )
        )
    return out
