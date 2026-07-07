"""Generated from Smithy shape ``com.amazonaws.chime#AlexaForBusinessMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime.types.boolean
    import aws_sdk_chime.types.sensitive_string


class AlexaForBusinessMetadata(TypedDict, closed=True):
    is_alexa_for_business_enabled: NotRequired["aws_sdk_chime.types.boolean.Boolean"]
    """<p>Starts or stops Alexa for Business.</p>"""
    alexa_for_business_room_arn: NotRequired[
        "aws_sdk_chime.types.sensitive_string.SensitiveString"
    ]
    """<p>The ARN of the room resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AlexaForBusinessMetadata) -> dict:
    out: dict = {}
    if "is_alexa_for_business_enabled" in value:
        out["IsAlexaForBusinessEnabled"] = value["is_alexa_for_business_enabled"]
    if "alexa_for_business_room_arn" in value:
        out["AlexaForBusinessRoomArn"] = value["alexa_for_business_room_arn"]
    return out


def deserialize_json(data: dict) -> AlexaForBusinessMetadata:
    out: AlexaForBusinessMetadata = {}  # type: ignore[typeddict-item]
    if "IsAlexaForBusinessEnabled" in data:
        out["is_alexa_for_business_enabled"] = data["IsAlexaForBusinessEnabled"]
    if "AlexaForBusinessRoomArn" in data:
        out["alexa_for_business_room_arn"] = data["AlexaForBusinessRoomArn"]
    return out
