"""Generated from Smithy shape ``com.amazonaws.controltower#EnabledControlResourceDrift``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_controltower.types.drift_status


class EnabledControlResourceDrift(TypedDict):
    status: NotRequired["aws_sdk_controltower.types.drift_status.DriftStatus"]
    """<p>The status of resource drift for the enabled control, indicating whether the underlying resources match the expected configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnabledControlResourceDrift) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_controltower.types.drift_status

        out["status"] = aws_sdk_controltower.types.drift_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> EnabledControlResourceDrift:
    out: EnabledControlResourceDrift = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_controltower.types.drift_status

        out["status"] = aws_sdk_controltower.types.drift_status.deserialize_json(
            data["status"]
        )
    return out
