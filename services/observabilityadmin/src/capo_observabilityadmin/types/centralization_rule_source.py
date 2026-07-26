"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#CentralizationRuleSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_observabilityadmin.errors import DeserializationError

if TYPE_CHECKING:
    import capo_observabilityadmin.types.regions
    import capo_observabilityadmin.types.source_filter_string
    import capo_observabilityadmin.types.source_logs_configuration
    import capo_observabilityadmin.types.source_metrics_configuration


class CentralizationRuleSource(TypedDict, closed=True):
    regions: "capo_observabilityadmin.types.regions.Regions"
    """<p>The list of source regions from which telemetry data should be centralized.</p>"""
    scope: NotRequired[
        "capo_observabilityadmin.types.source_filter_string.SourceFilterString"
    ]
    """<p>The organizational scope from which telemetry data should be centralized, specified using organization id, accounts or organizational unit ids.</p>"""
    source_logs_configuration: NotRequired[
        "capo_observabilityadmin.types.source_logs_configuration.SourceLogsConfiguration"
    ]
    """<p>Log specific configuration for centralization source log groups.</p>"""
    source_metrics_configuration: NotRequired[
        "capo_observabilityadmin.types.source_metrics_configuration.SourceMetricsConfiguration"
    ]
    """<p>Metric specific configuration for centralization source metrics.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CentralizationRuleSource) -> dict:
    out: dict = {}
    import capo_observabilityadmin.types.regions

    out["Regions"] = capo_observabilityadmin.types.regions.serialize_json(
        value["regions"]
    )
    if "scope" in value:
        out["Scope"] = value["scope"]
    if "source_logs_configuration" in value:
        import capo_observabilityadmin.types.source_logs_configuration

        out["SourceLogsConfiguration"] = (
            capo_observabilityadmin.types.source_logs_configuration.serialize_json(
                value["source_logs_configuration"]
            )
        )
    if "source_metrics_configuration" in value:
        import capo_observabilityadmin.types.source_metrics_configuration

        out["SourceMetricsConfiguration"] = (
            capo_observabilityadmin.types.source_metrics_configuration.serialize_json(
                value["source_metrics_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CentralizationRuleSource:
    out: CentralizationRuleSource = {}  # type: ignore[typeddict-item]
    if "Regions" in data:
        import capo_observabilityadmin.types.regions

        out["regions"] = capo_observabilityadmin.types.regions.deserialize_json(
            data["Regions"]
        )
    else:
        raise DeserializationError("CentralizationRuleSource.regions required")
    if "Scope" in data:
        out["scope"] = data["Scope"]
    if "SourceLogsConfiguration" in data:
        import capo_observabilityadmin.types.source_logs_configuration

        out["source_logs_configuration"] = (
            capo_observabilityadmin.types.source_logs_configuration.deserialize_json(
                data["SourceLogsConfiguration"]
            )
        )
    if "SourceMetricsConfiguration" in data:
        import capo_observabilityadmin.types.source_metrics_configuration

        out["source_metrics_configuration"] = (
            capo_observabilityadmin.types.source_metrics_configuration.deserialize_json(
                data["SourceMetricsConfiguration"]
            )
        )
    return out
