"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#CentralizationRuleDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_observabilityadmin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.account_identifier
    import aws_sdk_observabilityadmin.types.destination_logs_configuration
    import aws_sdk_observabilityadmin.types.destination_metrics_configuration
    import aws_sdk_observabilityadmin.types.region


class CentralizationRuleDestination(TypedDict, closed=True):
    region: "aws_sdk_observabilityadmin.types.region.Region"
    """<p>The primary destination region to which telemetry data should be centralized.</p>"""
    account: NotRequired[
        "aws_sdk_observabilityadmin.types.account_identifier.AccountIdentifier"
    ]
    """<p>The destination account (within the organization) to which the telemetry data should be centralized.</p>"""
    destination_logs_configuration: NotRequired[
        "aws_sdk_observabilityadmin.types.destination_logs_configuration.DestinationLogsConfiguration"
    ]
    """<p>Log specific configuration for centralization destination log groups.</p>"""
    destination_metrics_configuration: NotRequired[
        "aws_sdk_observabilityadmin.types.destination_metrics_configuration.DestinationMetricsConfiguration"
    ]
    """<p>Metric specific configuration for centralization destination metrics.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CentralizationRuleDestination) -> dict:
    out: dict = {}
    out["Region"] = value["region"]
    if "account" in value:
        out["Account"] = value["account"]
    if "destination_logs_configuration" in value:
        import aws_sdk_observabilityadmin.types.destination_logs_configuration

        out["DestinationLogsConfiguration"] = (
            aws_sdk_observabilityadmin.types.destination_logs_configuration.serialize_json(
                value["destination_logs_configuration"]
            )
        )
    if "destination_metrics_configuration" in value:
        import aws_sdk_observabilityadmin.types.destination_metrics_configuration

        out["DestinationMetricsConfiguration"] = (
            aws_sdk_observabilityadmin.types.destination_metrics_configuration.serialize_json(
                value["destination_metrics_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CentralizationRuleDestination:
    out: CentralizationRuleDestination = {}  # type: ignore[typeddict-item]
    if "Region" in data:
        out["region"] = data["Region"]
    else:
        raise DeserializationError("CentralizationRuleDestination.region required")
    if "Account" in data:
        out["account"] = data["Account"]
    if "DestinationLogsConfiguration" in data:
        import aws_sdk_observabilityadmin.types.destination_logs_configuration

        out["destination_logs_configuration"] = (
            aws_sdk_observabilityadmin.types.destination_logs_configuration.deserialize_json(
                data["DestinationLogsConfiguration"]
            )
        )
    if "DestinationMetricsConfiguration" in data:
        import aws_sdk_observabilityadmin.types.destination_metrics_configuration

        out["destination_metrics_configuration"] = (
            aws_sdk_observabilityadmin.types.destination_metrics_configuration.deserialize_json(
                data["DestinationMetricsConfiguration"]
            )
        )
    return out
