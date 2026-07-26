"""Generated from Smithy shape ``com.amazonaws.workmail#MailDomains``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workmail.types.mail_domain_summary

MailDomains: TypeAlias = list[
    "capo_workmail.types.mail_domain_summary.MailDomainSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MailDomains) -> list:
    import capo_workmail.types.mail_domain_summary

    out: list = []
    for item in value:
        out.append(capo_workmail.types.mail_domain_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> MailDomains:
    import capo_workmail.types.mail_domain_summary

    out: MailDomains = []
    for item in data:
        out.append(
            capo_workmail.types.mail_domain_summary.deserialize_aws_json_1_1(item)
        )
    return out
