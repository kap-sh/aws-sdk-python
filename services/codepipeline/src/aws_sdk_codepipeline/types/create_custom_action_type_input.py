"""Generated from Smithy shape ``com.amazonaws.codepipeline#CreateCustomActionTypeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.action_category
    import aws_sdk_codepipeline.types.action_configuration_property_list
    import aws_sdk_codepipeline.types.action_provider
    import aws_sdk_codepipeline.types.action_type_settings
    import aws_sdk_codepipeline.types.artifact_details
    import aws_sdk_codepipeline.types.tag_list
    import aws_sdk_codepipeline.types.version


class CreateCustomActionTypeInput(TypedDict, closed=True):
    category: "aws_sdk_codepipeline.types.action_category.ActionCategory"
    """<p>The category of the custom action, such as a build action or a test action.</p>"""
    provider: "aws_sdk_codepipeline.types.action_provider.ActionProvider"
    """<p>The provider of the service used in the custom action, such as CodeDeploy.</p>"""
    version: "aws_sdk_codepipeline.types.version.Version"
    """<p>The version identifier of the custom action.</p>"""
    settings: NotRequired[
        "aws_sdk_codepipeline.types.action_type_settings.ActionTypeSettings"
    ]
    """<p>URLs that provide users information about this custom action.</p>"""
    configuration_properties: NotRequired[
        "aws_sdk_codepipeline.types.action_configuration_property_list.ActionConfigurationPropertyList"
    ]
    r"""<p>The configuration properties for the custom action.</p> <note> <p>You can refer to a name in the configuration properties of the custom action within the URL templates by following the format of {Config:name}, as long as the configuration property is both required and not secret. For more information, see <a href=\"https://docs.aws.amazon.com/codepipeline/latest/userguide/how-to-create-custom-action.html\">Create a Custom Action for a Pipeline</a>.</p> </note>"""
    input_artifact_details: (
        "aws_sdk_codepipeline.types.artifact_details.ArtifactDetails"
    )
    """<p>The details of the input artifact for the action, such as its commit ID.</p>"""
    output_artifact_details: (
        "aws_sdk_codepipeline.types.artifact_details.ArtifactDetails"
    )
    """<p>The details of the output artifact of the action, such as its commit ID.</p>"""
    tags: NotRequired["aws_sdk_codepipeline.types.tag_list.TagList"]
    """<p>The tags for the custom action.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateCustomActionTypeInput) -> dict:
    out: dict = {}
    import aws_sdk_codepipeline.types.action_category

    out["category"] = aws_sdk_codepipeline.types.action_category.serialize_aws_json_1_1(
        value["category"]
    )
    out["provider"] = value["provider"]
    out["version"] = value["version"]
    if "settings" in value:
        import aws_sdk_codepipeline.types.action_type_settings

        out["settings"] = (
            aws_sdk_codepipeline.types.action_type_settings.serialize_aws_json_1_1(
                value["settings"]
            )
        )
    if "configuration_properties" in value:
        import aws_sdk_codepipeline.types.action_configuration_property_list

        out["configurationProperties"] = (
            aws_sdk_codepipeline.types.action_configuration_property_list.serialize_aws_json_1_1(
                value["configuration_properties"]
            )
        )
    import aws_sdk_codepipeline.types.artifact_details

    out["inputArtifactDetails"] = (
        aws_sdk_codepipeline.types.artifact_details.serialize_aws_json_1_1(
            value["input_artifact_details"]
        )
    )
    import aws_sdk_codepipeline.types.artifact_details

    out["outputArtifactDetails"] = (
        aws_sdk_codepipeline.types.artifact_details.serialize_aws_json_1_1(
            value["output_artifact_details"]
        )
    )
    if "tags" in value:
        import aws_sdk_codepipeline.types.tag_list

        out["tags"] = aws_sdk_codepipeline.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateCustomActionTypeInput:
    out: CreateCustomActionTypeInput = {}  # type: ignore[typeddict-item]
    if "category" in data:
        import aws_sdk_codepipeline.types.action_category

        out["category"] = (
            aws_sdk_codepipeline.types.action_category.deserialize_aws_json_1_1(
                data["category"]
            )
        )
    else:
        raise DeserializationError("CreateCustomActionTypeInput.category required")
    if "provider" in data:
        out["provider"] = data["provider"]
    else:
        raise DeserializationError("CreateCustomActionTypeInput.provider required")
    if "version" in data:
        out["version"] = data["version"]
    else:
        raise DeserializationError("CreateCustomActionTypeInput.version required")
    if "settings" in data:
        import aws_sdk_codepipeline.types.action_type_settings

        out["settings"] = (
            aws_sdk_codepipeline.types.action_type_settings.deserialize_aws_json_1_1(
                data["settings"]
            )
        )
    if "configurationProperties" in data:
        import aws_sdk_codepipeline.types.action_configuration_property_list

        out["configuration_properties"] = (
            aws_sdk_codepipeline.types.action_configuration_property_list.deserialize_aws_json_1_1(
                data["configurationProperties"]
            )
        )
    if "inputArtifactDetails" in data:
        import aws_sdk_codepipeline.types.artifact_details

        out["input_artifact_details"] = (
            aws_sdk_codepipeline.types.artifact_details.deserialize_aws_json_1_1(
                data["inputArtifactDetails"]
            )
        )
    else:
        raise DeserializationError(
            "CreateCustomActionTypeInput.input_artifact_details required"
        )
    if "outputArtifactDetails" in data:
        import aws_sdk_codepipeline.types.artifact_details

        out["output_artifact_details"] = (
            aws_sdk_codepipeline.types.artifact_details.deserialize_aws_json_1_1(
                data["outputArtifactDetails"]
            )
        )
    else:
        raise DeserializationError(
            "CreateCustomActionTypeInput.output_artifact_details required"
        )
    if "tags" in data:
        import aws_sdk_codepipeline.types.tag_list

        out["tags"] = aws_sdk_codepipeline.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
