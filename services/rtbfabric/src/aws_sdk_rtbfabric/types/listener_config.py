"""Generated from Smithy shape ``com.amazonaws.rtbfabric#ListenerConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_rtbfabric.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rtbfabric.types.protocol_list


class ListenerConfig(TypedDict):
    protocols: "aws_sdk_rtbfabric.types.protocol_list.ProtocolList"
    """<p>The protocol for connections from clients to the gateway</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListenerConfig) -> dict:
    out: dict = {}
    import aws_sdk_rtbfabric.types.protocol_list

    out["protocols"] = aws_sdk_rtbfabric.types.protocol_list.serialize_json(
        value["protocols"]
    )
    return out


def deserialize_json(data: dict) -> ListenerConfig:
    out: ListenerConfig = {}  # type: ignore[typeddict-item]
    if "protocols" in data:
        import aws_sdk_rtbfabric.types.protocol_list

        out["protocols"] = aws_sdk_rtbfabric.types.protocol_list.deserialize_json(
            data["protocols"]
        )
    else:
        raise DeserializationError("ListenerConfig.protocols required")
    return out
