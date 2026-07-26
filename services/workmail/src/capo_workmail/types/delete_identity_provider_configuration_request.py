"""Generated from Smithy shape ``com.amazonaws.workmail#DeleteIdentityProviderConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workmail.types.organization_id


class DeleteIdentityProviderConfigurationRequest(TypedDict, closed=True):
    organization_id: "capo_workmail.types.organization_id.OrganizationId"
    """<p> The Organization ID. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteIdentityProviderConfigurationRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteIdentityProviderConfigurationRequest:
    out: DeleteIdentityProviderConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    else:
        raise DeserializationError(
            "DeleteIdentityProviderConfigurationRequest.organization_id required"
        )
    return out
