"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyBuildResultAssets``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_build_log
    import aws_sdk_bedrock.types.automated_reasoning_policy_build_result_asset_manifest
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_quality_report
    import aws_sdk_bedrock.types.automated_reasoning_policy_fidelity_report
    import aws_sdk_bedrock.types.automated_reasoning_policy_generated_test_cases
    import aws_sdk_bedrock.types.automated_reasoning_policy_scenarios
    import aws_sdk_bedrock.types.automated_reasoning_policy_source_document


class _AutomatedReasoningPolicyBuildResultAssets_policyDefinition(TypedDict):
    policyDefinition: "aws_sdk_bedrock.types.automated_reasoning_policy_definition.AutomatedReasoningPolicyDefinition"


class _AutomatedReasoningPolicyBuildResultAssets_qualityReport(TypedDict):
    qualityReport: "aws_sdk_bedrock.types.automated_reasoning_policy_definition_quality_report.AutomatedReasoningPolicyDefinitionQualityReport"


class _AutomatedReasoningPolicyBuildResultAssets_buildLog(TypedDict):
    buildLog: "aws_sdk_bedrock.types.automated_reasoning_policy_build_log.AutomatedReasoningPolicyBuildLog"


class _AutomatedReasoningPolicyBuildResultAssets_generatedTestCases(TypedDict):
    generatedTestCases: "aws_sdk_bedrock.types.automated_reasoning_policy_generated_test_cases.AutomatedReasoningPolicyGeneratedTestCases"


class _AutomatedReasoningPolicyBuildResultAssets_policyScenarios(TypedDict):
    policyScenarios: "aws_sdk_bedrock.types.automated_reasoning_policy_scenarios.AutomatedReasoningPolicyScenarios"


class _AutomatedReasoningPolicyBuildResultAssets_assetManifest(TypedDict):
    assetManifest: "aws_sdk_bedrock.types.automated_reasoning_policy_build_result_asset_manifest.AutomatedReasoningPolicyBuildResultAssetManifest"


class _AutomatedReasoningPolicyBuildResultAssets_document(TypedDict):
    document: "aws_sdk_bedrock.types.automated_reasoning_policy_source_document.AutomatedReasoningPolicySourceDocument"


class _AutomatedReasoningPolicyBuildResultAssets_fidelityReport(TypedDict):
    fidelityReport: "aws_sdk_bedrock.types.automated_reasoning_policy_fidelity_report.AutomatedReasoningPolicyFidelityReport"


AutomatedReasoningPolicyBuildResultAssets: TypeAlias = (
    _AutomatedReasoningPolicyBuildResultAssets_policyDefinition
    | _AutomatedReasoningPolicyBuildResultAssets_qualityReport
    | _AutomatedReasoningPolicyBuildResultAssets_buildLog
    | _AutomatedReasoningPolicyBuildResultAssets_generatedTestCases
    | _AutomatedReasoningPolicyBuildResultAssets_policyScenarios
    | _AutomatedReasoningPolicyBuildResultAssets_assetManifest
    | _AutomatedReasoningPolicyBuildResultAssets_document
    | _AutomatedReasoningPolicyBuildResultAssets_fidelityReport
)


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyBuildResultAssets) -> dict:
    if "policyDefinition" in value:
        import aws_sdk_bedrock.types.automated_reasoning_policy_definition

        return {
            "policyDefinition": aws_sdk_bedrock.types.automated_reasoning_policy_definition.serialize_json(
                value["policyDefinition"]
            )
        }
    elif "qualityReport" in value:
        import aws_sdk_bedrock.types.automated_reasoning_policy_definition_quality_report

        return {
            "qualityReport": aws_sdk_bedrock.types.automated_reasoning_policy_definition_quality_report.serialize_json(
                value["qualityReport"]
            )
        }
    elif "buildLog" in value:
        import aws_sdk_bedrock.types.automated_reasoning_policy_build_log

        return {
            "buildLog": aws_sdk_bedrock.types.automated_reasoning_policy_build_log.serialize_json(
                value["buildLog"]
            )
        }
    elif "generatedTestCases" in value:
        import aws_sdk_bedrock.types.automated_reasoning_policy_generated_test_cases

        return {
            "generatedTestCases": aws_sdk_bedrock.types.automated_reasoning_policy_generated_test_cases.serialize_json(
                value["generatedTestCases"]
            )
        }
    elif "policyScenarios" in value:
        import aws_sdk_bedrock.types.automated_reasoning_policy_scenarios

        return {
            "policyScenarios": aws_sdk_bedrock.types.automated_reasoning_policy_scenarios.serialize_json(
                value["policyScenarios"]
            )
        }
    elif "assetManifest" in value:
        import aws_sdk_bedrock.types.automated_reasoning_policy_build_result_asset_manifest

        return {
            "assetManifest": aws_sdk_bedrock.types.automated_reasoning_policy_build_result_asset_manifest.serialize_json(
                value["assetManifest"]
            )
        }
    elif "document" in value:
        import aws_sdk_bedrock.types.automated_reasoning_policy_source_document

        return {
            "document": aws_sdk_bedrock.types.automated_reasoning_policy_source_document.serialize_json(
                value["document"]
            )
        }
    elif "fidelityReport" in value:
        import aws_sdk_bedrock.types.automated_reasoning_policy_fidelity_report

        return {
            "fidelityReport": aws_sdk_bedrock.types.automated_reasoning_policy_fidelity_report.serialize_json(
                value["fidelityReport"]
            )
        }
    else:
        raise SerializationError(
            "AutomatedReasoningPolicyBuildResultAssets: no variant present"
        )


def deserialize_json(data: dict) -> AutomatedReasoningPolicyBuildResultAssets:
    if "policyDefinition" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_definition

        return {
            "policyDefinition": aws_sdk_bedrock.types.automated_reasoning_policy_definition.deserialize_json(
                data["policyDefinition"]
            )
        }
    elif "qualityReport" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_definition_quality_report

        return {
            "qualityReport": aws_sdk_bedrock.types.automated_reasoning_policy_definition_quality_report.deserialize_json(
                data["qualityReport"]
            )
        }
    elif "buildLog" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_build_log

        return {
            "buildLog": aws_sdk_bedrock.types.automated_reasoning_policy_build_log.deserialize_json(
                data["buildLog"]
            )
        }
    elif "generatedTestCases" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_generated_test_cases

        return {
            "generatedTestCases": aws_sdk_bedrock.types.automated_reasoning_policy_generated_test_cases.deserialize_json(
                data["generatedTestCases"]
            )
        }
    elif "policyScenarios" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_scenarios

        return {
            "policyScenarios": aws_sdk_bedrock.types.automated_reasoning_policy_scenarios.deserialize_json(
                data["policyScenarios"]
            )
        }
    elif "assetManifest" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_build_result_asset_manifest

        return {
            "assetManifest": aws_sdk_bedrock.types.automated_reasoning_policy_build_result_asset_manifest.deserialize_json(
                data["assetManifest"]
            )
        }
    elif "document" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_source_document

        return {
            "document": aws_sdk_bedrock.types.automated_reasoning_policy_source_document.deserialize_json(
                data["document"]
            )
        }
    elif "fidelityReport" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_fidelity_report

        return {
            "fidelityReport": aws_sdk_bedrock.types.automated_reasoning_policy_fidelity_report.deserialize_json(
                data["fidelityReport"]
            )
        }
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyBuildResultAssets: no recognized variant key"
        )
