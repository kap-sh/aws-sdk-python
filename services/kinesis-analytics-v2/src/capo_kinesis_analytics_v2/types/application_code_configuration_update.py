"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ApplicationCodeConfigurationUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.code_content_type
    import capo_kinesis_analytics_v2.types.code_content_update


class ApplicationCodeConfigurationUpdate(TypedDict, closed=True):
    code_content_type_update: NotRequired[
        "capo_kinesis_analytics_v2.types.code_content_type.CodeContentType"
    ]
    """<p>Describes updates to the code content type.</p>"""
    code_content_update: NotRequired[
        "capo_kinesis_analytics_v2.types.code_content_update.CodeContentUpdate"
    ]
    """<p>Describes updates to the code content of an application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationCodeConfigurationUpdate) -> dict:
    out: dict = {}
    if "code_content_type_update" in value:
        import capo_kinesis_analytics_v2.types.code_content_type

        out["CodeContentTypeUpdate"] = (
            capo_kinesis_analytics_v2.types.code_content_type.serialize_aws_json_1_1(
                value["code_content_type_update"]
            )
        )
    if "code_content_update" in value:
        import capo_kinesis_analytics_v2.types.code_content_update

        out["CodeContentUpdate"] = (
            capo_kinesis_analytics_v2.types.code_content_update.serialize_aws_json_1_1(
                value["code_content_update"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ApplicationCodeConfigurationUpdate:
    out: ApplicationCodeConfigurationUpdate = {}  # type: ignore[typeddict-item]
    if "CodeContentTypeUpdate" in data:
        import capo_kinesis_analytics_v2.types.code_content_type

        out["code_content_type_update"] = (
            capo_kinesis_analytics_v2.types.code_content_type.deserialize_aws_json_1_1(
                data["CodeContentTypeUpdate"]
            )
        )
    if "CodeContentUpdate" in data:
        import capo_kinesis_analytics_v2.types.code_content_update

        out["code_content_update"] = (
            capo_kinesis_analytics_v2.types.code_content_update.deserialize_aws_json_1_1(
                data["CodeContentUpdate"]
            )
        )
    return out
