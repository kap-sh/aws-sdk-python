"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ServiceLevelObjective``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_application_signals.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_application_signals.types.burn_rate_configurations
    import aws_sdk_application_signals.types.evaluation_type
    import aws_sdk_application_signals.types.goal
    import aws_sdk_application_signals.types.metric_source_type
    import aws_sdk_application_signals.types.request_based_service_level_indicator
    import aws_sdk_application_signals.types.service_level_indicator
    import aws_sdk_application_signals.types.service_level_objective_arn
    import aws_sdk_application_signals.types.service_level_objective_description
    import aws_sdk_application_signals.types.service_level_objective_name


class ServiceLevelObjective(TypedDict):
    arn: "aws_sdk_application_signals.types.service_level_objective_arn.ServiceLevelObjectiveArn"
    """<p>The ARN of this SLO.</p>"""
    name: "aws_sdk_application_signals.types.service_level_objective_name.ServiceLevelObjectiveName"
    """<p>The name of this SLO.</p>"""
    description: NotRequired[
        "aws_sdk_application_signals.types.service_level_objective_description.ServiceLevelObjectiveDescription"
    ]
    """<p>The description that you created for this SLO.</p>"""
    created_time: "datetime.datetime"
    """<p>The date and time that this SLO was created. When used in a raw HTTP Query API, it is formatted as <code>yyyy-MM-dd'T'HH:mm:ss</code>. For example, <code>2019-07-01T23:59:59</code>.</p>"""
    last_updated_time: "datetime.datetime"
    """<p>The time that this SLO was most recently updated. When used in a raw HTTP Query API, it is formatted as <code>yyyy-MM-dd'T'HH:mm:ss</code>. For example, <code>2019-07-01T23:59:59</code>.</p>"""
    sli: NotRequired[
        "aws_sdk_application_signals.types.service_level_indicator.ServiceLevelIndicator"
    ]
    """<p>A structure containing information about the performance metric that this SLO monitors, if this is a period-based SLO.</p>"""
    request_based_sli: NotRequired[
        "aws_sdk_application_signals.types.request_based_service_level_indicator.RequestBasedServiceLevelIndicator"
    ]
    """<p>A structure containing information about the performance metric that this SLO monitors, if this is a request-based SLO.</p>"""
    evaluation_type: NotRequired[
        "aws_sdk_application_signals.types.evaluation_type.EvaluationType"
    ]
    """<p>Displays whether this is a period-based SLO or a request-based SLO.</p>"""
    goal: "aws_sdk_application_signals.types.goal.Goal"
    burn_rate_configurations: NotRequired[
        "aws_sdk_application_signals.types.burn_rate_configurations.BurnRateConfigurations"
    ]
    """<p>Each object in this array defines the length of the look-back window used to calculate one burn rate metric for this SLO. The burn rate measures how fast the service is consuming the error budget, relative to the attainment goal of the SLO.</p>"""
    metric_source_type: NotRequired[
        "aws_sdk_application_signals.types.metric_source_type.MetricSourceType"
    ]
    """<p>Displays the SLI metric source type for this SLO. Supported types are:</p> <ul> <li> <p>Service operation</p> </li> <li> <p>Service dependency</p> </li> <li> <p>Service</p> </li> <li> <p>CloudWatch metric</p> </li> <li> <p>AppMonitor</p> </li> <li> <p>Canary</p> </li> </ul>"""
    auto_investigation_enabled: NotRequired["bool"]
    """Indicates whether DevOps Agent will automatically investigate this SLO when it is breached"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceLevelObjective) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    import aws_sdk_application_signals.types._prelude.timestamp

    out["CreatedTime"] = (
        aws_sdk_application_signals.types._prelude.timestamp.serialize_json(
            value["created_time"]
        )
    )
    import aws_sdk_application_signals.types._prelude.timestamp

    out["LastUpdatedTime"] = (
        aws_sdk_application_signals.types._prelude.timestamp.serialize_json(
            value["last_updated_time"]
        )
    )
    if "sli" in value:
        import aws_sdk_application_signals.types.service_level_indicator

        out["Sli"] = (
            aws_sdk_application_signals.types.service_level_indicator.serialize_json(
                value["sli"]
            )
        )
    if "request_based_sli" in value:
        import aws_sdk_application_signals.types.request_based_service_level_indicator

        out["RequestBasedSli"] = (
            aws_sdk_application_signals.types.request_based_service_level_indicator.serialize_json(
                value["request_based_sli"]
            )
        )
    if "evaluation_type" in value:
        import aws_sdk_application_signals.types.evaluation_type

        out["EvaluationType"] = (
            aws_sdk_application_signals.types.evaluation_type.serialize_json(
                value["evaluation_type"]
            )
        )
    import aws_sdk_application_signals.types.goal

    out["Goal"] = aws_sdk_application_signals.types.goal.serialize_json(value["goal"])
    if "burn_rate_configurations" in value:
        import aws_sdk_application_signals.types.burn_rate_configurations

        out["BurnRateConfigurations"] = (
            aws_sdk_application_signals.types.burn_rate_configurations.serialize_json(
                value["burn_rate_configurations"]
            )
        )
    if "metric_source_type" in value:
        import aws_sdk_application_signals.types.metric_source_type

        out["MetricSourceType"] = (
            aws_sdk_application_signals.types.metric_source_type.serialize_json(
                value["metric_source_type"]
            )
        )
    if "auto_investigation_enabled" in value:
        out["AutoInvestigationEnabled"] = value["auto_investigation_enabled"]
    return out


def deserialize_json(data: dict) -> ServiceLevelObjective:
    out: ServiceLevelObjective = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("ServiceLevelObjective.arn required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("ServiceLevelObjective.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "CreatedTime" in data:
        import aws_sdk_application_signals.types._prelude.timestamp

        out["created_time"] = (
            aws_sdk_application_signals.types._prelude.timestamp.deserialize_json(
                data["CreatedTime"]
            )
        )
    else:
        raise DeserializationError("ServiceLevelObjective.created_time required")
    if "LastUpdatedTime" in data:
        import aws_sdk_application_signals.types._prelude.timestamp

        out["last_updated_time"] = (
            aws_sdk_application_signals.types._prelude.timestamp.deserialize_json(
                data["LastUpdatedTime"]
            )
        )
    else:
        raise DeserializationError("ServiceLevelObjective.last_updated_time required")
    if "Sli" in data:
        import aws_sdk_application_signals.types.service_level_indicator

        out["sli"] = (
            aws_sdk_application_signals.types.service_level_indicator.deserialize_json(
                data["Sli"]
            )
        )
    if "RequestBasedSli" in data:
        import aws_sdk_application_signals.types.request_based_service_level_indicator

        out["request_based_sli"] = (
            aws_sdk_application_signals.types.request_based_service_level_indicator.deserialize_json(
                data["RequestBasedSli"]
            )
        )
    if "EvaluationType" in data:
        import aws_sdk_application_signals.types.evaluation_type

        out["evaluation_type"] = (
            aws_sdk_application_signals.types.evaluation_type.deserialize_json(
                data["EvaluationType"]
            )
        )
    if "Goal" in data:
        import aws_sdk_application_signals.types.goal

        out["goal"] = aws_sdk_application_signals.types.goal.deserialize_json(
            data["Goal"]
        )
    else:
        raise DeserializationError("ServiceLevelObjective.goal required")
    if "BurnRateConfigurations" in data:
        import aws_sdk_application_signals.types.burn_rate_configurations

        out["burn_rate_configurations"] = (
            aws_sdk_application_signals.types.burn_rate_configurations.deserialize_json(
                data["BurnRateConfigurations"]
            )
        )
    if "MetricSourceType" in data:
        import aws_sdk_application_signals.types.metric_source_type

        out["metric_source_type"] = (
            aws_sdk_application_signals.types.metric_source_type.deserialize_json(
                data["MetricSourceType"]
            )
        )
    if "AutoInvestigationEnabled" in data:
        out["auto_investigation_enabled"] = data["AutoInvestigationEnabled"]
    return out
