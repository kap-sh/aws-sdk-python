"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SubSlotSetting``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.sub_slot_expression
    import aws_sdk_lex_models_v2.types.sub_slot_specification_map


class SubSlotSetting(TypedDict, closed=True):
    expression: NotRequired[
        "aws_sdk_lex_models_v2.types.sub_slot_expression.SubSlotExpression"
    ]
    """<p>The expression text for defining the constituent sub slots in the composite slot using logical AND and OR operators.</p>"""
    slot_specifications: NotRequired[
        "aws_sdk_lex_models_v2.types.sub_slot_specification_map.SubSlotSpecificationMap"
    ]
    """<p>Specifications for the constituent sub slots of a composite slot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubSlotSetting) -> dict:
    out: dict = {}
    if "expression" in value:
        out["expression"] = value["expression"]
    if "slot_specifications" in value:
        import aws_sdk_lex_models_v2.types.sub_slot_specification_map

        out["slotSpecifications"] = (
            aws_sdk_lex_models_v2.types.sub_slot_specification_map.serialize_json(
                value["slot_specifications"]
            )
        )
    return out


def deserialize_json(data: dict) -> SubSlotSetting:
    out: SubSlotSetting = {}  # type: ignore[typeddict-item]
    if "expression" in data:
        out["expression"] = data["expression"]
    if "slotSpecifications" in data:
        import aws_sdk_lex_models_v2.types.sub_slot_specification_map

        out["slot_specifications"] = (
            aws_sdk_lex_models_v2.types.sub_slot_specification_map.deserialize_json(
                data["slotSpecifications"]
            )
        )
    return out
