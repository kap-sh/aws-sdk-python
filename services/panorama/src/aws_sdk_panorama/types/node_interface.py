"""Generated from Smithy shape ``com.amazonaws.panorama#NodeInterface``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_panorama.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_panorama.types.input_port_list
    import aws_sdk_panorama.types.output_port_list


class NodeInterface(TypedDict):
    inputs: "aws_sdk_panorama.types.input_port_list.InputPortList"
    """<p>The node interface's inputs.</p>"""
    outputs: "aws_sdk_panorama.types.output_port_list.OutputPortList"
    """<p>The node interface's outputs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NodeInterface) -> dict:
    out: dict = {}
    import aws_sdk_panorama.types.input_port_list

    out["Inputs"] = aws_sdk_panorama.types.input_port_list.serialize_json(
        value["inputs"]
    )
    import aws_sdk_panorama.types.output_port_list

    out["Outputs"] = aws_sdk_panorama.types.output_port_list.serialize_json(
        value["outputs"]
    )
    return out


def deserialize_json(data: dict) -> NodeInterface:
    out: NodeInterface = {}  # type: ignore[typeddict-item]
    if "Inputs" in data:
        import aws_sdk_panorama.types.input_port_list

        out["inputs"] = aws_sdk_panorama.types.input_port_list.deserialize_json(
            data["Inputs"]
        )
    else:
        raise DeserializationError("NodeInterface.inputs required")
    if "Outputs" in data:
        import aws_sdk_panorama.types.output_port_list

        out["outputs"] = aws_sdk_panorama.types.output_port_list.deserialize_json(
            data["Outputs"]
        )
    else:
        raise DeserializationError("NodeInterface.outputs required")
    return out
