"""Generated from Smithy shape ``com.amazonaws.oam#LinkConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_oam.types.log_group_configuration
    import capo_oam.types.metric_configuration


class LinkConfiguration(TypedDict, closed=True):
    log_group_configuration: NotRequired[
        "capo_oam.types.log_group_configuration.LogGroupConfiguration"
    ]
    """<p>Use this structure to filter which log groups are to send log events from the source account to the monitoring account.</p>"""
    metric_configuration: NotRequired[
        "capo_oam.types.metric_configuration.MetricConfiguration"
    ]
    """<p>Use this structure to filter which metric namespaces are to be shared from the source account to the monitoring account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LinkConfiguration) -> dict:
    out: dict = {}
    if "log_group_configuration" in value:
        import capo_oam.types.log_group_configuration

        out["LogGroupConfiguration"] = (
            capo_oam.types.log_group_configuration.serialize_json(
                value["log_group_configuration"]
            )
        )
    if "metric_configuration" in value:
        import capo_oam.types.metric_configuration

        out["MetricConfiguration"] = capo_oam.types.metric_configuration.serialize_json(
            value["metric_configuration"]
        )
    return out


def deserialize_json(data: dict) -> LinkConfiguration:
    out: LinkConfiguration = {}  # type: ignore[typeddict-item]
    if "LogGroupConfiguration" in data:
        import capo_oam.types.log_group_configuration

        out["log_group_configuration"] = (
            capo_oam.types.log_group_configuration.deserialize_json(
                data["LogGroupConfiguration"]
            )
        )
    if "MetricConfiguration" in data:
        import capo_oam.types.metric_configuration

        out["metric_configuration"] = (
            capo_oam.types.metric_configuration.deserialize_json(
                data["MetricConfiguration"]
            )
        )
    return out
