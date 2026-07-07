"""Generated from Smithy shape ``com.amazonaws.controltower#GetEnabledControlOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_controltower.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_controltower.types.enabled_control_details


class GetEnabledControlOutput(TypedDict, closed=True):
    enabled_control_details: (
        "aws_sdk_controltower.types.enabled_control_details.EnabledControlDetails"
    )
    """<p>Information about the enabled control.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEnabledControlOutput) -> dict:
    out: dict = {}
    import aws_sdk_controltower.types.enabled_control_details

    out["enabledControlDetails"] = (
        aws_sdk_controltower.types.enabled_control_details.serialize_json(
            value["enabled_control_details"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetEnabledControlOutput:
    out: GetEnabledControlOutput = {}  # type: ignore[typeddict-item]
    if "enabledControlDetails" in data:
        import aws_sdk_controltower.types.enabled_control_details

        out["enabled_control_details"] = (
            aws_sdk_controltower.types.enabled_control_details.deserialize_json(
                data["enabledControlDetails"]
            )
        )
    else:
        raise DeserializationError(
            "GetEnabledControlOutput.enabled_control_details required"
        )
    return out
