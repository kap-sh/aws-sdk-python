"""Generated from Smithy shape ``com.amazonaws.m2#EngineVersionsSummary``."""

from typing_extensions import TypedDict

from capo_m2.errors import DeserializationError


class EngineVersionsSummary(TypedDict, closed=True):
    engine_type: "str"
    """<p>The type of target platform for the application.</p>"""
    engine_version: "str"
    """<p>The version of the engine type used by the application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EngineVersionsSummary) -> dict:
    out: dict = {}
    out["engineType"] = value["engine_type"]
    out["engineVersion"] = value["engine_version"]
    return out


def deserialize_json(data: dict) -> EngineVersionsSummary:
    out: EngineVersionsSummary = {}  # type: ignore[typeddict-item]
    if "engineType" in data:
        out["engine_type"] = data["engineType"]
    else:
        raise DeserializationError("EngineVersionsSummary.engine_type required")
    if "engineVersion" in data:
        out["engine_version"] = data["engineVersion"]
    else:
        raise DeserializationError("EngineVersionsSummary.engine_version required")
    return out
