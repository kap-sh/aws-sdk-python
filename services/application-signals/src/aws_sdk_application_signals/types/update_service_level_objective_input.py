"""Generated from Smithy shape ``com.amazonaws.applicationsignals#UpdateServiceLevelObjectiveInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_application_signals.types.burn_rate_configurations
    import aws_sdk_application_signals.types.goal
    import aws_sdk_application_signals.types.request_based_service_level_indicator_config
    import aws_sdk_application_signals.types.service_level_indicator_config
    import aws_sdk_application_signals.types.service_level_objective_description
    import aws_sdk_application_signals.types.service_level_objective_id


class UpdateServiceLevelObjectiveInput(TypedDict, closed=True):
    id: "aws_sdk_application_signals.types.service_level_objective_id.ServiceLevelObjectiveId"
    """<p>The Amazon Resource Name (ARN) or name of the service level objective that you want to update.</p>"""
    description: NotRequired[
        "aws_sdk_application_signals.types.service_level_objective_description.ServiceLevelObjectiveDescription"
    ]
    """<p>An optional description for the SLO.</p>"""
    sli_config: NotRequired[
        "aws_sdk_application_signals.types.service_level_indicator_config.ServiceLevelIndicatorConfig"
    ]
    """<p>If this SLO is a period-based SLO, this structure defines the information about what performance metric this SLO will monitor.</p>"""
    request_based_sli_config: NotRequired[
        "aws_sdk_application_signals.types.request_based_service_level_indicator_config.RequestBasedServiceLevelIndicatorConfig"
    ]
    """<p>If this SLO is a request-based SLO, this structure defines the information about what performance metric this SLO will monitor.</p> <p>You can't specify both <code>SliConfig</code> and <code>RequestBasedSliConfig</code> in the same operation.</p>"""
    goal: NotRequired["aws_sdk_application_signals.types.goal.Goal"]
    """<p>A structure that contains the attributes that determine the goal of the SLO. This includes the time period for evaluation and the attainment threshold.</p>"""
    burn_rate_configurations: NotRequired[
        "aws_sdk_application_signals.types.burn_rate_configurations.BurnRateConfigurations"
    ]
    """<p>Use this array to create <i>burn rates</i> for this SLO. Each burn rate is a metric that indicates how fast the service is consuming the error budget, relative to the attainment goal of the SLO.</p>"""
    auto_investigation_enabled: NotRequired["bool"]
    """Indicates whether DevOps Agent will automatically investigate this SLO when it is breached"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateServiceLevelObjectiveInput) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "sli_config" in value:
        import aws_sdk_application_signals.types.service_level_indicator_config

        out["SliConfig"] = (
            aws_sdk_application_signals.types.service_level_indicator_config.serialize_json(
                value["sli_config"]
            )
        )
    if "request_based_sli_config" in value:
        import aws_sdk_application_signals.types.request_based_service_level_indicator_config

        out["RequestBasedSliConfig"] = (
            aws_sdk_application_signals.types.request_based_service_level_indicator_config.serialize_json(
                value["request_based_sli_config"]
            )
        )
    if "goal" in value:
        import aws_sdk_application_signals.types.goal

        out["Goal"] = aws_sdk_application_signals.types.goal.serialize_json(
            value["goal"]
        )
    if "burn_rate_configurations" in value:
        import aws_sdk_application_signals.types.burn_rate_configurations

        out["BurnRateConfigurations"] = (
            aws_sdk_application_signals.types.burn_rate_configurations.serialize_json(
                value["burn_rate_configurations"]
            )
        )
    if "auto_investigation_enabled" in value:
        out["AutoInvestigationEnabled"] = value["auto_investigation_enabled"]
    return out


def deserialize_json(data: dict) -> UpdateServiceLevelObjectiveInput:
    out: UpdateServiceLevelObjectiveInput = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "SliConfig" in data:
        import aws_sdk_application_signals.types.service_level_indicator_config

        out["sli_config"] = (
            aws_sdk_application_signals.types.service_level_indicator_config.deserialize_json(
                data["SliConfig"]
            )
        )
    if "RequestBasedSliConfig" in data:
        import aws_sdk_application_signals.types.request_based_service_level_indicator_config

        out["request_based_sli_config"] = (
            aws_sdk_application_signals.types.request_based_service_level_indicator_config.deserialize_json(
                data["RequestBasedSliConfig"]
            )
        )
    if "Goal" in data:
        import aws_sdk_application_signals.types.goal

        out["goal"] = aws_sdk_application_signals.types.goal.deserialize_json(
            data["Goal"]
        )
    if "BurnRateConfigurations" in data:
        import aws_sdk_application_signals.types.burn_rate_configurations

        out["burn_rate_configurations"] = (
            aws_sdk_application_signals.types.burn_rate_configurations.deserialize_json(
                data["BurnRateConfigurations"]
            )
        )
    if "AutoInvestigationEnabled" in data:
        out["auto_investigation_enabled"] = data["AutoInvestigationEnabled"]
    return out
