"""Generated from Smithy shape ``com.amazonaws.controltower#EnabledControlInheritanceDrift``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_controltower.types.drift_status


class EnabledControlInheritanceDrift(TypedDict):
    status: NotRequired["aws_sdk_controltower.types.drift_status.DriftStatus"]
    """<p>The status of inheritance drift for the enabled control, indicating whether inheritance configuration matches expectations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnabledControlInheritanceDrift) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_controltower.types.drift_status

        out["status"] = aws_sdk_controltower.types.drift_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> EnabledControlInheritanceDrift:
    out: EnabledControlInheritanceDrift = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_controltower.types.drift_status

        out["status"] = aws_sdk_controltower.types.drift_status.deserialize_json(
            data["status"]
        )
    return out
