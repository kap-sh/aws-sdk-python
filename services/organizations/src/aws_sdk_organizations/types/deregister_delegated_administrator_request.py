"""Generated from Smithy shape ``com.amazonaws.organizations#DeregisterDelegatedAdministratorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_organizations.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_organizations.types.account_id
    import aws_sdk_organizations.types.service_principal


class DeregisterDelegatedAdministratorRequest(TypedDict, closed=True):
    account_id: "aws_sdk_organizations.types.account_id.AccountId"
    """<p>The account ID number of the member account in the organization that you want to deregister as a delegated administrator.</p>"""
    service_principal: "aws_sdk_organizations.types.service_principal.ServicePrincipal"
    """<p>The service principal name of an Amazon Web Services service for which the account is a delegated administrator.</p> <p>Delegated administrator privileges are revoked for only the specified Amazon Web Services service from the member account. If the specified service is the only service for which the member account is a delegated administrator, the operation also revokes Organizations read action permissions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeregisterDelegatedAdministratorRequest) -> dict:
    out: dict = {}
    out["AccountId"] = value["account_id"]
    out["ServicePrincipal"] = value["service_principal"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeregisterDelegatedAdministratorRequest:
    out: DeregisterDelegatedAdministratorRequest = {}  # type: ignore[typeddict-item]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    else:
        raise DeserializationError(
            "DeregisterDelegatedAdministratorRequest.account_id required"
        )
    if "ServicePrincipal" in data:
        out["service_principal"] = data["ServicePrincipal"]
    else:
        raise DeserializationError(
            "DeregisterDelegatedAdministratorRequest.service_principal required"
        )
    return out
