"""Generated from Smithy shape ``com.amazonaws.drs#CPU``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.bounded_string
    import capo_drs.types.positive_integer


class CPU(TypedDict, closed=True):
    cores: "capo_drs.types.positive_integer.PositiveInteger"
    """<p>The number of CPU cores.</p>"""
    model_name: NotRequired["capo_drs.types.bounded_string.BoundedString"]
    """<p>The model name of the CPU.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CPU) -> dict:
    out: dict = {}
    out["cores"] = value.get("cores", 0)
    if "model_name" in value:
        out["modelName"] = value["model_name"]
    return out


def deserialize_json(data: dict) -> CPU:
    out: CPU = {}  # type: ignore[typeddict-item]
    if "cores" in data:
        out["cores"] = data["cores"]
    else:
        out["cores"] = 0
    if "modelName" in data:
        out["model_name"] = data["modelName"]
    return out
