"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#NumberAttributeConstraintsType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.string_type


class NumberAttributeConstraintsType(TypedDict, closed=True):
    min_value: NotRequired[
        "aws_sdk_cognito_identity_provider.types.string_type.StringType"
    ]
    """<p>The minimum value of an attribute that is of the number data type.</p>"""
    max_value: NotRequired[
        "aws_sdk_cognito_identity_provider.types.string_type.StringType"
    ]
    """<p>The maximum length of a number attribute value. Must be a number less than or equal to <code>2^1023</code>, represented as a string with a length of 131072 characters or fewer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NumberAttributeConstraintsType) -> dict:
    out: dict = {}
    if "min_value" in value:
        out["MinValue"] = value["min_value"]
    if "max_value" in value:
        out["MaxValue"] = value["max_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NumberAttributeConstraintsType:
    out: NumberAttributeConstraintsType = {}  # type: ignore[typeddict-item]
    if "MinValue" in data:
        out["min_value"] = data["MinValue"]
    if "MaxValue" in data:
        out["max_value"] = data["MaxValue"]
    return out
