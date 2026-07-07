"""Generated from Smithy shape ``com.amazonaws.codepipeline#RuleType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.artifact_details
    import aws_sdk_codepipeline.types.rule_configuration_property_list
    import aws_sdk_codepipeline.types.rule_type_id
    import aws_sdk_codepipeline.types.rule_type_settings


class RuleType(TypedDict, closed=True):
    id: "aws_sdk_codepipeline.types.rule_type_id.RuleTypeId"
    """<p>Represents information about a rule type.</p>"""
    settings: NotRequired[
        "aws_sdk_codepipeline.types.rule_type_settings.RuleTypeSettings"
    ]
    """<p>Returns information about the settings for a rule type.</p>"""
    rule_configuration_properties: NotRequired[
        "aws_sdk_codepipeline.types.rule_configuration_property_list.RuleConfigurationPropertyList"
    ]
    """<p>The configuration properties for the rule type.</p>"""
    input_artifact_details: (
        "aws_sdk_codepipeline.types.artifact_details.ArtifactDetails"
    )


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleType) -> dict:
    out: dict = {}
    import aws_sdk_codepipeline.types.rule_type_id

    out["id"] = aws_sdk_codepipeline.types.rule_type_id.serialize_aws_json_1_1(
        value["id"]
    )
    if "settings" in value:
        import aws_sdk_codepipeline.types.rule_type_settings

        out["settings"] = (
            aws_sdk_codepipeline.types.rule_type_settings.serialize_aws_json_1_1(
                value["settings"]
            )
        )
    if "rule_configuration_properties" in value:
        import aws_sdk_codepipeline.types.rule_configuration_property_list

        out["ruleConfigurationProperties"] = (
            aws_sdk_codepipeline.types.rule_configuration_property_list.serialize_aws_json_1_1(
                value["rule_configuration_properties"]
            )
        )
    import aws_sdk_codepipeline.types.artifact_details

    out["inputArtifactDetails"] = (
        aws_sdk_codepipeline.types.artifact_details.serialize_aws_json_1_1(
            value["input_artifact_details"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RuleType:
    out: RuleType = {}  # type: ignore[typeddict-item]
    if "id" in data:
        import aws_sdk_codepipeline.types.rule_type_id

        out["id"] = aws_sdk_codepipeline.types.rule_type_id.deserialize_aws_json_1_1(
            data["id"]
        )
    else:
        raise DeserializationError("RuleType.id required")
    if "settings" in data:
        import aws_sdk_codepipeline.types.rule_type_settings

        out["settings"] = (
            aws_sdk_codepipeline.types.rule_type_settings.deserialize_aws_json_1_1(
                data["settings"]
            )
        )
    if "ruleConfigurationProperties" in data:
        import aws_sdk_codepipeline.types.rule_configuration_property_list

        out["rule_configuration_properties"] = (
            aws_sdk_codepipeline.types.rule_configuration_property_list.deserialize_aws_json_1_1(
                data["ruleConfigurationProperties"]
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
        raise DeserializationError("RuleType.input_artifact_details required")
    return out
