"""Generated from Smithy shape ``com.amazonaws.pinpoint#DeleteAdmChannelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.adm_channel_response


class DeleteAdmChannelResponse(TypedDict, closed=True):
    adm_channel_response: NotRequired[
        "aws_sdk_pinpoint.types.adm_channel_response.ADMChannelResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAdmChannelResponse) -> dict:
    out: dict = {}
    if "adm_channel_response" in value:
        import aws_sdk_pinpoint.types.adm_channel_response

        out["ADMChannelResponse"] = (
            aws_sdk_pinpoint.types.adm_channel_response.serialize_json(
                value["adm_channel_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeleteAdmChannelResponse:
    out: DeleteAdmChannelResponse = {}  # type: ignore[typeddict-item]
    if "ADMChannelResponse" in data:
        import aws_sdk_pinpoint.types.adm_channel_response

        out["adm_channel_response"] = (
            aws_sdk_pinpoint.types.adm_channel_response.deserialize_json(
                data["ADMChannelResponse"]
            )
        )
    return out
