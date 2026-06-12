"""Generated from Smithy shape ``com.amazonaws.sesv2#EmailAddressInsightsMailboxEvaluations``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.email_address_insights_verdict


class EmailAddressInsightsMailboxEvaluations(TypedDict):
    has_valid_syntax: NotRequired[
        "aws_sdk_sesv2.types.email_address_insights_verdict.EmailAddressInsightsVerdict"
    ]
    """<p>Checks that the email address follows proper RFC standards and contains valid characters in the correct format.</p>"""
    has_valid_dns_records: NotRequired[
        "aws_sdk_sesv2.types.email_address_insights_verdict.EmailAddressInsightsVerdict"
    ]
    """<p>Checks that the domain exists, has valid DNS records, and is conﬁgured to receive email.</p>"""
    mailbox_exists: NotRequired[
        "aws_sdk_sesv2.types.email_address_insights_verdict.EmailAddressInsightsVerdict"
    ]
    """<p>Checks that the mailbox exists and can receive messages without actually sending an email.</p>"""
    is_role_address: NotRequired[
        "aws_sdk_sesv2.types.email_address_insights_verdict.EmailAddressInsightsVerdict"
    ]
    """<p>Identiﬁes role-based addresses (such as admin@, support@, or info@) that may have lower engagement rates.</p>"""
    is_disposable: NotRequired[
        "aws_sdk_sesv2.types.email_address_insights_verdict.EmailAddressInsightsVerdict"
    ]
    """<p>Checks disposable or temporary email addresses that could negatively impact your sender reputation.</p>"""
    is_random_input: NotRequired[
        "aws_sdk_sesv2.types.email_address_insights_verdict.EmailAddressInsightsVerdict"
    ]
    """<p>Checks if the input appears to be random text.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EmailAddressInsightsMailboxEvaluations) -> dict:
    out: dict = {}
    if "has_valid_syntax" in value:
        import aws_sdk_sesv2.types.email_address_insights_verdict

        out["HasValidSyntax"] = (
            aws_sdk_sesv2.types.email_address_insights_verdict.serialize_json(
                value["has_valid_syntax"]
            )
        )
    if "has_valid_dns_records" in value:
        import aws_sdk_sesv2.types.email_address_insights_verdict

        out["HasValidDnsRecords"] = (
            aws_sdk_sesv2.types.email_address_insights_verdict.serialize_json(
                value["has_valid_dns_records"]
            )
        )
    if "mailbox_exists" in value:
        import aws_sdk_sesv2.types.email_address_insights_verdict

        out["MailboxExists"] = (
            aws_sdk_sesv2.types.email_address_insights_verdict.serialize_json(
                value["mailbox_exists"]
            )
        )
    if "is_role_address" in value:
        import aws_sdk_sesv2.types.email_address_insights_verdict

        out["IsRoleAddress"] = (
            aws_sdk_sesv2.types.email_address_insights_verdict.serialize_json(
                value["is_role_address"]
            )
        )
    if "is_disposable" in value:
        import aws_sdk_sesv2.types.email_address_insights_verdict

        out["IsDisposable"] = (
            aws_sdk_sesv2.types.email_address_insights_verdict.serialize_json(
                value["is_disposable"]
            )
        )
    if "is_random_input" in value:
        import aws_sdk_sesv2.types.email_address_insights_verdict

        out["IsRandomInput"] = (
            aws_sdk_sesv2.types.email_address_insights_verdict.serialize_json(
                value["is_random_input"]
            )
        )
    return out


def deserialize_json(data: dict) -> EmailAddressInsightsMailboxEvaluations:
    out: EmailAddressInsightsMailboxEvaluations = {}  # type: ignore[typeddict-item]
    if "HasValidSyntax" in data:
        import aws_sdk_sesv2.types.email_address_insights_verdict

        out["has_valid_syntax"] = (
            aws_sdk_sesv2.types.email_address_insights_verdict.deserialize_json(
                data["HasValidSyntax"]
            )
        )
    if "HasValidDnsRecords" in data:
        import aws_sdk_sesv2.types.email_address_insights_verdict

        out["has_valid_dns_records"] = (
            aws_sdk_sesv2.types.email_address_insights_verdict.deserialize_json(
                data["HasValidDnsRecords"]
            )
        )
    if "MailboxExists" in data:
        import aws_sdk_sesv2.types.email_address_insights_verdict

        out["mailbox_exists"] = (
            aws_sdk_sesv2.types.email_address_insights_verdict.deserialize_json(
                data["MailboxExists"]
            )
        )
    if "IsRoleAddress" in data:
        import aws_sdk_sesv2.types.email_address_insights_verdict

        out["is_role_address"] = (
            aws_sdk_sesv2.types.email_address_insights_verdict.deserialize_json(
                data["IsRoleAddress"]
            )
        )
    if "IsDisposable" in data:
        import aws_sdk_sesv2.types.email_address_insights_verdict

        out["is_disposable"] = (
            aws_sdk_sesv2.types.email_address_insights_verdict.deserialize_json(
                data["IsDisposable"]
            )
        )
    if "IsRandomInput" in data:
        import aws_sdk_sesv2.types.email_address_insights_verdict

        out["is_random_input"] = (
            aws_sdk_sesv2.types.email_address_insights_verdict.deserialize_json(
                data["IsRandomInput"]
            )
        )
    return out
