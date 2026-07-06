"""Generated from Smithy shape ``com.amazonaws.b2bi#X12CodeListValidationRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_b2bi.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_b2bi.types.code_list
    import aws_sdk_b2bi.types.element_id


class X12CodeListValidationRule(TypedDict, closed=True):
    element_id: "aws_sdk_b2bi.types.element_id.ElementId"
    """<p>Specifies the four-digit element ID to which the code list modifications apply. This identifies which X12 element will have its allowed code values modified.</p>"""
    codes_to_add: NotRequired["aws_sdk_b2bi.types.code_list.CodeList"]
    """<p>Specifies a list of code values to add to the element's allowed values. These codes will be considered valid for the specified element in addition to the standard codes defined by the X12 specification.</p>"""
    codes_to_remove: NotRequired["aws_sdk_b2bi.types.code_list.CodeList"]
    """<p>Specifies a list of code values to remove from the element's allowed values. These codes will be considered invalid for the specified element, even if they are part of the standard codes defined by the X12 specification.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: X12CodeListValidationRule) -> dict:
    out: dict = {}
    out["elementId"] = value["element_id"]
    if "codes_to_add" in value:
        import aws_sdk_b2bi.types.code_list

        out["codesToAdd"] = aws_sdk_b2bi.types.code_list.serialize_aws_json_1_0(
            value["codes_to_add"]
        )
    if "codes_to_remove" in value:
        import aws_sdk_b2bi.types.code_list

        out["codesToRemove"] = aws_sdk_b2bi.types.code_list.serialize_aws_json_1_0(
            value["codes_to_remove"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> X12CodeListValidationRule:
    out: X12CodeListValidationRule = {}  # type: ignore[typeddict-item]
    if "elementId" in data:
        out["element_id"] = data["elementId"]
    else:
        raise DeserializationError("X12CodeListValidationRule.element_id required")
    if "codesToAdd" in data:
        import aws_sdk_b2bi.types.code_list

        out["codes_to_add"] = aws_sdk_b2bi.types.code_list.deserialize_aws_json_1_0(
            data["codesToAdd"]
        )
    if "codesToRemove" in data:
        import aws_sdk_b2bi.types.code_list

        out["codes_to_remove"] = aws_sdk_b2bi.types.code_list.deserialize_aws_json_1_0(
            data["codesToRemove"]
        )
    return out
