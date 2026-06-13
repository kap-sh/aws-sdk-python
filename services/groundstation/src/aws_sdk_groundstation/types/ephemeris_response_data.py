"""Generated from Smithy shape ``com.amazonaws.groundstation#EphemerisResponseData``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.ephemeris_type
    import aws_sdk_groundstation.types.uuid


class EphemerisResponseData(TypedDict):
    ephemeris_id: NotRequired["aws_sdk_groundstation.types.uuid.Uuid"]
    """<p>Unique identifier of the ephemeris. Appears only for custom ephemerides.</p>"""
    ephemeris_type: "aws_sdk_groundstation.types.ephemeris_type.EphemerisType"
    """<p>Type of ephemeris.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EphemerisResponseData) -> dict:
    out: dict = {}
    if "ephemeris_id" in value:
        out["ephemerisId"] = value["ephemeris_id"]
    import aws_sdk_groundstation.types.ephemeris_type

    out["ephemerisType"] = aws_sdk_groundstation.types.ephemeris_type.serialize_json(
        value["ephemeris_type"]
    )
    return out


def deserialize_json(data: dict) -> EphemerisResponseData:
    out: EphemerisResponseData = {}  # type: ignore[typeddict-item]
    if "ephemerisId" in data:
        out["ephemeris_id"] = data["ephemerisId"]
    if "ephemerisType" in data:
        import aws_sdk_groundstation.types.ephemeris_type

        out["ephemeris_type"] = (
            aws_sdk_groundstation.types.ephemeris_type.deserialize_json(
                data["ephemerisType"]
            )
        )
    else:
        raise DeserializationError("EphemerisResponseData.ephemeris_type required")
    return out
