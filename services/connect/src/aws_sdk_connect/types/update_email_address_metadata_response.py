"""Generated from Smithy shape ``com.amazonaws.connect#UpdateEmailAddressMetadataResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.email_address_arn
    import aws_sdk_connect.types.email_address_id


class UpdateEmailAddressMetadataResponse(TypedDict):
    email_address_id: NotRequired[
        "aws_sdk_connect.types.email_address_id.EmailAddressId"
    ]
    """<p>The identifier of the email address.</p>"""
    email_address_arn: NotRequired[
        "aws_sdk_connect.types.email_address_arn.EmailAddressArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the email address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEmailAddressMetadataResponse) -> dict:
    out: dict = {}
    if "email_address_id" in value:
        out["EmailAddressId"] = value["email_address_id"]
    if "email_address_arn" in value:
        out["EmailAddressArn"] = value["email_address_arn"]
    return out


def deserialize_json(data: dict) -> UpdateEmailAddressMetadataResponse:
    out: UpdateEmailAddressMetadataResponse = {}  # type: ignore[typeddict-item]
    if "EmailAddressId" in data:
        out["email_address_id"] = data["EmailAddressId"]
    if "EmailAddressArn" in data:
        out["email_address_arn"] = data["EmailAddressArn"]
    return out
