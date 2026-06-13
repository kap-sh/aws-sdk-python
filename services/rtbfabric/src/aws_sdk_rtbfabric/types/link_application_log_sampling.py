"""Generated from Smithy shape ``com.amazonaws.rtbfabric#LinkApplicationLogSampling``."""

from typing import TypedDict

from aws_sdk_rtbfabric.errors import DeserializationError


class LinkApplicationLogSampling(TypedDict):
    error_log: "float"
    """<p>An error log entry.</p>"""
    filter_log: "float"
    """<p>A filter log entry.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LinkApplicationLogSampling) -> dict:
    out: dict = {}
    out["errorLog"] = value["error_log"]
    out["filterLog"] = value["filter_log"]
    return out


def deserialize_json(data: dict) -> LinkApplicationLogSampling:
    out: LinkApplicationLogSampling = {}  # type: ignore[typeddict-item]
    if "errorLog" in data:
        out["error_log"] = data["errorLog"]
    else:
        raise DeserializationError("LinkApplicationLogSampling.error_log required")
    if "filterLog" in data:
        out["filter_log"] = data["filterLog"]
    else:
        raise DeserializationError("LinkApplicationLogSampling.filter_log required")
    return out
