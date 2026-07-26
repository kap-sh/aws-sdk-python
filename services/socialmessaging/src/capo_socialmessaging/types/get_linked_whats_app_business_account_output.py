"""Generated from Smithy shape ``com.amazonaws.socialmessaging#GetLinkedWhatsAppBusinessAccountOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_socialmessaging.types.linked_whats_app_business_account


class GetLinkedWhatsAppBusinessAccountOutput(TypedDict, closed=True):
    account: NotRequired[
        "capo_socialmessaging.types.linked_whats_app_business_account.LinkedWhatsAppBusinessAccount"
    ]
    """<p>The details of the linked WhatsApp Business Account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLinkedWhatsAppBusinessAccountOutput) -> dict:
    out: dict = {}
    if "account" in value:
        import capo_socialmessaging.types.linked_whats_app_business_account

        out["account"] = (
            capo_socialmessaging.types.linked_whats_app_business_account.serialize_json(
                value["account"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetLinkedWhatsAppBusinessAccountOutput:
    out: GetLinkedWhatsAppBusinessAccountOutput = {}  # type: ignore[typeddict-item]
    if "account" in data:
        import capo_socialmessaging.types.linked_whats_app_business_account

        out["account"] = (
            capo_socialmessaging.types.linked_whats_app_business_account.deserialize_json(
                data["account"]
            )
        )
    return out
