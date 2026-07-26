"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#AddApplicationInputResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.application_version_id
    import capo_kinesis_analytics_v2.types.input_descriptions
    import capo_kinesis_analytics_v2.types.resource_arn


class AddApplicationInputResponse(TypedDict, closed=True):
    application_arn: NotRequired[
        "capo_kinesis_analytics_v2.types.resource_arn.ResourceARN"
    ]
    """<p>The Amazon Resource Name (ARN) of the application.</p>"""
    application_version_id: NotRequired[
        "capo_kinesis_analytics_v2.types.application_version_id.ApplicationVersionId"
    ]
    """<p>Provides the current application version.</p>"""
    input_descriptions: NotRequired[
        "capo_kinesis_analytics_v2.types.input_descriptions.InputDescriptions"
    ]
    """<p>Describes the application input configuration. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddApplicationInputResponse) -> dict:
    out: dict = {}
    if "application_arn" in value:
        out["ApplicationARN"] = value["application_arn"]
    if "application_version_id" in value:
        out["ApplicationVersionId"] = value["application_version_id"]
    if "input_descriptions" in value:
        import capo_kinesis_analytics_v2.types.input_descriptions

        out["InputDescriptions"] = (
            capo_kinesis_analytics_v2.types.input_descriptions.serialize_aws_json_1_1(
                value["input_descriptions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AddApplicationInputResponse:
    out: AddApplicationInputResponse = {}  # type: ignore[typeddict-item]
    if "ApplicationARN" in data:
        out["application_arn"] = data["ApplicationARN"]
    if "ApplicationVersionId" in data:
        out["application_version_id"] = data["ApplicationVersionId"]
    if "InputDescriptions" in data:
        import capo_kinesis_analytics_v2.types.input_descriptions

        out["input_descriptions"] = (
            capo_kinesis_analytics_v2.types.input_descriptions.deserialize_aws_json_1_1(
                data["InputDescriptions"]
            )
        )
    return out
