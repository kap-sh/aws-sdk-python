"""Generated from Smithy shape ``com.amazonaws.groundstation#EphemerisDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.s3_object
    import aws_sdk_groundstation.types.unbounded_string


class EphemerisDescription(TypedDict):
    source_s3_object: NotRequired["aws_sdk_groundstation.types.s3_object.S3Object"]
    """<p>Source Amazon S3 object used for the ephemeris.</p>"""
    ephemeris_data: NotRequired[
        "aws_sdk_groundstation.types.unbounded_string.UnboundedString"
    ]
    """<p>Supplied ephemeris data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EphemerisDescription) -> dict:
    out: dict = {}
    if "source_s3_object" in value:
        import aws_sdk_groundstation.types.s3_object

        out["sourceS3Object"] = aws_sdk_groundstation.types.s3_object.serialize_json(
            value["source_s3_object"]
        )
    if "ephemeris_data" in value:
        out["ephemerisData"] = value["ephemeris_data"]
    return out


def deserialize_json(data: dict) -> EphemerisDescription:
    out: EphemerisDescription = {}  # type: ignore[typeddict-item]
    if "sourceS3Object" in data:
        import aws_sdk_groundstation.types.s3_object

        out["source_s3_object"] = (
            aws_sdk_groundstation.types.s3_object.deserialize_json(
                data["sourceS3Object"]
            )
        )
    if "ephemerisData" in data:
        out["ephemeris_data"] = data["ephemerisData"]
    return out
