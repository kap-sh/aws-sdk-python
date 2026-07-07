"""Generated from Smithy shape ``com.amazonaws.controltower#GetEnabledControlInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_controltower.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_controltower.types.arn


class GetEnabledControlInput(TypedDict, closed=True):
    enabled_control_identifier: "aws_sdk_controltower.types.arn.Arn"
    """<p>The <code>controlIdentifier</code> of the enabled control.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEnabledControlInput) -> dict:
    out: dict = {}
    out["enabledControlIdentifier"] = value["enabled_control_identifier"]
    return out


def deserialize_json(data: dict) -> GetEnabledControlInput:
    out: GetEnabledControlInput = {}  # type: ignore[typeddict-item]
    if "enabledControlIdentifier" in data:
        out["enabled_control_identifier"] = data["enabledControlIdentifier"]
    else:
        raise DeserializationError(
            "GetEnabledControlInput.enabled_control_identifier required"
        )
    return out
