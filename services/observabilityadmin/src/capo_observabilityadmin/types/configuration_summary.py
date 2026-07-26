"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#ConfigurationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.data_sources
    import capo_observabilityadmin.types.processors
    import capo_observabilityadmin.types.sinks
    import capo_observabilityadmin.types.sources


class ConfigurationSummary(TypedDict, closed=True):
    sources: NotRequired["capo_observabilityadmin.types.sources.Sources"]
    """<p>The list of data sources configured in the pipeline.</p>"""
    data_sources: NotRequired["capo_observabilityadmin.types.data_sources.DataSources"]
    """<p>The list of data sources that provide telemetry data to the pipeline.</p>"""
    processors: NotRequired["capo_observabilityadmin.types.processors.Processors"]
    """<p>The list of processors configured in the pipeline for data transformation.</p>"""
    processor_count: NotRequired["int"]
    """<p>The total number of processors configured in the pipeline.</p>"""
    sinks: NotRequired["capo_observabilityadmin.types.sinks.Sinks"]
    """<p>The list of destinations where processed data is sent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationSummary) -> dict:
    out: dict = {}
    if "sources" in value:
        import capo_observabilityadmin.types.sources

        out["Sources"] = capo_observabilityadmin.types.sources.serialize_json(
            value["sources"]
        )
    if "data_sources" in value:
        import capo_observabilityadmin.types.data_sources

        out["DataSources"] = capo_observabilityadmin.types.data_sources.serialize_json(
            value["data_sources"]
        )
    if "processors" in value:
        import capo_observabilityadmin.types.processors

        out["Processors"] = capo_observabilityadmin.types.processors.serialize_json(
            value["processors"]
        )
    if "processor_count" in value:
        out["ProcessorCount"] = value["processor_count"]
    if "sinks" in value:
        import capo_observabilityadmin.types.sinks

        out["Sinks"] = capo_observabilityadmin.types.sinks.serialize_json(
            value["sinks"]
        )
    return out


def deserialize_json(data: dict) -> ConfigurationSummary:
    out: ConfigurationSummary = {}  # type: ignore[typeddict-item]
    if "Sources" in data:
        import capo_observabilityadmin.types.sources

        out["sources"] = capo_observabilityadmin.types.sources.deserialize_json(
            data["Sources"]
        )
    if "DataSources" in data:
        import capo_observabilityadmin.types.data_sources

        out["data_sources"] = (
            capo_observabilityadmin.types.data_sources.deserialize_json(
                data["DataSources"]
            )
        )
    if "Processors" in data:
        import capo_observabilityadmin.types.processors

        out["processors"] = capo_observabilityadmin.types.processors.deserialize_json(
            data["Processors"]
        )
    if "ProcessorCount" in data:
        out["processor_count"] = data["ProcessorCount"]
    if "Sinks" in data:
        import capo_observabilityadmin.types.sinks

        out["sinks"] = capo_observabilityadmin.types.sinks.deserialize_json(
            data["Sinks"]
        )
    return out
