"""Generated from Smithy shape ``com.amazonaws.workmail#ListMailDomainsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.mail_domains
    import capo_workmail.types.next_token


class ListMailDomainsResponse(TypedDict, closed=True):
    mail_domains: NotRequired["capo_workmail.types.mail_domains.MailDomains"]
    """<p>The list of mail domain summaries, specifying domains that exist in the specified WorkMail organization, along with the information about whether the domain is or isn't the default.</p>"""
    next_token: NotRequired["capo_workmail.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. The value becomes <code>null</code> when there are no more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListMailDomainsResponse) -> dict:
    out: dict = {}
    if "mail_domains" in value:
        import capo_workmail.types.mail_domains

        out["MailDomains"] = capo_workmail.types.mail_domains.serialize_aws_json_1_1(
            value["mail_domains"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListMailDomainsResponse:
    out: ListMailDomainsResponse = {}  # type: ignore[typeddict-item]
    if "MailDomains" in data:
        import capo_workmail.types.mail_domains

        out["mail_domains"] = capo_workmail.types.mail_domains.deserialize_aws_json_1_1(
            data["MailDomains"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
