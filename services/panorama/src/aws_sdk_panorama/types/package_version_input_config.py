"""Generated from Smithy shape ``com.amazonaws.panorama#PackageVersionInputConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_panorama.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_panorama.types.s3_location


class PackageVersionInputConfig(TypedDict, closed=True):
    s3_location: "aws_sdk_panorama.types.s3_location.S3Location"
    """<p>A location in Amazon S3.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PackageVersionInputConfig) -> dict:
    out: dict = {}
    import aws_sdk_panorama.types.s3_location

    out["S3Location"] = aws_sdk_panorama.types.s3_location.serialize_json(
        value["s3_location"]
    )
    return out


def deserialize_json(data: dict) -> PackageVersionInputConfig:
    out: PackageVersionInputConfig = {}  # type: ignore[typeddict-item]
    if "S3Location" in data:
        import aws_sdk_panorama.types.s3_location

        out["s3_location"] = aws_sdk_panorama.types.s3_location.deserialize_json(
            data["S3Location"]
        )
    else:
        raise DeserializationError("PackageVersionInputConfig.s3_location required")
    return out
