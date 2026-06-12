"""Generated from Smithy shape ``com.amazonaws.connect#CrossChannelBehavior``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.behavior_type


class CrossChannelBehavior(TypedDict):
    behavior_type: "aws_sdk_connect.types.behavior_type.BehaviorType"
    """<p>Specifies the other channels that can be routed to an agent handling their current channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CrossChannelBehavior) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.behavior_type

    out["BehaviorType"] = aws_sdk_connect.types.behavior_type.serialize_json(
        value["behavior_type"]
    )
    return out


def deserialize_json(data: dict) -> CrossChannelBehavior:
    out: CrossChannelBehavior = {}  # type: ignore[typeddict-item]
    if "BehaviorType" in data:
        import aws_sdk_connect.types.behavior_type

        out["behavior_type"] = aws_sdk_connect.types.behavior_type.deserialize_json(
            data["BehaviorType"]
        )
    else:
        raise DeserializationError("CrossChannelBehavior.behavior_type required")
    return out
