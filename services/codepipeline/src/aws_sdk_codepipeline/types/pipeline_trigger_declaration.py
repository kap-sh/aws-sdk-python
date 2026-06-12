"""Generated from Smithy shape ``com.amazonaws.codepipeline#PipelineTriggerDeclaration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.git_configuration
    import aws_sdk_codepipeline.types.pipeline_trigger_provider_type


class PipelineTriggerDeclaration(TypedDict):
    provider_type: "aws_sdk_codepipeline.types.pipeline_trigger_provider_type.PipelineTriggerProviderType"
    """<p>The source provider for the event, such as connections configured for a repository with Git tags, for the specified trigger configuration.</p>"""
    git_configuration: "aws_sdk_codepipeline.types.git_configuration.GitConfiguration"
    """<p>Provides the filter criteria and the source stage for the repository event that starts the pipeline, such as Git tags.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PipelineTriggerDeclaration) -> dict:
    out: dict = {}
    import aws_sdk_codepipeline.types.pipeline_trigger_provider_type

    out["providerType"] = (
        aws_sdk_codepipeline.types.pipeline_trigger_provider_type.serialize_aws_json_1_1(
            value["provider_type"]
        )
    )
    import aws_sdk_codepipeline.types.git_configuration

    out["gitConfiguration"] = (
        aws_sdk_codepipeline.types.git_configuration.serialize_aws_json_1_1(
            value["git_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PipelineTriggerDeclaration:
    out: PipelineTriggerDeclaration = {}  # type: ignore[typeddict-item]
    if "providerType" in data:
        import aws_sdk_codepipeline.types.pipeline_trigger_provider_type

        out["provider_type"] = (
            aws_sdk_codepipeline.types.pipeline_trigger_provider_type.deserialize_aws_json_1_1(
                data["providerType"]
            )
        )
    else:
        raise DeserializationError("PipelineTriggerDeclaration.provider_type required")
    if "gitConfiguration" in data:
        import aws_sdk_codepipeline.types.git_configuration

        out["git_configuration"] = (
            aws_sdk_codepipeline.types.git_configuration.deserialize_aws_json_1_1(
                data["gitConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "PipelineTriggerDeclaration.git_configuration required"
        )
    return out
