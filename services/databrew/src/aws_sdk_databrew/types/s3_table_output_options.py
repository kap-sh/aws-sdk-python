"""Generated from Smithy shape ``com.amazonaws.databrew#S3TableOutputOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_databrew.types.s3_location


class S3TableOutputOptions(TypedDict, closed=True):
    location: "aws_sdk_databrew.types.s3_location.S3Location"
    """<p>Represents an Amazon S3 location (bucket name and object key) where DataBrew can write output from a job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3TableOutputOptions) -> dict:
    out: dict = {}
    import aws_sdk_databrew.types.s3_location

    out["Location"] = aws_sdk_databrew.types.s3_location.serialize_json(
        value["location"]
    )
    return out


def deserialize_json(data: dict) -> S3TableOutputOptions:
    out: S3TableOutputOptions = {}  # type: ignore[typeddict-item]
    if "Location" in data:
        import aws_sdk_databrew.types.s3_location

        out["location"] = aws_sdk_databrew.types.s3_location.deserialize_json(
            data["Location"]
        )
    else:
        raise DeserializationError("S3TableOutputOptions.location required")
    return out
