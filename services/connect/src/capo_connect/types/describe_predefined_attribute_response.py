"""Generated from Smithy shape ``com.amazonaws.connect#DescribePredefinedAttributeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.predefined_attribute


class DescribePredefinedAttributeResponse(TypedDict, closed=True):
    predefined_attribute: NotRequired[
        "capo_connect.types.predefined_attribute.PredefinedAttribute"
    ]
    """<p>Information about the predefined attribute.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribePredefinedAttributeResponse) -> dict:
    out: dict = {}
    if "predefined_attribute" in value:
        import capo_connect.types.predefined_attribute

        out["PredefinedAttribute"] = (
            capo_connect.types.predefined_attribute.serialize_json(
                value["predefined_attribute"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribePredefinedAttributeResponse:
    out: DescribePredefinedAttributeResponse = {}  # type: ignore[typeddict-item]
    if "PredefinedAttribute" in data:
        import capo_connect.types.predefined_attribute

        out["predefined_attribute"] = (
            capo_connect.types.predefined_attribute.deserialize_json(
                data["PredefinedAttribute"]
            )
        )
    return out
