"""Generated from Smithy shape ``com.amazonaws.guardduty#LoginAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.login_attribute

LoginAttributes: TypeAlias = list["capo_guardduty.types.login_attribute.LoginAttribute"]


# --- restJson1 ser/de ---
def serialize_json(value: LoginAttributes) -> list:
    import capo_guardduty.types.login_attribute

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.login_attribute.serialize_json(item))
    return out


def deserialize_json(data: list) -> LoginAttributes:
    import capo_guardduty.types.login_attribute

    out: LoginAttributes = []
    for item in data:
        out.append(capo_guardduty.types.login_attribute.deserialize_json(item))
    return out
