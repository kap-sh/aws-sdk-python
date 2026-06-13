"""Generated from Smithy shape ``com.amazonaws.quicksight#ForecastScenario``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.what_if_point_scenario
    import aws_sdk_quicksight.types.what_if_range_scenario


class ForecastScenario(TypedDict):
    what_if_point_scenario: NotRequired[
        "aws_sdk_quicksight.types.what_if_point_scenario.WhatIfPointScenario"
    ]
    """<p>The what-if analysis forecast setup with the target date.</p>"""
    what_if_range_scenario: NotRequired[
        "aws_sdk_quicksight.types.what_if_range_scenario.WhatIfRangeScenario"
    ]
    """<p>The what-if analysis forecast setup with the date range.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ForecastScenario) -> dict:
    out: dict = {}
    if "what_if_point_scenario" in value:
        import aws_sdk_quicksight.types.what_if_point_scenario

        out["WhatIfPointScenario"] = (
            aws_sdk_quicksight.types.what_if_point_scenario.serialize_json(
                value["what_if_point_scenario"]
            )
        )
    if "what_if_range_scenario" in value:
        import aws_sdk_quicksight.types.what_if_range_scenario

        out["WhatIfRangeScenario"] = (
            aws_sdk_quicksight.types.what_if_range_scenario.serialize_json(
                value["what_if_range_scenario"]
            )
        )
    return out


def deserialize_json(data: dict) -> ForecastScenario:
    out: ForecastScenario = {}  # type: ignore[typeddict-item]
    if "WhatIfPointScenario" in data:
        import aws_sdk_quicksight.types.what_if_point_scenario

        out["what_if_point_scenario"] = (
            aws_sdk_quicksight.types.what_if_point_scenario.deserialize_json(
                data["WhatIfPointScenario"]
            )
        )
    if "WhatIfRangeScenario" in data:
        import aws_sdk_quicksight.types.what_if_range_scenario

        out["what_if_range_scenario"] = (
            aws_sdk_quicksight.types.what_if_range_scenario.deserialize_json(
                data["WhatIfRangeScenario"]
            )
        )
    return out
