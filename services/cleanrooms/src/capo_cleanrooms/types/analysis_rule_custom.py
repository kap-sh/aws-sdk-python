"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalysisRuleCustom``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.additional_analyses
    import capo_cleanrooms.types.allowed_analyses_list
    import capo_cleanrooms.types.allowed_analysis_provider_list
    import capo_cleanrooms.types.analysis_rule_column_list
    import capo_cleanrooms.types.differential_privacy_configuration


class AnalysisRuleCustom(TypedDict, closed=True):
    allowed_analyses: "capo_cleanrooms.types.allowed_analyses_list.AllowedAnalysesList"
    """<p>The ARN of the analysis templates that are allowed by the custom analysis rule.</p>"""
    allowed_analysis_providers: NotRequired[
        "capo_cleanrooms.types.allowed_analysis_provider_list.AllowedAnalysisProviderList"
    ]
    """<p>The IDs of the Amazon Web Services accounts that are allowed to query by the custom analysis rule. Required when <code>allowedAnalyses</code> is <code>ANY_QUERY</code>.</p>"""
    additional_analyses: NotRequired[
        "capo_cleanrooms.types.additional_analyses.AdditionalAnalyses"
    ]
    """<p> An indicator as to whether additional analyses (such as Clean Rooms ML) can be applied to the output of the direct query.</p>"""
    disallowed_output_columns: NotRequired[
        "capo_cleanrooms.types.analysis_rule_column_list.AnalysisRuleColumnList"
    ]
    """<p> A list of columns that aren't allowed to be shown in the query output.</p>"""
    differential_privacy: NotRequired[
        "capo_cleanrooms.types.differential_privacy_configuration.DifferentialPrivacyConfiguration"
    ]
    """<p>The differential privacy configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisRuleCustom) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.allowed_analyses_list

    out["allowedAnalyses"] = capo_cleanrooms.types.allowed_analyses_list.serialize_json(
        value["allowed_analyses"]
    )
    if "allowed_analysis_providers" in value:
        import capo_cleanrooms.types.allowed_analysis_provider_list

        out["allowedAnalysisProviders"] = (
            capo_cleanrooms.types.allowed_analysis_provider_list.serialize_json(
                value["allowed_analysis_providers"]
            )
        )
    if "additional_analyses" in value:
        import capo_cleanrooms.types.additional_analyses

        out["additionalAnalyses"] = (
            capo_cleanrooms.types.additional_analyses.serialize_json(
                value["additional_analyses"]
            )
        )
    if "disallowed_output_columns" in value:
        import capo_cleanrooms.types.analysis_rule_column_list

        out["disallowedOutputColumns"] = (
            capo_cleanrooms.types.analysis_rule_column_list.serialize_json(
                value["disallowed_output_columns"]
            )
        )
    if "differential_privacy" in value:
        import capo_cleanrooms.types.differential_privacy_configuration

        out["differentialPrivacy"] = (
            capo_cleanrooms.types.differential_privacy_configuration.serialize_json(
                value["differential_privacy"]
            )
        )
    return out


def deserialize_json(data: dict) -> AnalysisRuleCustom:
    out: AnalysisRuleCustom = {}  # type: ignore[typeddict-item]
    if "allowedAnalyses" in data:
        import capo_cleanrooms.types.allowed_analyses_list

        out["allowed_analyses"] = (
            capo_cleanrooms.types.allowed_analyses_list.deserialize_json(
                data["allowedAnalyses"]
            )
        )
    else:
        raise DeserializationError("AnalysisRuleCustom.allowed_analyses required")
    if "allowedAnalysisProviders" in data:
        import capo_cleanrooms.types.allowed_analysis_provider_list

        out["allowed_analysis_providers"] = (
            capo_cleanrooms.types.allowed_analysis_provider_list.deserialize_json(
                data["allowedAnalysisProviders"]
            )
        )
    if "additionalAnalyses" in data:
        import capo_cleanrooms.types.additional_analyses

        out["additional_analyses"] = (
            capo_cleanrooms.types.additional_analyses.deserialize_json(
                data["additionalAnalyses"]
            )
        )
    if "disallowedOutputColumns" in data:
        import capo_cleanrooms.types.analysis_rule_column_list

        out["disallowed_output_columns"] = (
            capo_cleanrooms.types.analysis_rule_column_list.deserialize_json(
                data["disallowedOutputColumns"]
            )
        )
    if "differentialPrivacy" in data:
        import capo_cleanrooms.types.differential_privacy_configuration

        out["differential_privacy"] = (
            capo_cleanrooms.types.differential_privacy_configuration.deserialize_json(
                data["differentialPrivacy"]
            )
        )
    return out
