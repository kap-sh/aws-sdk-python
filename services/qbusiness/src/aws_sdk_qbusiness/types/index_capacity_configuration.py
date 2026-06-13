"""Generated from Smithy shape ``com.amazonaws.qbusiness#IndexCapacityConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.index_capacity_integer


class IndexCapacityConfiguration(TypedDict):
    units: NotRequired[
        "aws_sdk_qbusiness.types.index_capacity_integer.IndexCapacityInteger"
    ]
    """<p>The number of storage units configured for an Amazon Q Business index.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IndexCapacityConfiguration) -> dict:
    out: dict = {}
    if "units" in value:
        out["units"] = value["units"]
    return out


def deserialize_json(data: dict) -> IndexCapacityConfiguration:
    out: IndexCapacityConfiguration = {}  # type: ignore[typeddict-item]
    if "units" in data:
        out["units"] = data["units"]
    return out
