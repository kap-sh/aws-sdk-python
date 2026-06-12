"""Generated from Smithy shape ``com.amazonaws.b2bi#X12ElementLengthValidationRule``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_b2bi.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_b2bi.types.element_id


class X12ElementLengthValidationRule(TypedDict):
    element_id: "aws_sdk_b2bi.types.element_id.ElementId"
    """<p>Specifies the four-digit element ID to which the length constraints will be applied. This identifies which X12 element will have its length requirements modified.</p>"""
    max_length: "int"
    """<p>Specifies the maximum allowed length for the identified element. This value must be between 1 and 200 characters and defines the upper limit for the element's content length.</p>"""
    min_length: "int"
    """<p>Specifies the minimum required length for the identified element. This value must be between 1 and 200 characters and defines the lower limit for the element's content length.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: X12ElementLengthValidationRule) -> dict:
    out: dict = {}
    out["elementId"] = value["element_id"]
    out["maxLength"] = value["max_length"]
    out["minLength"] = value["min_length"]
    return out


def deserialize_aws_json_1_0(data: dict) -> X12ElementLengthValidationRule:
    out: X12ElementLengthValidationRule = {}  # type: ignore[typeddict-item]
    if "elementId" in data:
        out["element_id"] = data["elementId"]
    else:
        raise DeserializationError("X12ElementLengthValidationRule.element_id required")
    if "maxLength" in data:
        out["max_length"] = data["maxLength"]
    else:
        raise DeserializationError("X12ElementLengthValidationRule.max_length required")
    if "minLength" in data:
        out["min_length"] = data["minLength"]
    else:
        raise DeserializationError("X12ElementLengthValidationRule.min_length required")
    return out
