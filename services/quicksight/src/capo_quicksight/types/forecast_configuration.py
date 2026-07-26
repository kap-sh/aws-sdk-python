"""Generated from Smithy shape ``com.amazonaws.quicksight#ForecastConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.forecast_scenario
    import capo_quicksight.types.time_based_forecast_properties


class ForecastConfiguration(TypedDict, closed=True):
    forecast_properties: NotRequired[
        "capo_quicksight.types.time_based_forecast_properties.TimeBasedForecastProperties"
    ]
    """<p>The forecast properties setup of a forecast in the line chart.</p>"""
    scenario: NotRequired["capo_quicksight.types.forecast_scenario.ForecastScenario"]
    """<p>The forecast scenario of a forecast in the line chart.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ForecastConfiguration) -> dict:
    out: dict = {}
    if "forecast_properties" in value:
        import capo_quicksight.types.time_based_forecast_properties

        out["ForecastProperties"] = (
            capo_quicksight.types.time_based_forecast_properties.serialize_json(
                value["forecast_properties"]
            )
        )
    if "scenario" in value:
        import capo_quicksight.types.forecast_scenario

        out["Scenario"] = capo_quicksight.types.forecast_scenario.serialize_json(
            value["scenario"]
        )
    return out


def deserialize_json(data: dict) -> ForecastConfiguration:
    out: ForecastConfiguration = {}  # type: ignore[typeddict-item]
    if "ForecastProperties" in data:
        import capo_quicksight.types.time_based_forecast_properties

        out["forecast_properties"] = (
            capo_quicksight.types.time_based_forecast_properties.deserialize_json(
                data["ForecastProperties"]
            )
        )
    if "Scenario" in data:
        import capo_quicksight.types.forecast_scenario

        out["scenario"] = capo_quicksight.types.forecast_scenario.deserialize_json(
            data["Scenario"]
        )
    return out
