"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ConsolidatedPolicyCustom``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.additional_analyses
    import aws_sdk_cleanrooms.types.allowed_additional_analyses
    import aws_sdk_cleanrooms.types.allowed_analyses_list
    import aws_sdk_cleanrooms.types.allowed_analysis_provider_list
    import aws_sdk_cleanrooms.types.allowed_result_receivers
    import aws_sdk_cleanrooms.types.analysis_rule_column_list
    import aws_sdk_cleanrooms.types.differential_privacy_configuration


class ConsolidatedPolicyCustom(TypedDict, closed=True):
    allowed_analyses: (
        "aws_sdk_cleanrooms.types.allowed_analyses_list.AllowedAnalysesList"
    )
    """<p> The allowed analyses.</p>"""
    allowed_analysis_providers: NotRequired[
        "aws_sdk_cleanrooms.types.allowed_analysis_provider_list.AllowedAnalysisProviderList"
    ]
    """<p> The allowed analysis providers.</p>"""
    additional_analyses: NotRequired[
        "aws_sdk_cleanrooms.types.additional_analyses.AdditionalAnalyses"
    ]
    """<p> Additional analyses for the consolidated policy.</p>"""
    disallowed_output_columns: NotRequired[
        "aws_sdk_cleanrooms.types.analysis_rule_column_list.AnalysisRuleColumnList"
    ]
    """<p> Disallowed output columns</p>"""
    differential_privacy: NotRequired[
        "aws_sdk_cleanrooms.types.differential_privacy_configuration.DifferentialPrivacyConfiguration"
    ]
    allowed_result_receivers: NotRequired[
        "aws_sdk_cleanrooms.types.allowed_result_receivers.AllowedResultReceivers"
    ]
    """<p> The allowed result receivers.</p>"""
    allowed_additional_analyses: NotRequired[
        "aws_sdk_cleanrooms.types.allowed_additional_analyses.AllowedAdditionalAnalyses"
    ]
    """<p> The additional analyses allowed by the consolidated policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConsolidatedPolicyCustom) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.allowed_analyses_list

    out["allowedAnalyses"] = (
        aws_sdk_cleanrooms.types.allowed_analyses_list.serialize_json(
            value["allowed_analyses"]
        )
    )
    if "allowed_analysis_providers" in value:
        import aws_sdk_cleanrooms.types.allowed_analysis_provider_list

        out["allowedAnalysisProviders"] = (
            aws_sdk_cleanrooms.types.allowed_analysis_provider_list.serialize_json(
                value["allowed_analysis_providers"]
            )
        )
    if "additional_analyses" in value:
        import aws_sdk_cleanrooms.types.additional_analyses

        out["additionalAnalyses"] = (
            aws_sdk_cleanrooms.types.additional_analyses.serialize_json(
                value["additional_analyses"]
            )
        )
    if "disallowed_output_columns" in value:
        import aws_sdk_cleanrooms.types.analysis_rule_column_list

        out["disallowedOutputColumns"] = (
            aws_sdk_cleanrooms.types.analysis_rule_column_list.serialize_json(
                value["disallowed_output_columns"]
            )
        )
    if "differential_privacy" in value:
        import aws_sdk_cleanrooms.types.differential_privacy_configuration

        out["differentialPrivacy"] = (
            aws_sdk_cleanrooms.types.differential_privacy_configuration.serialize_json(
                value["differential_privacy"]
            )
        )
    if "allowed_result_receivers" in value:
        import aws_sdk_cleanrooms.types.allowed_result_receivers

        out["allowedResultReceivers"] = (
            aws_sdk_cleanrooms.types.allowed_result_receivers.serialize_json(
                value["allowed_result_receivers"]
            )
        )
    if "allowed_additional_analyses" in value:
        import aws_sdk_cleanrooms.types.allowed_additional_analyses

        out["allowedAdditionalAnalyses"] = (
            aws_sdk_cleanrooms.types.allowed_additional_analyses.serialize_json(
                value["allowed_additional_analyses"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConsolidatedPolicyCustom:
    out: ConsolidatedPolicyCustom = {}  # type: ignore[typeddict-item]
    if "allowedAnalyses" in data:
        import aws_sdk_cleanrooms.types.allowed_analyses_list

        out["allowed_analyses"] = (
            aws_sdk_cleanrooms.types.allowed_analyses_list.deserialize_json(
                data["allowedAnalyses"]
            )
        )
    else:
        raise DeserializationError("ConsolidatedPolicyCustom.allowed_analyses required")
    if "allowedAnalysisProviders" in data:
        import aws_sdk_cleanrooms.types.allowed_analysis_provider_list

        out["allowed_analysis_providers"] = (
            aws_sdk_cleanrooms.types.allowed_analysis_provider_list.deserialize_json(
                data["allowedAnalysisProviders"]
            )
        )
    if "additionalAnalyses" in data:
        import aws_sdk_cleanrooms.types.additional_analyses

        out["additional_analyses"] = (
            aws_sdk_cleanrooms.types.additional_analyses.deserialize_json(
                data["additionalAnalyses"]
            )
        )
    if "disallowedOutputColumns" in data:
        import aws_sdk_cleanrooms.types.analysis_rule_column_list

        out["disallowed_output_columns"] = (
            aws_sdk_cleanrooms.types.analysis_rule_column_list.deserialize_json(
                data["disallowedOutputColumns"]
            )
        )
    if "differentialPrivacy" in data:
        import aws_sdk_cleanrooms.types.differential_privacy_configuration

        out["differential_privacy"] = (
            aws_sdk_cleanrooms.types.differential_privacy_configuration.deserialize_json(
                data["differentialPrivacy"]
            )
        )
    if "allowedResultReceivers" in data:
        import aws_sdk_cleanrooms.types.allowed_result_receivers

        out["allowed_result_receivers"] = (
            aws_sdk_cleanrooms.types.allowed_result_receivers.deserialize_json(
                data["allowedResultReceivers"]
            )
        )
    if "allowedAdditionalAnalyses" in data:
        import aws_sdk_cleanrooms.types.allowed_additional_analyses

        out["allowed_additional_analyses"] = (
            aws_sdk_cleanrooms.types.allowed_additional_analyses.deserialize_json(
                data["allowedAdditionalAnalyses"]
            )
        )
    return out
