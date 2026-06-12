"""Generated from Smithy shape ``com.amazonaws.guardduty#LoginAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.login_attribute

LoginAttributes: TypeAlias = list[
    "aws_sdk_guardduty.types.login_attribute.LoginAttribute"
]


# --- restJson1 ser/de ---
def serialize_json(value: LoginAttributes) -> list:
    import aws_sdk_guardduty.types.login_attribute

    out: list = []
    for item in value:
        out.append(aws_sdk_guardduty.types.login_attribute.serialize_json(item))
    return out


def deserialize_json(data: list) -> LoginAttributes:
    import aws_sdk_guardduty.types.login_attribute

    out: LoginAttributes = []
    for item in data:
        out.append(aws_sdk_guardduty.types.login_attribute.deserialize_json(item))
    return out
