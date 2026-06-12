"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ApplicationCodeConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.code_content
    import aws_sdk_kinesis_analytics_v2.types.code_content_type


class ApplicationCodeConfiguration(TypedDict):
    code_content: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.code_content.CodeContent"
    ]
    """<p>The location and type of the application code.</p>"""
    code_content_type: (
        "aws_sdk_kinesis_analytics_v2.types.code_content_type.CodeContentType"
    )
    """<p>Specifies whether the code content is in text or zip format.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationCodeConfiguration) -> dict:
    out: dict = {}
    if "code_content" in value:
        import aws_sdk_kinesis_analytics_v2.types.code_content

        out["CodeContent"] = (
            aws_sdk_kinesis_analytics_v2.types.code_content.serialize_aws_json_1_1(
                value["code_content"]
            )
        )
    import aws_sdk_kinesis_analytics_v2.types.code_content_type

    out["CodeContentType"] = (
        aws_sdk_kinesis_analytics_v2.types.code_content_type.serialize_aws_json_1_1(
            value["code_content_type"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ApplicationCodeConfiguration:
    out: ApplicationCodeConfiguration = {}  # type: ignore[typeddict-item]
    if "CodeContent" in data:
        import aws_sdk_kinesis_analytics_v2.types.code_content

        out["code_content"] = (
            aws_sdk_kinesis_analytics_v2.types.code_content.deserialize_aws_json_1_1(
                data["CodeContent"]
            )
        )
    if "CodeContentType" in data:
        import aws_sdk_kinesis_analytics_v2.types.code_content_type

        out["code_content_type"] = (
            aws_sdk_kinesis_analytics_v2.types.code_content_type.deserialize_aws_json_1_1(
                data["CodeContentType"]
            )
        )
    else:
        raise DeserializationError(
            "ApplicationCodeConfiguration.code_content_type required"
        )
    return out
