"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#StringAttributeConstraintsType``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.string_type


class StringAttributeConstraintsType(TypedDict):
    min_length: NotRequired[
        "aws_sdk_cognito_identity_provider.types.string_type.StringType"
    ]
    """<p>The minimum length of a string attribute value.</p>"""
    max_length: NotRequired[
        "aws_sdk_cognito_identity_provider.types.string_type.StringType"
    ]
    """<p>The maximum length of a string attribute value. Must be a number less than or equal to <code>2^1023</code>, represented as a string with a length of 131072 characters or fewer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StringAttributeConstraintsType) -> dict:
    out: dict = {}
    if "min_length" in value:
        out["MinLength"] = value["min_length"]
    if "max_length" in value:
        out["MaxLength"] = value["max_length"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StringAttributeConstraintsType:
    out: StringAttributeConstraintsType = {}  # type: ignore[typeddict-item]
    if "MinLength" in data:
        out["min_length"] = data["MinLength"]
    if "MaxLength" in data:
        out["max_length"] = data["MaxLength"]
    return out
