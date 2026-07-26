"""Generated from Smithy shape ``com.amazonaws.connect#AdditionalEmailRecipients``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.email_recipients_list


class AdditionalEmailRecipients(TypedDict, closed=True):
    to_list: NotRequired["capo_connect.types.email_recipients_list.EmailRecipientsList"]
    """<p>List of additional TO email recipients for an email contact.</p>"""
    cc_list: NotRequired["capo_connect.types.email_recipients_list.EmailRecipientsList"]
    """<p>List of additional CC email recipients for an email contact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AdditionalEmailRecipients) -> dict:
    out: dict = {}
    if "to_list" in value:
        import capo_connect.types.email_recipients_list

        out["ToList"] = capo_connect.types.email_recipients_list.serialize_json(
            value["to_list"]
        )
    if "cc_list" in value:
        import capo_connect.types.email_recipients_list

        out["CcList"] = capo_connect.types.email_recipients_list.serialize_json(
            value["cc_list"]
        )
    return out


def deserialize_json(data: dict) -> AdditionalEmailRecipients:
    out: AdditionalEmailRecipients = {}  # type: ignore[typeddict-item]
    if "ToList" in data:
        import capo_connect.types.email_recipients_list

        out["to_list"] = capo_connect.types.email_recipients_list.deserialize_json(
            data["ToList"]
        )
    if "CcList" in data:
        import capo_connect.types.email_recipients_list

        out["cc_list"] = capo_connect.types.email_recipients_list.deserialize_json(
            data["CcList"]
        )
    return out
