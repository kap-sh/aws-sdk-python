"""Generated from Smithy shape ``com.amazonaws.sesv2#ExportDataSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.message_insights_data_source
    import capo_sesv2.types.metrics_data_source


class ExportDataSource(TypedDict, closed=True):
    metrics_data_source: NotRequired[
        "capo_sesv2.types.metrics_data_source.MetricsDataSource"
    ]
    message_insights_data_source: NotRequired[
        "capo_sesv2.types.message_insights_data_source.MessageInsightsDataSource"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ExportDataSource) -> dict:
    out: dict = {}
    if "metrics_data_source" in value:
        import capo_sesv2.types.metrics_data_source

        out["MetricsDataSource"] = capo_sesv2.types.metrics_data_source.serialize_json(
            value["metrics_data_source"]
        )
    if "message_insights_data_source" in value:
        import capo_sesv2.types.message_insights_data_source

        out["MessageInsightsDataSource"] = (
            capo_sesv2.types.message_insights_data_source.serialize_json(
                value["message_insights_data_source"]
            )
        )
    return out


def deserialize_json(data: dict) -> ExportDataSource:
    out: ExportDataSource = {}  # type: ignore[typeddict-item]
    if "MetricsDataSource" in data:
        import capo_sesv2.types.metrics_data_source

        out["metrics_data_source"] = (
            capo_sesv2.types.metrics_data_source.deserialize_json(
                data["MetricsDataSource"]
            )
        )
    if "MessageInsightsDataSource" in data:
        import capo_sesv2.types.message_insights_data_source

        out["message_insights_data_source"] = (
            capo_sesv2.types.message_insights_data_source.deserialize_json(
                data["MessageInsightsDataSource"]
            )
        )
    return out
