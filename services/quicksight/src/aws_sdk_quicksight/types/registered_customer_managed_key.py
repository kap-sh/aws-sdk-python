"""Generated from Smithy shape ``com.amazonaws.quicksight#RegisteredCustomerManagedKey``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.boolean
    import aws_sdk_quicksight.types.string


class RegisteredCustomerManagedKey(TypedDict):
    key_arn: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The ARN of the KMS key that is registered to a Quick Sight account for encryption and decryption use.</p>"""
    default_key: "aws_sdk_quicksight.types.boolean.Boolean"
    """<p>Indicates whether a <code>RegisteredCustomerManagedKey</code> is set as the default key for encryption and decryption use.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisteredCustomerManagedKey) -> dict:
    out: dict = {}
    if "key_arn" in value:
        out["KeyArn"] = value["key_arn"]
    out["DefaultKey"] = value.get("default_key", False)
    return out


def deserialize_json(data: dict) -> RegisteredCustomerManagedKey:
    out: RegisteredCustomerManagedKey = {}  # type: ignore[typeddict-item]
    if "KeyArn" in data:
        out["key_arn"] = data["KeyArn"]
    if "DefaultKey" in data:
        out["default_key"] = data["DefaultKey"]
    else:
        out["default_key"] = False
    return out
