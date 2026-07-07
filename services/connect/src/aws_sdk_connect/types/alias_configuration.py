"""Generated from Smithy shape ``com.amazonaws.connect#AliasConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.email_address_id


class AliasConfiguration(TypedDict, closed=True):
    email_address_id: "aws_sdk_connect.types.email_address_id.EmailAddressId"
    """<p>The email address ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AliasConfiguration) -> dict:
    out: dict = {}
    out["EmailAddressId"] = value["email_address_id"]
    return out


def deserialize_json(data: dict) -> AliasConfiguration:
    out: AliasConfiguration = {}  # type: ignore[typeddict-item]
    if "EmailAddressId" in data:
        out["email_address_id"] = data["EmailAddressId"]
    else:
        raise DeserializationError("AliasConfiguration.email_address_id required")
    return out
