"""Generated from Smithy shape ``com.amazonaws.controltower#UpdateEnabledControlInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_controltower.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_controltower.types.arn
    import aws_sdk_controltower.types.enabled_control_parameters


class UpdateEnabledControlInput(TypedDict):
    parameters: (
        "aws_sdk_controltower.types.enabled_control_parameters.EnabledControlParameters"
    )
    """<p>A key/value pair, where <code>Key</code> is of type <code>String</code> and <code>Value</code> is of type <code>Document</code>.</p>"""
    enabled_control_identifier: "aws_sdk_controltower.types.arn.Arn"
    """<p> The ARN of the enabled control that will be updated. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEnabledControlInput) -> dict:
    out: dict = {}
    import aws_sdk_controltower.types.enabled_control_parameters

    out["parameters"] = (
        aws_sdk_controltower.types.enabled_control_parameters.serialize_json(
            value["parameters"]
        )
    )
    out["enabledControlIdentifier"] = value["enabled_control_identifier"]
    return out


def deserialize_json(data: dict) -> UpdateEnabledControlInput:
    out: UpdateEnabledControlInput = {}  # type: ignore[typeddict-item]
    if "parameters" in data:
        import aws_sdk_controltower.types.enabled_control_parameters

        out["parameters"] = (
            aws_sdk_controltower.types.enabled_control_parameters.deserialize_json(
                data["parameters"]
            )
        )
    else:
        raise DeserializationError("UpdateEnabledControlInput.parameters required")
    if "enabledControlIdentifier" in data:
        out["enabled_control_identifier"] = data["enabledControlIdentifier"]
    else:
        raise DeserializationError(
            "UpdateEnabledControlInput.enabled_control_identifier required"
        )
    return out
