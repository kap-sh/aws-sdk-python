"""Generated from Smithy shape ``com.amazonaws.iot#Sbom``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.s3_location


class Sbom(TypedDict):
    s3_location: NotRequired["aws_sdk_iot.types.s3_location.S3Location"]


# --- restJson1 ser/de ---
def serialize_json(value: Sbom) -> dict:
    out: dict = {}
    if "s3_location" in value:
        import aws_sdk_iot.types.s3_location

        out["s3Location"] = aws_sdk_iot.types.s3_location.serialize_json(
            value["s3_location"]
        )
    return out


def deserialize_json(data: dict) -> Sbom:
    out: Sbom = {}  # type: ignore[typeddict-item]
    if "s3Location" in data:
        import aws_sdk_iot.types.s3_location

        out["s3_location"] = aws_sdk_iot.types.s3_location.deserialize_json(
            data["s3Location"]
        )
    return out
