"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#InputSource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.input_source_type


class InputSource(TypedDict, closed=True):
    identifier: "str"
    """<p>The identifier of the input source.</p>"""
    type: "aws_sdk_resiliencehubv2.types.input_source_type.InputSourceType"
    """<p>The type of the input source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InputSource) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    import aws_sdk_resiliencehubv2.types.input_source_type

    out["type"] = aws_sdk_resiliencehubv2.types.input_source_type.serialize_json(
        value["type"]
    )
    return out


def deserialize_json(data: dict) -> InputSource:
    out: InputSource = {}  # type: ignore[typeddict-item]
    if "identifier" in data:
        out["identifier"] = data["identifier"]
    else:
        raise DeserializationError("InputSource.identifier required")
    if "type" in data:
        import aws_sdk_resiliencehubv2.types.input_source_type

        out["type"] = aws_sdk_resiliencehubv2.types.input_source_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("InputSource.type required")
    return out
