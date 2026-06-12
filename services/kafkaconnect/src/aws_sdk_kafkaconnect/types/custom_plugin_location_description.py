"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#CustomPluginLocationDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.s3_location_description


class CustomPluginLocationDescription(TypedDict):
    s3_location: NotRequired[
        "aws_sdk_kafkaconnect.types.s3_location_description.S3LocationDescription"
    ]
    """<p>The S3 bucket Amazon Resource Name (ARN), file key, and object version of the plugin file stored in Amazon S3.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomPluginLocationDescription) -> dict:
    out: dict = {}
    if "s3_location" in value:
        import aws_sdk_kafkaconnect.types.s3_location_description

        out["s3Location"] = (
            aws_sdk_kafkaconnect.types.s3_location_description.serialize_json(
                value["s3_location"]
            )
        )
    return out


def deserialize_json(data: dict) -> CustomPluginLocationDescription:
    out: CustomPluginLocationDescription = {}  # type: ignore[typeddict-item]
    if "s3Location" in data:
        import aws_sdk_kafkaconnect.types.s3_location_description

        out["s3_location"] = (
            aws_sdk_kafkaconnect.types.s3_location_description.deserialize_json(
                data["s3Location"]
            )
        )
    return out
