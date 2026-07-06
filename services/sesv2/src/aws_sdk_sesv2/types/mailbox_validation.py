"""Generated from Smithy shape ``com.amazonaws.sesv2#MailboxValidation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.email_address_insights_mailbox_evaluations
    import aws_sdk_sesv2.types.email_address_insights_verdict


class MailboxValidation(TypedDict, closed=True):
    is_valid: NotRequired[
        "aws_sdk_sesv2.types.email_address_insights_verdict.EmailAddressInsightsVerdict"
    ]
    """<p>Overall validity assessment with a conﬁdence verdict.</p>"""
    evaluations: NotRequired[
        "aws_sdk_sesv2.types.email_address_insights_mailbox_evaluations.EmailAddressInsightsMailboxEvaluations"
    ]
    """<p>Specific validation checks performed on the email address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MailboxValidation) -> dict:
    out: dict = {}
    if "is_valid" in value:
        import aws_sdk_sesv2.types.email_address_insights_verdict

        out["IsValid"] = (
            aws_sdk_sesv2.types.email_address_insights_verdict.serialize_json(
                value["is_valid"]
            )
        )
    if "evaluations" in value:
        import aws_sdk_sesv2.types.email_address_insights_mailbox_evaluations

        out["Evaluations"] = (
            aws_sdk_sesv2.types.email_address_insights_mailbox_evaluations.serialize_json(
                value["evaluations"]
            )
        )
    return out


def deserialize_json(data: dict) -> MailboxValidation:
    out: MailboxValidation = {}  # type: ignore[typeddict-item]
    if "IsValid" in data:
        import aws_sdk_sesv2.types.email_address_insights_verdict

        out["is_valid"] = (
            aws_sdk_sesv2.types.email_address_insights_verdict.deserialize_json(
                data["IsValid"]
            )
        )
    if "Evaluations" in data:
        import aws_sdk_sesv2.types.email_address_insights_mailbox_evaluations

        out["evaluations"] = (
            aws_sdk_sesv2.types.email_address_insights_mailbox_evaluations.deserialize_json(
                data["Evaluations"]
            )
        )
    return out
