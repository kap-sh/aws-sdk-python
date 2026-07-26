"""Generated from Smithy shape ``com.amazonaws.amp#LoggingFilter``."""

from typing_extensions import TypedDict

from capo_amp.errors import DeserializationError


class LoggingFilter(TypedDict, closed=True):
    qsp_threshold: "int"
    """<p>The Query Samples Processed (QSP) threshold above which queries will be logged. Queries processing more samples than this threshold will be captured in logs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LoggingFilter) -> dict:
    out: dict = {}
    out["qspThreshold"] = value["qsp_threshold"]
    return out


def deserialize_json(data: dict) -> LoggingFilter:
    out: LoggingFilter = {}  # type: ignore[typeddict-item]
    if "qspThreshold" in data:
        out["qsp_threshold"] = data["qspThreshold"]
    else:
        raise DeserializationError("LoggingFilter.qsp_threshold required")
    return out
