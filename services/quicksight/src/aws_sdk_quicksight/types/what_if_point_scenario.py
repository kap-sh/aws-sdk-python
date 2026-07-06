"""Generated from Smithy shape ``com.amazonaws.quicksight#WhatIfPointScenario``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.double
    import aws_sdk_quicksight.types.timestamp


class WhatIfPointScenario(TypedDict, closed=True):
    date: "aws_sdk_quicksight.types.timestamp.Timestamp"
    """<p>The date that you need the forecast results for.</p>"""
    value: "aws_sdk_quicksight.types.double.Double"
    """<p>The target value that you want to meet for the provided date.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WhatIfPointScenario) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.timestamp

    out["Date"] = aws_sdk_quicksight.types.timestamp.serialize_json(value["date"])
    out["Value"] = value.get("value", 0)
    return out


def deserialize_json(data: dict) -> WhatIfPointScenario:
    out: WhatIfPointScenario = {}  # type: ignore[typeddict-item]
    if "Date" in data:
        import aws_sdk_quicksight.types.timestamp

        out["date"] = aws_sdk_quicksight.types.timestamp.deserialize_json(data["Date"])
    else:
        raise DeserializationError("WhatIfPointScenario.date required")
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        out["value"] = 0
    return out
