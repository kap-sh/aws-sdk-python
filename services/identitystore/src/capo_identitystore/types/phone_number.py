"""Generated from Smithy shape ``com.amazonaws.identitystore#PhoneNumber``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_identitystore.types.boolean_type
    import capo_identitystore.types.sensitive_string_type


class PhoneNumber(TypedDict, closed=True):
    value: NotRequired[
        "capo_identitystore.types.sensitive_string_type.SensitiveStringType"
    ]
    r"""<p>A string containing a phone number. For example, \"8675309\" or \"+1 (800) 123-4567\". </p>"""
    type: NotRequired[
        "capo_identitystore.types.sensitive_string_type.SensitiveStringType"
    ]
    r"""<p>A string representing the type of a phone number. For example, \"Mobile.\"</p>"""
    primary: "capo_identitystore.types.boolean_type.BooleanType"
    """<p>A Boolean value representing whether this is the primary phone number for the associated resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PhoneNumber) -> dict:
    out: dict = {}
    if "value" in value:
        out["Value"] = value["value"]
    if "type" in value:
        out["Type"] = value["type"]
    out["Primary"] = value.get("primary", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> PhoneNumber:
    out: PhoneNumber = {}  # type: ignore[typeddict-item]
    if "Value" in data:
        out["value"] = data["Value"]
    if "Type" in data:
        out["type"] = data["Type"]
    if "Primary" in data:
        out["primary"] = data["Primary"]
    else:
        out["primary"] = False
    return out
