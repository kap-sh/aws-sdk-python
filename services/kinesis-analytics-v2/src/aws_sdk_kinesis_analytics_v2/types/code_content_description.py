"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#CodeContentDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.code_md5
    import aws_sdk_kinesis_analytics_v2.types.code_size
    import aws_sdk_kinesis_analytics_v2.types.s3_application_code_location_description
    import aws_sdk_kinesis_analytics_v2.types.text_content


class CodeContentDescription(TypedDict, closed=True):
    text_content: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.text_content.TextContent"
    ]
    """<p>The text-format code</p>"""
    code_md5: NotRequired["aws_sdk_kinesis_analytics_v2.types.code_md5.CodeMD5"]
    """<p>The checksum that can be used to validate zip-format code.</p>"""
    code_size: NotRequired["aws_sdk_kinesis_analytics_v2.types.code_size.CodeSize"]
    """<p>The size in bytes of the application code. Can be used to validate zip-format code.</p>"""
    s3_application_code_location_description: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.s3_application_code_location_description.S3ApplicationCodeLocationDescription"
    ]
    """<p>The S3 bucket Amazon Resource Name (ARN), file key, and object version of the application code stored in Amazon S3.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CodeContentDescription) -> dict:
    out: dict = {}
    if "text_content" in value:
        out["TextContent"] = value["text_content"]
    if "code_md5" in value:
        out["CodeMD5"] = value["code_md5"]
    if "code_size" in value:
        out["CodeSize"] = value["code_size"]
    if "s3_application_code_location_description" in value:
        import aws_sdk_kinesis_analytics_v2.types.s3_application_code_location_description

        out["S3ApplicationCodeLocationDescription"] = (
            aws_sdk_kinesis_analytics_v2.types.s3_application_code_location_description.serialize_aws_json_1_1(
                value["s3_application_code_location_description"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CodeContentDescription:
    out: CodeContentDescription = {}  # type: ignore[typeddict-item]
    if "TextContent" in data:
        out["text_content"] = data["TextContent"]
    if "CodeMD5" in data:
        out["code_md5"] = data["CodeMD5"]
    if "CodeSize" in data:
        out["code_size"] = data["CodeSize"]
    if "S3ApplicationCodeLocationDescription" in data:
        import aws_sdk_kinesis_analytics_v2.types.s3_application_code_location_description

        out["s3_application_code_location_description"] = (
            aws_sdk_kinesis_analytics_v2.types.s3_application_code_location_description.deserialize_aws_json_1_1(
                data["S3ApplicationCodeLocationDescription"]
            )
        )
    return out
