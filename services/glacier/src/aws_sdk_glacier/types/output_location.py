"""Generated from Smithy shape ``com.amazonaws.glacier#OutputLocation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glacier.types.s3_location


class OutputLocation(TypedDict):
    s3: NotRequired["aws_sdk_glacier.types.s3_location.S3Location"]
    """<p>Describes an S3 location that will receive the results of the job request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OutputLocation) -> dict:
    out: dict = {}
    if "s3" in value:
        import aws_sdk_glacier.types.s3_location

        out["S3"] = aws_sdk_glacier.types.s3_location.serialize_json(value["s3"])
    return out


def deserialize_json(data: dict) -> OutputLocation:
    out: OutputLocation = {}  # type: ignore[typeddict-item]
    if "S3" in data:
        import aws_sdk_glacier.types.s3_location

        out["s3"] = aws_sdk_glacier.types.s3_location.deserialize_json(data["S3"])
    return out
