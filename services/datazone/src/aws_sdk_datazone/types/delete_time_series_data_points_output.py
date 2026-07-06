"""Generated from Smithy shape ``com.amazonaws.datazone#DeleteTimeSeriesDataPointsOutput``."""

from typing_extensions import TypedDict


class DeleteTimeSeriesDataPointsOutput(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTimeSeriesDataPointsOutput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteTimeSeriesDataPointsOutput:
    out: DeleteTimeSeriesDataPointsOutput = {}  # type: ignore[typeddict-item]
    return out
