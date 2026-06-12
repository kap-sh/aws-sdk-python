"""Generated from Smithy shape ``com.amazonaws.macie2#Statistics``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__double


class Statistics(TypedDict):
    approximate_number_of_objects_to_process: NotRequired[
        "aws_sdk_macie2.types.__double.__double"
    ]
    """<p>The approximate number of objects that the job has yet to process during its current run.</p>"""
    number_of_runs: NotRequired["aws_sdk_macie2.types.__double.__double"]
    """<p>The number of times that the job has run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Statistics) -> dict:
    out: dict = {}
    if "approximate_number_of_objects_to_process" in value:
        out["approximateNumberOfObjectsToProcess"] = value[
            "approximate_number_of_objects_to_process"
        ]
    if "number_of_runs" in value:
        out["numberOfRuns"] = value["number_of_runs"]
    return out


def deserialize_json(data: dict) -> Statistics:
    out: Statistics = {}  # type: ignore[typeddict-item]
    if "approximateNumberOfObjectsToProcess" in data:
        out["approximate_number_of_objects_to_process"] = data[
            "approximateNumberOfObjectsToProcess"
        ]
    if "numberOfRuns" in data:
        out["number_of_runs"] = data["numberOfRuns"]
    return out
