"""Generated from Smithy shape ``com.amazonaws.socialmessaging#GetLinkedWhatsAppBusinessAccountOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_socialmessaging.types.linked_whats_app_business_account


class GetLinkedWhatsAppBusinessAccountOutput(TypedDict):
    account: NotRequired[
        "aws_sdk_socialmessaging.types.linked_whats_app_business_account.LinkedWhatsAppBusinessAccount"
    ]
    """<p>The details of the linked WhatsApp Business Account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLinkedWhatsAppBusinessAccountOutput) -> dict:
    out: dict = {}
    if "account" in value:
        import aws_sdk_socialmessaging.types.linked_whats_app_business_account

        out["account"] = (
            aws_sdk_socialmessaging.types.linked_whats_app_business_account.serialize_json(
                value["account"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetLinkedWhatsAppBusinessAccountOutput:
    out: GetLinkedWhatsAppBusinessAccountOutput = {}  # type: ignore[typeddict-item]
    if "account" in data:
        import aws_sdk_socialmessaging.types.linked_whats_app_business_account

        out["account"] = (
            aws_sdk_socialmessaging.types.linked_whats_app_business_account.deserialize_json(
                data["account"]
            )
        )
    return out
