"""Generated from Smithy shape ``com.amazonaws.pi#ResponsePartitionKey``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_pi.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pi.types.dimension_map


class ResponsePartitionKey(TypedDict):
    dimensions: "aws_sdk_pi.types.dimension_map.DimensionMap"
    """<p>A dimension map that contains the dimensions for this partition.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResponsePartitionKey) -> dict:
    out: dict = {}
    import aws_sdk_pi.types.dimension_map

    out["Dimensions"] = aws_sdk_pi.types.dimension_map.serialize_aws_json_1_1(
        value["dimensions"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResponsePartitionKey:
    out: ResponsePartitionKey = {}  # type: ignore[typeddict-item]
    if "Dimensions" in data:
        import aws_sdk_pi.types.dimension_map

        out["dimensions"] = aws_sdk_pi.types.dimension_map.deserialize_aws_json_1_1(
            data["Dimensions"]
        )
    else:
        raise DeserializationError("ResponsePartitionKey.dimensions required")
    return out
