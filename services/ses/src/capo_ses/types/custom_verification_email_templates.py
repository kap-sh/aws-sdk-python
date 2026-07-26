"""Generated from Smithy shape ``com.amazonaws.ses#CustomVerificationEmailTemplates``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.custom_verification_email_template

CustomVerificationEmailTemplates: TypeAlias = list[
    "capo_ses.types.custom_verification_email_template.CustomVerificationEmailTemplate"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: CustomVerificationEmailTemplates, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_ses.types.custom_verification_email_template

    for n, item in enumerate(value, 1):
        capo_ses.types.custom_verification_email_template.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> CustomVerificationEmailTemplates:
    import capo_ses.types.custom_verification_email_template

    out: CustomVerificationEmailTemplates = []
    for child in el.findall("member"):
        out.append(
            capo_ses.types.custom_verification_email_template.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: CustomVerificationEmailTemplates, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_ses.types.custom_verification_email_template

    for n, item in enumerate(value, 1):
        capo_ses.types.custom_verification_email_template.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(
    parent: Element, tag: str
) -> CustomVerificationEmailTemplates:
    import capo_ses.types.custom_verification_email_template

    out: CustomVerificationEmailTemplates = []
    for child in parent.findall(tag):
        out.append(
            capo_ses.types.custom_verification_email_template.deserialize_query(child)
        )
    return out
