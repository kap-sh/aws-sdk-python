"""Generated from Smithy shape ``com.amazonaws.quicksight#ForecastScenario``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.what_if_point_scenario
    import capo_quicksight.types.what_if_range_scenario


class ForecastScenario(TypedDict, closed=True):
    what_if_point_scenario: NotRequired[
        "capo_quicksight.types.what_if_point_scenario.WhatIfPointScenario"
    ]
    """<p>The what-if analysis forecast setup with the target date.</p>"""
    what_if_range_scenario: NotRequired[
        "capo_quicksight.types.what_if_range_scenario.WhatIfRangeScenario"
    ]
    """<p>The what-if analysis forecast setup with the date range.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ForecastScenario) -> dict:
    out: dict = {}
    if "what_if_point_scenario" in value:
        import capo_quicksight.types.what_if_point_scenario

        out["WhatIfPointScenario"] = (
            capo_quicksight.types.what_if_point_scenario.serialize_json(
                value["what_if_point_scenario"]
            )
        )
    if "what_if_range_scenario" in value:
        import capo_quicksight.types.what_if_range_scenario

        out["WhatIfRangeScenario"] = (
            capo_quicksight.types.what_if_range_scenario.serialize_json(
                value["what_if_range_scenario"]
            )
        )
    return out


def deserialize_json(data: dict) -> ForecastScenario:
    out: ForecastScenario = {}  # type: ignore[typeddict-item]
    if "WhatIfPointScenario" in data:
        import capo_quicksight.types.what_if_point_scenario

        out["what_if_point_scenario"] = (
            capo_quicksight.types.what_if_point_scenario.deserialize_json(
                data["WhatIfPointScenario"]
            )
        )
    if "WhatIfRangeScenario" in data:
        import capo_quicksight.types.what_if_range_scenario

        out["what_if_range_scenario"] = (
            capo_quicksight.types.what_if_range_scenario.deserialize_json(
                data["WhatIfRangeScenario"]
            )
        )
    return out
