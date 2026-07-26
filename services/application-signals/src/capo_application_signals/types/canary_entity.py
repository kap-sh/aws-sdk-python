"""Generated from Smithy shape ``com.amazonaws.applicationsignals#CanaryEntity``."""

from typing_extensions import TypedDict

from capo_application_signals.errors import DeserializationError


class CanaryEntity(TypedDict, closed=True):
    canary_name: "str"
    """<p>The name of the CloudWatch Synthetics canary.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CanaryEntity) -> dict:
    out: dict = {}
    out["CanaryName"] = value["canary_name"]
    return out


def deserialize_json(data: dict) -> CanaryEntity:
    out: CanaryEntity = {}  # type: ignore[typeddict-item]
    if "CanaryName" in data:
        out["canary_name"] = data["CanaryName"]
    else:
        raise DeserializationError("CanaryEntity.canary_name required")
    return out
