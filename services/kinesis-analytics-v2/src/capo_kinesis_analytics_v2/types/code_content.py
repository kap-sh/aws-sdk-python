"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#CodeContent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.s3_content_location
    import capo_kinesis_analytics_v2.types.text_content
    import capo_kinesis_analytics_v2.types.zip_file_content


class CodeContent(TypedDict, closed=True):
    text_content: NotRequired[
        "capo_kinesis_analytics_v2.types.text_content.TextContent"
    ]
    """<p>The text-format code for a Managed Service for Apache Flink application.</p>"""
    zip_file_content: NotRequired[
        "capo_kinesis_analytics_v2.types.zip_file_content.ZipFileContent"
    ]
    """<p>The zip-format code for a Managed Service for Apache Flink application.</p>"""
    s3_content_location: NotRequired[
        "capo_kinesis_analytics_v2.types.s3_content_location.S3ContentLocation"
    ]
    """<p>Information about the Amazon S3 bucket that contains the application code.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CodeContent) -> dict:
    out: dict = {}
    if "text_content" in value:
        out["TextContent"] = value["text_content"]
    if "zip_file_content" in value:
        import capo_kinesis_analytics_v2.types.zip_file_content

        out["ZipFileContent"] = (
            capo_kinesis_analytics_v2.types.zip_file_content.serialize_aws_json_1_1(
                value["zip_file_content"]
            )
        )
    if "s3_content_location" in value:
        import capo_kinesis_analytics_v2.types.s3_content_location

        out["S3ContentLocation"] = (
            capo_kinesis_analytics_v2.types.s3_content_location.serialize_aws_json_1_1(
                value["s3_content_location"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CodeContent:
    out: CodeContent = {}  # type: ignore[typeddict-item]
    if "TextContent" in data:
        out["text_content"] = data["TextContent"]
    if "ZipFileContent" in data:
        import capo_kinesis_analytics_v2.types.zip_file_content

        out["zip_file_content"] = (
            capo_kinesis_analytics_v2.types.zip_file_content.deserialize_aws_json_1_1(
                data["ZipFileContent"]
            )
        )
    if "S3ContentLocation" in data:
        import capo_kinesis_analytics_v2.types.s3_content_location

        out["s3_content_location"] = (
            capo_kinesis_analytics_v2.types.s3_content_location.deserialize_aws_json_1_1(
                data["S3ContentLocation"]
            )
        )
    return out
