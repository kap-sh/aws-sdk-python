"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#MagneticStoreRejectedDataLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_timestream_write.types.s3_configuration


class MagneticStoreRejectedDataLocation(TypedDict, closed=True):
    s3_configuration: NotRequired[
        "aws_sdk_timestream_write.types.s3_configuration.S3Configuration"
    ]
    """<p>Configuration of an S3 location to write error reports for records rejected, asynchronously, during magnetic store writes.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MagneticStoreRejectedDataLocation) -> dict:
    out: dict = {}
    if "s3_configuration" in value:
        import aws_sdk_timestream_write.types.s3_configuration

        out["S3Configuration"] = (
            aws_sdk_timestream_write.types.s3_configuration.serialize_aws_json_1_0(
                value["s3_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> MagneticStoreRejectedDataLocation:
    out: MagneticStoreRejectedDataLocation = {}  # type: ignore[typeddict-item]
    if "S3Configuration" in data:
        import aws_sdk_timestream_write.types.s3_configuration

        out["s3_configuration"] = (
            aws_sdk_timestream_write.types.s3_configuration.deserialize_aws_json_1_0(
                data["S3Configuration"]
            )
        )
    return out
