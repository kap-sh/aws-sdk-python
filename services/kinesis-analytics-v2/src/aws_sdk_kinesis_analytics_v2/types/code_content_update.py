"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#CodeContentUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.s3_content_location_update
    import aws_sdk_kinesis_analytics_v2.types.text_content
    import aws_sdk_kinesis_analytics_v2.types.zip_file_content


class CodeContentUpdate(TypedDict, closed=True):
    text_content_update: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.text_content.TextContent"
    ]
    """<p>Describes an update to the text code for an application.</p>"""
    zip_file_content_update: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.zip_file_content.ZipFileContent"
    ]
    """<p>Describes an update to the zipped code for an application.</p>"""
    s3_content_location_update: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.s3_content_location_update.S3ContentLocationUpdate"
    ]
    """<p>Describes an update to the location of code for an application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CodeContentUpdate) -> dict:
    out: dict = {}
    if "text_content_update" in value:
        out["TextContentUpdate"] = value["text_content_update"]
    if "zip_file_content_update" in value:
        import aws_sdk_kinesis_analytics_v2.types.zip_file_content

        out["ZipFileContentUpdate"] = (
            aws_sdk_kinesis_analytics_v2.types.zip_file_content.serialize_aws_json_1_1(
                value["zip_file_content_update"]
            )
        )
    if "s3_content_location_update" in value:
        import aws_sdk_kinesis_analytics_v2.types.s3_content_location_update

        out["S3ContentLocationUpdate"] = (
            aws_sdk_kinesis_analytics_v2.types.s3_content_location_update.serialize_aws_json_1_1(
                value["s3_content_location_update"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CodeContentUpdate:
    out: CodeContentUpdate = {}  # type: ignore[typeddict-item]
    if "TextContentUpdate" in data:
        out["text_content_update"] = data["TextContentUpdate"]
    if "ZipFileContentUpdate" in data:
        import aws_sdk_kinesis_analytics_v2.types.zip_file_content

        out["zip_file_content_update"] = (
            aws_sdk_kinesis_analytics_v2.types.zip_file_content.deserialize_aws_json_1_1(
                data["ZipFileContentUpdate"]
            )
        )
    if "S3ContentLocationUpdate" in data:
        import aws_sdk_kinesis_analytics_v2.types.s3_content_location_update

        out["s3_content_location_update"] = (
            aws_sdk_kinesis_analytics_v2.types.s3_content_location_update.deserialize_aws_json_1_1(
                data["S3ContentLocationUpdate"]
            )
        )
    return out
