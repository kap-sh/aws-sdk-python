"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#InputSource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.input_source_type


class InputSource(TypedDict, closed=True):
    identifier: "str"
    """<p>The identifier of the input source.</p>"""
    type: "capo_resiliencehubv2.types.input_source_type.InputSourceType"
    """<p>The type of the input source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InputSource) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    import capo_resiliencehubv2.types.input_source_type

    out["type"] = capo_resiliencehubv2.types.input_source_type.serialize_json(
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
        import capo_resiliencehubv2.types.input_source_type

        out["type"] = capo_resiliencehubv2.types.input_source_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("InputSource.type required")
    return out
