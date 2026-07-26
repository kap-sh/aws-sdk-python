"""Generated from Smithy shape ``com.amazonaws.quicksight#SemanticEntityType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.limited_string
    import capo_quicksight.types.type_parameters


class SemanticEntityType(TypedDict, closed=True):
    type_name: NotRequired["capo_quicksight.types.limited_string.LimitedString"]
    """<p>The semantic entity type name.</p>"""
    sub_type_name: NotRequired["capo_quicksight.types.limited_string.LimitedString"]
    """<p>The semantic entity sub type name.</p>"""
    type_parameters: NotRequired["capo_quicksight.types.type_parameters.TypeParameters"]
    """<p>The semantic entity type parameters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SemanticEntityType) -> dict:
    out: dict = {}
    if "type_name" in value:
        out["TypeName"] = value["type_name"]
    if "sub_type_name" in value:
        out["SubTypeName"] = value["sub_type_name"]
    if "type_parameters" in value:
        import capo_quicksight.types.type_parameters

        out["TypeParameters"] = capo_quicksight.types.type_parameters.serialize_json(
            value["type_parameters"]
        )
    return out


def deserialize_json(data: dict) -> SemanticEntityType:
    out: SemanticEntityType = {}  # type: ignore[typeddict-item]
    if "TypeName" in data:
        out["type_name"] = data["TypeName"]
    if "SubTypeName" in data:
        out["sub_type_name"] = data["SubTypeName"]
    if "TypeParameters" in data:
        import capo_quicksight.types.type_parameters

        out["type_parameters"] = capo_quicksight.types.type_parameters.deserialize_json(
            data["TypeParameters"]
        )
    return out
