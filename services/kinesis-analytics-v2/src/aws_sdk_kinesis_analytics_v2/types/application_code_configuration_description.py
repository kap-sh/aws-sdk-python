"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ApplicationCodeConfigurationDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.code_content_description
    import aws_sdk_kinesis_analytics_v2.types.code_content_type


class ApplicationCodeConfigurationDescription(TypedDict):
    code_content_type: (
        "aws_sdk_kinesis_analytics_v2.types.code_content_type.CodeContentType"
    )
    """<p>Specifies whether the code content is in text or zip format.</p>"""
    code_content_description: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.code_content_description.CodeContentDescription"
    ]
    """<p>Describes details about the location and format of the application code.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationCodeConfigurationDescription) -> dict:
    out: dict = {}
    import aws_sdk_kinesis_analytics_v2.types.code_content_type

    out["CodeContentType"] = (
        aws_sdk_kinesis_analytics_v2.types.code_content_type.serialize_aws_json_1_1(
            value["code_content_type"]
        )
    )
    if "code_content_description" in value:
        import aws_sdk_kinesis_analytics_v2.types.code_content_description

        out["CodeContentDescription"] = (
            aws_sdk_kinesis_analytics_v2.types.code_content_description.serialize_aws_json_1_1(
                value["code_content_description"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ApplicationCodeConfigurationDescription:
    out: ApplicationCodeConfigurationDescription = {}  # type: ignore[typeddict-item]
    if "CodeContentType" in data:
        import aws_sdk_kinesis_analytics_v2.types.code_content_type

        out["code_content_type"] = (
            aws_sdk_kinesis_analytics_v2.types.code_content_type.deserialize_aws_json_1_1(
                data["CodeContentType"]
            )
        )
    else:
        raise DeserializationError(
            "ApplicationCodeConfigurationDescription.code_content_type required"
        )
    if "CodeContentDescription" in data:
        import aws_sdk_kinesis_analytics_v2.types.code_content_description

        out["code_content_description"] = (
            aws_sdk_kinesis_analytics_v2.types.code_content_description.deserialize_aws_json_1_1(
                data["CodeContentDescription"]
            )
        )
    return out
