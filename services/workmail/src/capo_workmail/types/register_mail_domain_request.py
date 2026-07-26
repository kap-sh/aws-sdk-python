"""Generated from Smithy shape ``com.amazonaws.workmail#RegisterMailDomainRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workmail.types.idempotency_client_token
    import capo_workmail.types.organization_id
    import capo_workmail.types.work_mail_domain_name


class RegisterMailDomainRequest(TypedDict, closed=True):
    client_token: NotRequired[
        "capo_workmail.types.idempotency_client_token.IdempotencyClientToken"
    ]
    """<p>Idempotency token used when retrying requests.</p>"""
    organization_id: "capo_workmail.types.organization_id.OrganizationId"
    """<p>The WorkMail organization under which you're creating the domain.</p>"""
    domain_name: "capo_workmail.types.work_mail_domain_name.WorkMailDomainName"
    """<p>The name of the mail domain to create in WorkMail and SES.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegisterMailDomainRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["OrganizationId"] = value["organization_id"]
    out["DomainName"] = value["domain_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RegisterMailDomainRequest:
    out: RegisterMailDomainRequest = {}  # type: ignore[typeddict-item]
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    else:
        raise DeserializationError("RegisterMailDomainRequest.organization_id required")
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    else:
        raise DeserializationError("RegisterMailDomainRequest.domain_name required")
    return out
