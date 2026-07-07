"""Generated from Smithy shape ``com.amazonaws.customerprofiles#AttributeDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.attribute_list
    import aws_sdk_customer_profiles.types.string1_to255


class AttributeDetails(TypedDict, closed=True):
    attributes: "aws_sdk_customer_profiles.types.attribute_list.AttributeList"
    """<p>A list of attribute items specified in the mathematical expression.</p>"""
    expression: "aws_sdk_customer_profiles.types.string1_to255.string1To255"
    r"""<p>Mathematical expression that is performed on attribute items provided in the attribute list. Each element in the expression should follow the structure of \\"{ObjectTypeName.AttributeName}\\".</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttributeDetails) -> dict:
    out: dict = {}
    import aws_sdk_customer_profiles.types.attribute_list

    out["Attributes"] = aws_sdk_customer_profiles.types.attribute_list.serialize_json(
        value["attributes"]
    )
    out["Expression"] = value["expression"]
    return out


def deserialize_json(data: dict) -> AttributeDetails:
    out: AttributeDetails = {}  # type: ignore[typeddict-item]
    if "Attributes" in data:
        import aws_sdk_customer_profiles.types.attribute_list

        out["attributes"] = (
            aws_sdk_customer_profiles.types.attribute_list.deserialize_json(
                data["Attributes"]
            )
        )
    else:
        raise DeserializationError("AttributeDetails.attributes required")
    if "Expression" in data:
        out["expression"] = data["Expression"]
    else:
        raise DeserializationError("AttributeDetails.expression required")
    return out
