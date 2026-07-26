"""Generated from Smithy shape ``com.amazonaws.connect#InputPredefinedAttributeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.enable_value_validation_on_association


class InputPredefinedAttributeConfiguration(TypedDict, closed=True):
    enable_value_validation_on_association: "capo_connect.types.enable_value_validation_on_association.EnableValueValidationOnAssociation"
    """<p>When this parameter is set to true, Connect Customer enforces strict validation on the specific values, if the values are predefined in attributes. The contact will store only valid and predefined values for the predefined attribute key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InputPredefinedAttributeConfiguration) -> dict:
    out: dict = {}
    out["EnableValueValidationOnAssociation"] = value.get(
        "enable_value_validation_on_association", False
    )
    return out


def deserialize_json(data: dict) -> InputPredefinedAttributeConfiguration:
    out: InputPredefinedAttributeConfiguration = {}  # type: ignore[typeddict-item]
    if "EnableValueValidationOnAssociation" in data:
        out["enable_value_validation_on_association"] = data[
            "EnableValueValidationOnAssociation"
        ]
    else:
        out["enable_value_validation_on_association"] = False
    return out
