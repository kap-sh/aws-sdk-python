"""Generated from Smithy shape ``com.amazonaws.connect#OutboundStrategy``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.outbound_strategy_config
    import aws_sdk_connect.types.outbound_strategy_type


class OutboundStrategy(TypedDict):
    type: "aws_sdk_connect.types.outbound_strategy_type.OutboundStrategyType"
    """<p>Type of the outbound strategy.</p>"""
    config: NotRequired[
        "aws_sdk_connect.types.outbound_strategy_config.OutboundStrategyConfig"
    ]
    """<p>Config of the outbound strategy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OutboundStrategy) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.outbound_strategy_type

    out["Type"] = aws_sdk_connect.types.outbound_strategy_type.serialize_json(
        value["type"]
    )
    if "config" in value:
        import aws_sdk_connect.types.outbound_strategy_config

        out["Config"] = aws_sdk_connect.types.outbound_strategy_config.serialize_json(
            value["config"]
        )
    return out


def deserialize_json(data: dict) -> OutboundStrategy:
    out: OutboundStrategy = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_connect.types.outbound_strategy_type

        out["type"] = aws_sdk_connect.types.outbound_strategy_type.deserialize_json(
            data["Type"]
        )
    else:
        raise DeserializationError("OutboundStrategy.type required")
    if "Config" in data:
        import aws_sdk_connect.types.outbound_strategy_config

        out["config"] = aws_sdk_connect.types.outbound_strategy_config.deserialize_json(
            data["Config"]
        )
    return out
