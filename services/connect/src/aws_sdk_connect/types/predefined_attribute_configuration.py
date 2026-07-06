"""Generated from Smithy shape ``com.amazonaws.connect#PredefinedAttributeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.enable_value_validation_on_association
    import aws_sdk_connect.types.is_read_only


class PredefinedAttributeConfiguration(TypedDict, closed=True):
    enable_value_validation_on_association: "aws_sdk_connect.types.enable_value_validation_on_association.EnableValueValidationOnAssociation"
    """<p>When this parameter is set to true, Connect Customer enforces strict validation on the specific values, if the values are predefined in attributes. The contact will store only valid and predefined values for teh predefined attribute key.</p>"""
    is_read_only: "aws_sdk_connect.types.is_read_only.IsReadOnly"
    """<p>A boolean flag used to indicate whether a predefined attribute should be displayed in the Connect Customer admin website.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PredefinedAttributeConfiguration) -> dict:
    out: dict = {}
    out["EnableValueValidationOnAssociation"] = value.get(
        "enable_value_validation_on_association", False
    )
    out["IsReadOnly"] = value.get("is_read_only", False)
    return out


def deserialize_json(data: dict) -> PredefinedAttributeConfiguration:
    out: PredefinedAttributeConfiguration = {}  # type: ignore[typeddict-item]
    if "EnableValueValidationOnAssociation" in data:
        out["enable_value_validation_on_association"] = data[
            "EnableValueValidationOnAssociation"
        ]
    else:
        out["enable_value_validation_on_association"] = False
    if "IsReadOnly" in data:
        out["is_read_only"] = data["IsReadOnly"]
    else:
        out["is_read_only"] = False
    return out
