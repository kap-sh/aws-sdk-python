"""Generated from Smithy shape ``com.amazonaws.sesv2#EmailAddressInsightsMailboxEvaluations``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.email_address_insights_verdict


class EmailAddressInsightsMailboxEvaluations(TypedDict, closed=True):
    has_valid_syntax: NotRequired[
        "capo_sesv2.types.email_address_insights_verdict.EmailAddressInsightsVerdict"
    ]
    """<p>Checks that the email address follows proper RFC standards and contains valid characters in the correct format.</p>"""
    has_valid_dns_records: NotRequired[
        "capo_sesv2.types.email_address_insights_verdict.EmailAddressInsightsVerdict"
    ]
    """<p>Checks that the domain exists, has valid DNS records, and is conﬁgured to receive email.</p>"""
    mailbox_exists: NotRequired[
        "capo_sesv2.types.email_address_insights_verdict.EmailAddressInsightsVerdict"
    ]
    """<p>Checks that the mailbox exists and can receive messages without actually sending an email.</p>"""
    is_role_address: NotRequired[
        "capo_sesv2.types.email_address_insights_verdict.EmailAddressInsightsVerdict"
    ]
    """<p>Identiﬁes role-based addresses (such as admin@, support@, or info@) that may have lower engagement rates.</p>"""
    is_disposable: NotRequired[
        "capo_sesv2.types.email_address_insights_verdict.EmailAddressInsightsVerdict"
    ]
    """<p>Checks disposable or temporary email addresses that could negatively impact your sender reputation.</p>"""
    is_random_input: NotRequired[
        "capo_sesv2.types.email_address_insights_verdict.EmailAddressInsightsVerdict"
    ]
    """<p>Checks if the input appears to be random text.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EmailAddressInsightsMailboxEvaluations) -> dict:
    out: dict = {}
    if "has_valid_syntax" in value:
        import capo_sesv2.types.email_address_insights_verdict

        out["HasValidSyntax"] = (
            capo_sesv2.types.email_address_insights_verdict.serialize_json(
                value["has_valid_syntax"]
            )
        )
    if "has_valid_dns_records" in value:
        import capo_sesv2.types.email_address_insights_verdict

        out["HasValidDnsRecords"] = (
            capo_sesv2.types.email_address_insights_verdict.serialize_json(
                value["has_valid_dns_records"]
            )
        )
    if "mailbox_exists" in value:
        import capo_sesv2.types.email_address_insights_verdict

        out["MailboxExists"] = (
            capo_sesv2.types.email_address_insights_verdict.serialize_json(
                value["mailbox_exists"]
            )
        )
    if "is_role_address" in value:
        import capo_sesv2.types.email_address_insights_verdict

        out["IsRoleAddress"] = (
            capo_sesv2.types.email_address_insights_verdict.serialize_json(
                value["is_role_address"]
            )
        )
    if "is_disposable" in value:
        import capo_sesv2.types.email_address_insights_verdict

        out["IsDisposable"] = (
            capo_sesv2.types.email_address_insights_verdict.serialize_json(
                value["is_disposable"]
            )
        )
    if "is_random_input" in value:
        import capo_sesv2.types.email_address_insights_verdict

        out["IsRandomInput"] = (
            capo_sesv2.types.email_address_insights_verdict.serialize_json(
                value["is_random_input"]
            )
        )
    return out


def deserialize_json(data: dict) -> EmailAddressInsightsMailboxEvaluations:
    out: EmailAddressInsightsMailboxEvaluations = {}  # type: ignore[typeddict-item]
    if "HasValidSyntax" in data:
        import capo_sesv2.types.email_address_insights_verdict

        out["has_valid_syntax"] = (
            capo_sesv2.types.email_address_insights_verdict.deserialize_json(
                data["HasValidSyntax"]
            )
        )
    if "HasValidDnsRecords" in data:
        import capo_sesv2.types.email_address_insights_verdict

        out["has_valid_dns_records"] = (
            capo_sesv2.types.email_address_insights_verdict.deserialize_json(
                data["HasValidDnsRecords"]
            )
        )
    if "MailboxExists" in data:
        import capo_sesv2.types.email_address_insights_verdict

        out["mailbox_exists"] = (
            capo_sesv2.types.email_address_insights_verdict.deserialize_json(
                data["MailboxExists"]
            )
        )
    if "IsRoleAddress" in data:
        import capo_sesv2.types.email_address_insights_verdict

        out["is_role_address"] = (
            capo_sesv2.types.email_address_insights_verdict.deserialize_json(
                data["IsRoleAddress"]
            )
        )
    if "IsDisposable" in data:
        import capo_sesv2.types.email_address_insights_verdict

        out["is_disposable"] = (
            capo_sesv2.types.email_address_insights_verdict.deserialize_json(
                data["IsDisposable"]
            )
        )
    if "IsRandomInput" in data:
        import capo_sesv2.types.email_address_insights_verdict

        out["is_random_input"] = (
            capo_sesv2.types.email_address_insights_verdict.deserialize_json(
                data["IsRandomInput"]
            )
        )
    return out
