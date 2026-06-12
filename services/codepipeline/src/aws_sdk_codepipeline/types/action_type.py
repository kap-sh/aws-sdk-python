"""Generated from Smithy shape ``com.amazonaws.codepipeline#ActionType``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.action_configuration_property_list
    import aws_sdk_codepipeline.types.action_type_id
    import aws_sdk_codepipeline.types.action_type_settings
    import aws_sdk_codepipeline.types.artifact_details


class ActionType(TypedDict):
    id: "aws_sdk_codepipeline.types.action_type_id.ActionTypeId"
    """<p>Represents information about an action type.</p>"""
    settings: NotRequired[
        "aws_sdk_codepipeline.types.action_type_settings.ActionTypeSettings"
    ]
    """<p>The settings for the action type.</p>"""
    action_configuration_properties: NotRequired[
        "aws_sdk_codepipeline.types.action_configuration_property_list.ActionConfigurationPropertyList"
    ]
    """<p>The configuration properties for the action type.</p>"""
    input_artifact_details: (
        "aws_sdk_codepipeline.types.artifact_details.ArtifactDetails"
    )
    """<p>The details of the input artifact for the action, such as its commit ID.</p>"""
    output_artifact_details: (
        "aws_sdk_codepipeline.types.artifact_details.ArtifactDetails"
    )
    """<p>The details of the output artifact of the action, such as its commit ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActionType) -> dict:
    out: dict = {}
    import aws_sdk_codepipeline.types.action_type_id

    out["id"] = aws_sdk_codepipeline.types.action_type_id.serialize_aws_json_1_1(
        value["id"]
    )
    if "settings" in value:
        import aws_sdk_codepipeline.types.action_type_settings

        out["settings"] = (
            aws_sdk_codepipeline.types.action_type_settings.serialize_aws_json_1_1(
                value["settings"]
            )
        )
    if "action_configuration_properties" in value:
        import aws_sdk_codepipeline.types.action_configuration_property_list

        out["actionConfigurationProperties"] = (
            aws_sdk_codepipeline.types.action_configuration_property_list.serialize_aws_json_1_1(
                value["action_configuration_properties"]
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
    return out


def deserialize_aws_json_1_1(data: dict) -> ActionType:
    out: ActionType = {}  # type: ignore[typeddict-item]
    if "id" in data:
        import aws_sdk_codepipeline.types.action_type_id

        out["id"] = aws_sdk_codepipeline.types.action_type_id.deserialize_aws_json_1_1(
            data["id"]
        )
    else:
        raise DeserializationError("ActionType.id required")
    if "settings" in data:
        import aws_sdk_codepipeline.types.action_type_settings

        out["settings"] = (
            aws_sdk_codepipeline.types.action_type_settings.deserialize_aws_json_1_1(
                data["settings"]
            )
        )
    if "actionConfigurationProperties" in data:
        import aws_sdk_codepipeline.types.action_configuration_property_list

        out["action_configuration_properties"] = (
            aws_sdk_codepipeline.types.action_configuration_property_list.deserialize_aws_json_1_1(
                data["actionConfigurationProperties"]
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
        raise DeserializationError("ActionType.input_artifact_details required")
    if "outputArtifactDetails" in data:
        import aws_sdk_codepipeline.types.artifact_details

        out["output_artifact_details"] = (
            aws_sdk_codepipeline.types.artifact_details.deserialize_aws_json_1_1(
                data["outputArtifactDetails"]
            )
        )
    else:
        raise DeserializationError("ActionType.output_artifact_details required")
    return out
