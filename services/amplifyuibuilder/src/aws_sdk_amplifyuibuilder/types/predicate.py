"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#Predicate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.operand_type
    import aws_sdk_amplifyuibuilder.types.predicate_list

Predicate = TypedDict(
    "Predicate",
    {
        "or": NotRequired[
            "aws_sdk_amplifyuibuilder.types.predicate_list.PredicateList"
        ],
        "and": NotRequired[
            "aws_sdk_amplifyuibuilder.types.predicate_list.PredicateList"
        ],
        "field": NotRequired["str"],
        "operator": NotRequired["str"],
        "operand": NotRequired["str"],
        "operand_type": NotRequired[
            "aws_sdk_amplifyuibuilder.types.operand_type.OperandType"
        ],
    },
    closed=True,
)


# --- restJson1 ser/de ---
def serialize_json(value: Predicate) -> dict:
    out: dict = {}
    if "or" in value:
        import aws_sdk_amplifyuibuilder.types.predicate_list

        out["or"] = aws_sdk_amplifyuibuilder.types.predicate_list.serialize_json(
            value["or"]
        )
    if "and" in value:
        import aws_sdk_amplifyuibuilder.types.predicate_list

        out["and"] = aws_sdk_amplifyuibuilder.types.predicate_list.serialize_json(
            value["and"]
        )
    if "field" in value:
        out["field"] = value["field"]
    if "operator" in value:
        out["operator"] = value["operator"]
    if "operand" in value:
        out["operand"] = value["operand"]
    if "operand_type" in value:
        out["operandType"] = value["operand_type"]
    return out


def deserialize_json(data: dict) -> Predicate:
    out: Predicate = {}  # type: ignore[typeddict-item]
    if "or" in data:
        import aws_sdk_amplifyuibuilder.types.predicate_list

        out["or"] = aws_sdk_amplifyuibuilder.types.predicate_list.deserialize_json(
            data["or"]
        )
    if "and" in data:
        import aws_sdk_amplifyuibuilder.types.predicate_list

        out["and"] = aws_sdk_amplifyuibuilder.types.predicate_list.deserialize_json(
            data["and"]
        )
    if "field" in data:
        out["field"] = data["field"]
    if "operator" in data:
        out["operator"] = data["operator"]
    if "operand" in data:
        out["operand"] = data["operand"]
    if "operandType" in data:
        out["operand_type"] = data["operandType"]
    return out
