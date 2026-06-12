"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ForwardingConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.forwarding_config_state


class ForwardingConfig(TypedDict):
    state: "aws_sdk_iotsitewise.types.forwarding_config_state.ForwardingConfigState"
    """<p>The forwarding state for the given property. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ForwardingConfig) -> dict:
    out: dict = {}
    import aws_sdk_iotsitewise.types.forwarding_config_state

    out["state"] = aws_sdk_iotsitewise.types.forwarding_config_state.serialize_json(
        value["state"]
    )
    return out


def deserialize_json(data: dict) -> ForwardingConfig:
    out: ForwardingConfig = {}  # type: ignore[typeddict-item]
    if "state" in data:
        import aws_sdk_iotsitewise.types.forwarding_config_state

        out["state"] = (
            aws_sdk_iotsitewise.types.forwarding_config_state.deserialize_json(
                data["state"]
            )
        )
    else:
        raise DeserializationError("ForwardingConfig.state required")
    return out
