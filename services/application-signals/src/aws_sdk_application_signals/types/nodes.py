"""Generated from Smithy shape ``com.amazonaws.applicationsignals#Nodes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_application_signals.types.node

Nodes: TypeAlias = list["aws_sdk_application_signals.types.node.Node"]


# --- restJson1 ser/de ---
def serialize_json(value: Nodes) -> list:
    import aws_sdk_application_signals.types.node

    out: list = []
    for item in value:
        out.append(aws_sdk_application_signals.types.node.serialize_json(item))
    return out


def deserialize_json(data: list) -> Nodes:
    import aws_sdk_application_signals.types.node

    out: Nodes = []
    for item in data:
        out.append(aws_sdk_application_signals.types.node.deserialize_json(item))
    return out
