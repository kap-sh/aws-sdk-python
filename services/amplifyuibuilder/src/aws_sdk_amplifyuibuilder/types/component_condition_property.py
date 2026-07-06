"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ComponentConditionProperty``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.component_property

ComponentConditionProperty = TypedDict(
    "ComponentConditionProperty",
    {
        "property": NotRequired["str"],
        "field": NotRequired["str"],
        "operator": NotRequired["str"],
        "operand": NotRequired["str"],
        "then": NotRequired[
            "aws_sdk_amplifyuibuilder.types.component_property.ComponentProperty"
        ],
        "else": NotRequired[
            "aws_sdk_amplifyuibuilder.types.component_property.ComponentProperty"
        ],
        "operand_type": NotRequired["str"],
    },
    closed=True,
)


# --- restJson1 ser/de ---
def serialize_json(value: ComponentConditionProperty) -> dict:
    out: dict = {}
    if "property" in value:
        out["property"] = value["property"]
    if "field" in value:
        out["field"] = value["field"]
    if "operator" in value:
        out["operator"] = value["operator"]
    if "operand" in value:
        out["operand"] = value["operand"]
    if "then" in value:
        import aws_sdk_amplifyuibuilder.types.component_property

        out["then"] = aws_sdk_amplifyuibuilder.types.component_property.serialize_json(
            value["then"]
        )
    if "else" in value:
        import aws_sdk_amplifyuibuilder.types.component_property

        out["else"] = aws_sdk_amplifyuibuilder.types.component_property.serialize_json(
            value["else"]
        )
    if "operand_type" in value:
        out["operandType"] = value["operand_type"]
    return out


def deserialize_json(data: dict) -> ComponentConditionProperty:
    out: ComponentConditionProperty = {}  # type: ignore[typeddict-item]
    if "property" in data:
        out["property"] = data["property"]
    if "field" in data:
        out["field"] = data["field"]
    if "operator" in data:
        out["operator"] = data["operator"]
    if "operand" in data:
        out["operand"] = data["operand"]
    if "then" in data:
        import aws_sdk_amplifyuibuilder.types.component_property

        out["then"] = (
            aws_sdk_amplifyuibuilder.types.component_property.deserialize_json(
                data["then"]
            )
        )
    if "else" in data:
        import aws_sdk_amplifyuibuilder.types.component_property

        out["else"] = (
            aws_sdk_amplifyuibuilder.types.component_property.deserialize_json(
                data["else"]
            )
        )
    if "operandType" in data:
        out["operand_type"] = data["operandType"]
    return out
