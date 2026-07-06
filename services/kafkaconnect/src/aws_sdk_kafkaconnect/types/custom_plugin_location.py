"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#CustomPluginLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_kafkaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.s3_location


class CustomPluginLocation(TypedDict, closed=True):
    s3_location: "aws_sdk_kafkaconnect.types.s3_location.S3Location"
    """<p>The S3 bucket Amazon Resource Name (ARN), file key, and object version of the plugin file stored in Amazon S3.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomPluginLocation) -> dict:
    out: dict = {}
    import aws_sdk_kafkaconnect.types.s3_location

    out["s3Location"] = aws_sdk_kafkaconnect.types.s3_location.serialize_json(
        value["s3_location"]
    )
    return out


def deserialize_json(data: dict) -> CustomPluginLocation:
    out: CustomPluginLocation = {}  # type: ignore[typeddict-item]
    if "s3Location" in data:
        import aws_sdk_kafkaconnect.types.s3_location

        out["s3_location"] = aws_sdk_kafkaconnect.types.s3_location.deserialize_json(
            data["s3Location"]
        )
    else:
        raise DeserializationError("CustomPluginLocation.s3_location required")
    return out
