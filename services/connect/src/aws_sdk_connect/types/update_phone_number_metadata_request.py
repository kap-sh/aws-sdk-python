"""Generated from Smithy shape ``com.amazonaws.connect#UpdatePhoneNumberMetadataRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.client_token
    import aws_sdk_connect.types.phone_number_description
    import aws_sdk_connect.types.phone_number_id


class UpdatePhoneNumberMetadataRequest(TypedDict):
    phone_number_id: "aws_sdk_connect.types.phone_number_id.PhoneNumberId"
    """<p>The Amazon Resource Name (ARN) or resource ID of the phone number.</p>"""
    phone_number_description: NotRequired[
        "aws_sdk_connect.types.phone_number_description.PhoneNumberDescription"
    ]
    """<p>The description of the phone number.</p>"""
    client_token: NotRequired["aws_sdk_connect.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href=\"https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\">Making retries safe with idempotent APIs</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePhoneNumberMetadataRequest) -> dict:
    out: dict = {}
    if "phone_number_description" in value:
        out["PhoneNumberDescription"] = value["phone_number_description"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdatePhoneNumberMetadataRequest:
    out: UpdatePhoneNumberMetadataRequest = {}  # type: ignore[typeddict-item]
    if "PhoneNumberDescription" in data:
        out["phone_number_description"] = data["PhoneNumberDescription"]
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out
