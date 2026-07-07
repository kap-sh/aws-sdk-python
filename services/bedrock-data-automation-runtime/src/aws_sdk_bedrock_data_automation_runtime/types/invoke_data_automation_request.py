"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomationruntime#InvokeDataAutomationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_data_automation_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation_runtime.types.blueprint_list
    import aws_sdk_bedrock_data_automation_runtime.types.data_automation_configuration
    import aws_sdk_bedrock_data_automation_runtime.types.data_automation_profile_arn
    import aws_sdk_bedrock_data_automation_runtime.types.encryption_configuration
    import aws_sdk_bedrock_data_automation_runtime.types.output_configuration
    import aws_sdk_bedrock_data_automation_runtime.types.sync_input_configuration


class InvokeDataAutomationRequest(TypedDict, closed=True):
    input_configuration: "aws_sdk_bedrock_data_automation_runtime.types.sync_input_configuration.SyncInputConfiguration"
    """Input configuration."""
    data_automation_configuration: NotRequired[
        "aws_sdk_bedrock_data_automation_runtime.types.data_automation_configuration.DataAutomationConfiguration"
    ]
    """Data automation configuration."""
    blueprints: NotRequired[
        "aws_sdk_bedrock_data_automation_runtime.types.blueprint_list.BlueprintList"
    ]
    """Blueprint list."""
    data_automation_profile_arn: "aws_sdk_bedrock_data_automation_runtime.types.data_automation_profile_arn.DataAutomationProfileArn"
    """Data automation profile ARN"""
    encryption_configuration: NotRequired[
        "aws_sdk_bedrock_data_automation_runtime.types.encryption_configuration.EncryptionConfiguration"
    ]
    """Encryption configuration."""
    output_configuration: NotRequired[
        "aws_sdk_bedrock_data_automation_runtime.types.output_configuration.OutputConfiguration"
    ]
    """Output configuration."""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvokeDataAutomationRequest) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_data_automation_runtime.types.sync_input_configuration

    out["inputConfiguration"] = (
        aws_sdk_bedrock_data_automation_runtime.types.sync_input_configuration.serialize_aws_json_1_1(
            value["input_configuration"]
        )
    )
    if "data_automation_configuration" in value:
        import aws_sdk_bedrock_data_automation_runtime.types.data_automation_configuration

        out["dataAutomationConfiguration"] = (
            aws_sdk_bedrock_data_automation_runtime.types.data_automation_configuration.serialize_aws_json_1_1(
                value["data_automation_configuration"]
            )
        )
    if "blueprints" in value:
        import aws_sdk_bedrock_data_automation_runtime.types.blueprint_list

        out["blueprints"] = (
            aws_sdk_bedrock_data_automation_runtime.types.blueprint_list.serialize_aws_json_1_1(
                value["blueprints"]
            )
        )
    out["dataAutomationProfileArn"] = value["data_automation_profile_arn"]
    if "encryption_configuration" in value:
        import aws_sdk_bedrock_data_automation_runtime.types.encryption_configuration

        out["encryptionConfiguration"] = (
            aws_sdk_bedrock_data_automation_runtime.types.encryption_configuration.serialize_aws_json_1_1(
                value["encryption_configuration"]
            )
        )
    if "output_configuration" in value:
        import aws_sdk_bedrock_data_automation_runtime.types.output_configuration

        out["outputConfiguration"] = (
            aws_sdk_bedrock_data_automation_runtime.types.output_configuration.serialize_aws_json_1_1(
                value["output_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InvokeDataAutomationRequest:
    out: InvokeDataAutomationRequest = {}  # type: ignore[typeddict-item]
    if "inputConfiguration" in data:
        import aws_sdk_bedrock_data_automation_runtime.types.sync_input_configuration

        out["input_configuration"] = (
            aws_sdk_bedrock_data_automation_runtime.types.sync_input_configuration.deserialize_aws_json_1_1(
                data["inputConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "InvokeDataAutomationRequest.input_configuration required"
        )
    if "dataAutomationConfiguration" in data:
        import aws_sdk_bedrock_data_automation_runtime.types.data_automation_configuration

        out["data_automation_configuration"] = (
            aws_sdk_bedrock_data_automation_runtime.types.data_automation_configuration.deserialize_aws_json_1_1(
                data["dataAutomationConfiguration"]
            )
        )
    if "blueprints" in data:
        import aws_sdk_bedrock_data_automation_runtime.types.blueprint_list

        out["blueprints"] = (
            aws_sdk_bedrock_data_automation_runtime.types.blueprint_list.deserialize_aws_json_1_1(
                data["blueprints"]
            )
        )
    if "dataAutomationProfileArn" in data:
        out["data_automation_profile_arn"] = data["dataAutomationProfileArn"]
    else:
        raise DeserializationError(
            "InvokeDataAutomationRequest.data_automation_profile_arn required"
        )
    if "encryptionConfiguration" in data:
        import aws_sdk_bedrock_data_automation_runtime.types.encryption_configuration

        out["encryption_configuration"] = (
            aws_sdk_bedrock_data_automation_runtime.types.encryption_configuration.deserialize_aws_json_1_1(
                data["encryptionConfiguration"]
            )
        )
    if "outputConfiguration" in data:
        import aws_sdk_bedrock_data_automation_runtime.types.output_configuration

        out["output_configuration"] = (
            aws_sdk_bedrock_data_automation_runtime.types.output_configuration.deserialize_aws_json_1_1(
                data["outputConfiguration"]
            )
        )
    return out
