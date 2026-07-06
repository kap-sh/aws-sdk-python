"""Generated from Smithy shape ``com.amazonaws.odb#CustomerContact``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_odb.types.sensitive_string


class CustomerContact(TypedDict, closed=True):
    email: NotRequired["aws_sdk_odb.types.sensitive_string.SensitiveString"]
    """<p>The email address of the contact.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CustomerContact) -> dict:
    out: dict = {}
    if "email" in value:
        out["email"] = value["email"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CustomerContact:
    out: CustomerContact = {}  # type: ignore[typeddict-item]
    if "email" in data:
        out["email"] = data["email"]
    return out
