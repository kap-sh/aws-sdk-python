"""Generated from Smithy shape ``com.amazonaws.identitystore#Email``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_identitystore.types.boolean_type
    import aws_sdk_identitystore.types.sensitive_string_type


class Email(TypedDict):
    value: NotRequired[
        "aws_sdk_identitystore.types.sensitive_string_type.SensitiveStringType"
    ]
    """<p>A string containing an email address. For example, \"johndoe@amazon.com.\"</p>"""
    type: NotRequired[
        "aws_sdk_identitystore.types.sensitive_string_type.SensitiveStringType"
    ]
    """<p>A string representing the type of address. For example, \"Work.\"</p>"""
    primary: "aws_sdk_identitystore.types.boolean_type.BooleanType"
    """<p>A Boolean value representing whether this is the primary email address for the associated resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Email) -> dict:
    out: dict = {}
    if "value" in value:
        out["Value"] = value["value"]
    if "type" in value:
        out["Type"] = value["type"]
    out["Primary"] = value.get("primary", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> Email:
    out: Email = {}  # type: ignore[typeddict-item]
    if "Value" in data:
        out["value"] = data["Value"]
    if "Type" in data:
        out["type"] = data["Type"]
    if "Primary" in data:
        out["primary"] = data["Primary"]
    else:
        out["primary"] = False
    return out
