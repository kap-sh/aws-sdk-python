"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ConfigurationStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.configuration_error_details
    import aws_sdk_iotsitewise.types.configuration_state


class ConfigurationStatus(TypedDict):
    state: "aws_sdk_iotsitewise.types.configuration_state.ConfigurationState"
    """<p>The current state of the configuration.</p>"""
    error: NotRequired[
        "aws_sdk_iotsitewise.types.configuration_error_details.ConfigurationErrorDetails"
    ]
    """<p>Contains associated error information, if any.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationStatus) -> dict:
    out: dict = {}
    import aws_sdk_iotsitewise.types.configuration_state

    out["state"] = aws_sdk_iotsitewise.types.configuration_state.serialize_json(
        value["state"]
    )
    if "error" in value:
        import aws_sdk_iotsitewise.types.configuration_error_details

        out["error"] = (
            aws_sdk_iotsitewise.types.configuration_error_details.serialize_json(
                value["error"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConfigurationStatus:
    out: ConfigurationStatus = {}  # type: ignore[typeddict-item]
    if "state" in data:
        import aws_sdk_iotsitewise.types.configuration_state

        out["state"] = aws_sdk_iotsitewise.types.configuration_state.deserialize_json(
            data["state"]
        )
    else:
        raise DeserializationError("ConfigurationStatus.state required")
    if "error" in data:
        import aws_sdk_iotsitewise.types.configuration_error_details

        out["error"] = (
            aws_sdk_iotsitewise.types.configuration_error_details.deserialize_json(
                data["error"]
            )
        )
    return out
