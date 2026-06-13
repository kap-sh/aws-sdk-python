"""Generated from Smithy shape ``com.amazonaws.quicksight#WhatIfRangeScenario``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.double
    import aws_sdk_quicksight.types.timestamp


class WhatIfRangeScenario(TypedDict):
    start_date: "aws_sdk_quicksight.types.timestamp.Timestamp"
    """<p>The start date in the date range that you need the forecast results for.</p>"""
    end_date: "aws_sdk_quicksight.types.timestamp.Timestamp"
    """<p>The end date in the date range that you need the forecast results for.</p>"""
    value: "aws_sdk_quicksight.types.double.Double"
    """<p>The target value that you want to meet for the provided date range.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WhatIfRangeScenario) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.timestamp

    out["StartDate"] = aws_sdk_quicksight.types.timestamp.serialize_json(
        value["start_date"]
    )
    import aws_sdk_quicksight.types.timestamp

    out["EndDate"] = aws_sdk_quicksight.types.timestamp.serialize_json(
        value["end_date"]
    )
    out["Value"] = value.get("value", 0)
    return out


def deserialize_json(data: dict) -> WhatIfRangeScenario:
    out: WhatIfRangeScenario = {}  # type: ignore[typeddict-item]
    if "StartDate" in data:
        import aws_sdk_quicksight.types.timestamp

        out["start_date"] = aws_sdk_quicksight.types.timestamp.deserialize_json(
            data["StartDate"]
        )
    else:
        raise DeserializationError("WhatIfRangeScenario.start_date required")
    if "EndDate" in data:
        import aws_sdk_quicksight.types.timestamp

        out["end_date"] = aws_sdk_quicksight.types.timestamp.deserialize_json(
            data["EndDate"]
        )
    else:
        raise DeserializationError("WhatIfRangeScenario.end_date required")
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        out["value"] = 0
    return out
