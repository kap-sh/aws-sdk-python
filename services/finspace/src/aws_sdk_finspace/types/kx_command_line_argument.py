"""Generated from Smithy shape ``com.amazonaws.finspace#KxCommandLineArgument``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_finspace.types.kx_command_line_argument_key
    import aws_sdk_finspace.types.kx_command_line_argument_value


class KxCommandLineArgument(TypedDict, closed=True):
    key: NotRequired[
        "aws_sdk_finspace.types.kx_command_line_argument_key.KxCommandLineArgumentKey"
    ]
    """<p>The name of the key.</p>"""
    value: NotRequired[
        "aws_sdk_finspace.types.kx_command_line_argument_value.KxCommandLineArgumentValue"
    ]
    """<p>The value of the key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KxCommandLineArgument) -> dict:
    out: dict = {}
    if "key" in value:
        out["key"] = value["key"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> KxCommandLineArgument:
    out: KxCommandLineArgument = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    if "value" in data:
        out["value"] = data["value"]
    return out
