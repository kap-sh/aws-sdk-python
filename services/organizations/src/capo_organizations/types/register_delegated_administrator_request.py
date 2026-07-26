"""Generated from Smithy shape ``com.amazonaws.organizations#RegisterDelegatedAdministratorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_organizations.errors import DeserializationError

if TYPE_CHECKING:
    import capo_organizations.types.account_id
    import capo_organizations.types.service_principal


class RegisterDelegatedAdministratorRequest(TypedDict, closed=True):
    account_id: "capo_organizations.types.account_id.AccountId"
    """<p>The account ID number of the member account in the organization to register as a delegated administrator.</p>"""
    service_principal: "capo_organizations.types.service_principal.ServicePrincipal"
    """<p>The service principal of the Amazon Web Services service for which you want to make the member account a delegated administrator.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegisterDelegatedAdministratorRequest) -> dict:
    out: dict = {}
    out["AccountId"] = value["account_id"]
    out["ServicePrincipal"] = value["service_principal"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RegisterDelegatedAdministratorRequest:
    out: RegisterDelegatedAdministratorRequest = {}  # type: ignore[typeddict-item]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    else:
        raise DeserializationError(
            "RegisterDelegatedAdministratorRequest.account_id required"
        )
    if "ServicePrincipal" in data:
        out["service_principal"] = data["ServicePrincipal"]
    else:
        raise DeserializationError(
            "RegisterDelegatedAdministratorRequest.service_principal required"
        )
    return out
