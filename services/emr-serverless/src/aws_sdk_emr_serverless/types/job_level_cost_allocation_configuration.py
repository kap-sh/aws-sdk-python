"""Generated from Smithy shape ``com.amazonaws.emrserverless#JobLevelCostAllocationConfiguration``."""

from typing_extensions import NotRequired, TypedDict


class JobLevelCostAllocationConfiguration(TypedDict, closed=True):
    enabled: NotRequired["bool"]
    """<p>Enables job level cost allocation for the application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobLevelCostAllocationConfiguration) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    return out


def deserialize_json(data: dict) -> JobLevelCostAllocationConfiguration:
    out: JobLevelCostAllocationConfiguration = {}  # type: ignore[typeddict-item]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    return out
