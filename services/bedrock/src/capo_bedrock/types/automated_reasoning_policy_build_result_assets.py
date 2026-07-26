"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyBuildResultAssets``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_build_log
    import capo_bedrock.types.automated_reasoning_policy_build_result_asset_manifest
    import capo_bedrock.types.automated_reasoning_policy_definition
    import capo_bedrock.types.automated_reasoning_policy_definition_quality_report
    import capo_bedrock.types.automated_reasoning_policy_fidelity_report
    import capo_bedrock.types.automated_reasoning_policy_generated_test_cases
    import capo_bedrock.types.automated_reasoning_policy_scenarios
    import capo_bedrock.types.automated_reasoning_policy_source_document


class _AutomatedReasoningPolicyBuildResultAssets_policyDefinition(
    TypedDict, closed=True
):
    policyDefinition: "capo_bedrock.types.automated_reasoning_policy_definition.AutomatedReasoningPolicyDefinition"


class _AutomatedReasoningPolicyBuildResultAssets_qualityReport(TypedDict, closed=True):
    qualityReport: "capo_bedrock.types.automated_reasoning_policy_definition_quality_report.AutomatedReasoningPolicyDefinitionQualityReport"


class _AutomatedReasoningPolicyBuildResultAssets_buildLog(TypedDict, closed=True):
    buildLog: "capo_bedrock.types.automated_reasoning_policy_build_log.AutomatedReasoningPolicyBuildLog"


class _AutomatedReasoningPolicyBuildResultAssets_generatedTestCases(
    TypedDict, closed=True
):
    generatedTestCases: "capo_bedrock.types.automated_reasoning_policy_generated_test_cases.AutomatedReasoningPolicyGeneratedTestCases"


class _AutomatedReasoningPolicyBuildResultAssets_policyScenarios(
    TypedDict, closed=True
):
    policyScenarios: "capo_bedrock.types.automated_reasoning_policy_scenarios.AutomatedReasoningPolicyScenarios"


class _AutomatedReasoningPolicyBuildResultAssets_assetManifest(TypedDict, closed=True):
    assetManifest: "capo_bedrock.types.automated_reasoning_policy_build_result_asset_manifest.AutomatedReasoningPolicyBuildResultAssetManifest"


class _AutomatedReasoningPolicyBuildResultAssets_document(TypedDict, closed=True):
    document: "capo_bedrock.types.automated_reasoning_policy_source_document.AutomatedReasoningPolicySourceDocument"


class _AutomatedReasoningPolicyBuildResultAssets_fidelityReport(TypedDict, closed=True):
    fidelityReport: "capo_bedrock.types.automated_reasoning_policy_fidelity_report.AutomatedReasoningPolicyFidelityReport"


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
        import capo_bedrock.types.automated_reasoning_policy_definition

        return {
            "policyDefinition": capo_bedrock.types.automated_reasoning_policy_definition.serialize_json(
                value["policyDefinition"]
            )
        }
    elif "qualityReport" in value:
        import capo_bedrock.types.automated_reasoning_policy_definition_quality_report

        return {
            "qualityReport": capo_bedrock.types.automated_reasoning_policy_definition_quality_report.serialize_json(
                value["qualityReport"]
            )
        }
    elif "buildLog" in value:
        import capo_bedrock.types.automated_reasoning_policy_build_log

        return {
            "buildLog": capo_bedrock.types.automated_reasoning_policy_build_log.serialize_json(
                value["buildLog"]
            )
        }
    elif "generatedTestCases" in value:
        import capo_bedrock.types.automated_reasoning_policy_generated_test_cases

        return {
            "generatedTestCases": capo_bedrock.types.automated_reasoning_policy_generated_test_cases.serialize_json(
                value["generatedTestCases"]
            )
        }
    elif "policyScenarios" in value:
        import capo_bedrock.types.automated_reasoning_policy_scenarios

        return {
            "policyScenarios": capo_bedrock.types.automated_reasoning_policy_scenarios.serialize_json(
                value["policyScenarios"]
            )
        }
    elif "assetManifest" in value:
        import capo_bedrock.types.automated_reasoning_policy_build_result_asset_manifest

        return {
            "assetManifest": capo_bedrock.types.automated_reasoning_policy_build_result_asset_manifest.serialize_json(
                value["assetManifest"]
            )
        }
    elif "document" in value:
        import capo_bedrock.types.automated_reasoning_policy_source_document

        return {
            "document": capo_bedrock.types.automated_reasoning_policy_source_document.serialize_json(
                value["document"]
            )
        }
    elif "fidelityReport" in value:
        import capo_bedrock.types.automated_reasoning_policy_fidelity_report

        return {
            "fidelityReport": capo_bedrock.types.automated_reasoning_policy_fidelity_report.serialize_json(
                value["fidelityReport"]
            )
        }
    else:
        raise SerializationError(
            "AutomatedReasoningPolicyBuildResultAssets: no variant present"
        )


def deserialize_json(data: dict) -> AutomatedReasoningPolicyBuildResultAssets:
    if "policyDefinition" in data:
        import capo_bedrock.types.automated_reasoning_policy_definition

        return {
            "policyDefinition": capo_bedrock.types.automated_reasoning_policy_definition.deserialize_json(
                data["policyDefinition"]
            )
        }
    elif "qualityReport" in data:
        import capo_bedrock.types.automated_reasoning_policy_definition_quality_report

        return {
            "qualityReport": capo_bedrock.types.automated_reasoning_policy_definition_quality_report.deserialize_json(
                data["qualityReport"]
            )
        }
    elif "buildLog" in data:
        import capo_bedrock.types.automated_reasoning_policy_build_log

        return {
            "buildLog": capo_bedrock.types.automated_reasoning_policy_build_log.deserialize_json(
                data["buildLog"]
            )
        }
    elif "generatedTestCases" in data:
        import capo_bedrock.types.automated_reasoning_policy_generated_test_cases

        return {
            "generatedTestCases": capo_bedrock.types.automated_reasoning_policy_generated_test_cases.deserialize_json(
                data["generatedTestCases"]
            )
        }
    elif "policyScenarios" in data:
        import capo_bedrock.types.automated_reasoning_policy_scenarios

        return {
            "policyScenarios": capo_bedrock.types.automated_reasoning_policy_scenarios.deserialize_json(
                data["policyScenarios"]
            )
        }
    elif "assetManifest" in data:
        import capo_bedrock.types.automated_reasoning_policy_build_result_asset_manifest

        return {
            "assetManifest": capo_bedrock.types.automated_reasoning_policy_build_result_asset_manifest.deserialize_json(
                data["assetManifest"]
            )
        }
    elif "document" in data:
        import capo_bedrock.types.automated_reasoning_policy_source_document

        return {
            "document": capo_bedrock.types.automated_reasoning_policy_source_document.deserialize_json(
                data["document"]
            )
        }
    elif "fidelityReport" in data:
        import capo_bedrock.types.automated_reasoning_policy_fidelity_report

        return {
            "fidelityReport": capo_bedrock.types.automated_reasoning_policy_fidelity_report.deserialize_json(
                data["fidelityReport"]
            )
        }
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyBuildResultAssets: no recognized variant key"
        )
