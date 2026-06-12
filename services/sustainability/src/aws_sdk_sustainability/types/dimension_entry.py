"""Generated from Smithy shape ``com.amazonaws.sustainability#DimensionEntry``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sustainability.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sustainability.types.dimension


class DimensionEntry(TypedDict):
    dimension: "aws_sdk_sustainability.types.dimension.Dimension"
    """<p>The dimension type that categorizes this entry.</p>"""
    value: "str"
    """<p> The value for the specified dimension. Valid values vary based on the dimension type (e.g., <code>us-east-1</code> for the <code>REGION</code> dimension, <code>AmazonEC2</code> for the <code>SERVICE</code> dimension). </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DimensionEntry) -> dict:
    out: dict = {}
    import aws_sdk_sustainability.types.dimension

    out["Dimension"] = aws_sdk_sustainability.types.dimension.serialize_json(
        value["dimension"]
    )
    out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> DimensionEntry:
    out: DimensionEntry = {}  # type: ignore[typeddict-item]
    if "Dimension" in data:
        import aws_sdk_sustainability.types.dimension

        out["dimension"] = aws_sdk_sustainability.types.dimension.deserialize_json(
            data["Dimension"]
        )
    else:
        raise DeserializationError("DimensionEntry.dimension required")
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("DimensionEntry.value required")
    return out
