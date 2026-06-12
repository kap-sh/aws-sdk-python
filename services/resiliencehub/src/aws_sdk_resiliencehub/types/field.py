"""Generated from Smithy shape ``com.amazonaws.resiliencehub#Field``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.field_aggregation_type
    import aws_sdk_resiliencehub.types.string255


class Field(TypedDict):
    name: "aws_sdk_resiliencehub.types.string255.String255"
    """<p>Name of the field.</p>"""
    aggregation: NotRequired[
        "aws_sdk_resiliencehub.types.field_aggregation_type.FieldAggregationType"
    ]
    """<p>(Optional) Indicates the type of aggregation or summary operation (such as Sum, Average, and so on) to be performed on a particular field or set of data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Field) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "aggregation" in value:
        import aws_sdk_resiliencehub.types.field_aggregation_type

        out["aggregation"] = (
            aws_sdk_resiliencehub.types.field_aggregation_type.serialize_json(
                value["aggregation"]
            )
        )
    return out


def deserialize_json(data: dict) -> Field:
    out: Field = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("Field.name required")
    if "aggregation" in data:
        import aws_sdk_resiliencehub.types.field_aggregation_type

        out["aggregation"] = (
            aws_sdk_resiliencehub.types.field_aggregation_type.deserialize_json(
                data["aggregation"]
            )
        )
    return out
