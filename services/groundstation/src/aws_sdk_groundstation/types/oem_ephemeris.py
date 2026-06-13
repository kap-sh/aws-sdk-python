"""Generated from Smithy shape ``com.amazonaws.groundstation#OEMEphemeris``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.s3_object
    import aws_sdk_groundstation.types.unbounded_string


class OEMEphemeris(TypedDict):
    s3_object: NotRequired["aws_sdk_groundstation.types.s3_object.S3Object"]
    """<p>The Amazon S3 object that contains the ephemeris data.</p>"""
    oem_data: NotRequired[
        "aws_sdk_groundstation.types.unbounded_string.UnboundedString"
    ]
    """<p>OEM data that you provide directly instead of using an Amazon S3 object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OEMEphemeris) -> dict:
    out: dict = {}
    if "s3_object" in value:
        import aws_sdk_groundstation.types.s3_object

        out["s3Object"] = aws_sdk_groundstation.types.s3_object.serialize_json(
            value["s3_object"]
        )
    if "oem_data" in value:
        out["oemData"] = value["oem_data"]
    return out


def deserialize_json(data: dict) -> OEMEphemeris:
    out: OEMEphemeris = {}  # type: ignore[typeddict-item]
    if "s3Object" in data:
        import aws_sdk_groundstation.types.s3_object

        out["s3_object"] = aws_sdk_groundstation.types.s3_object.deserialize_json(
            data["s3Object"]
        )
    if "oemData" in data:
        out["oem_data"] = data["oemData"]
    return out
