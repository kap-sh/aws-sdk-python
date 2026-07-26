"""Generated from Smithy shape ``com.amazonaws.workmail#DeletePersonalAccessTokenRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workmail.types.organization_id
    import capo_workmail.types.personal_access_token_id


class DeletePersonalAccessTokenRequest(TypedDict, closed=True):
    organization_id: "capo_workmail.types.organization_id.OrganizationId"
    """<p> The Organization ID. </p>"""
    personal_access_token_id: (
        "capo_workmail.types.personal_access_token_id.PersonalAccessTokenId"
    )
    """<p> The Personal Access Token ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeletePersonalAccessTokenRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    out["PersonalAccessTokenId"] = value["personal_access_token_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeletePersonalAccessTokenRequest:
    out: DeletePersonalAccessTokenRequest = {}  # type: ignore[typeddict-item]
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    else:
        raise DeserializationError(
            "DeletePersonalAccessTokenRequest.organization_id required"
        )
    if "PersonalAccessTokenId" in data:
        out["personal_access_token_id"] = data["PersonalAccessTokenId"]
    else:
        raise DeserializationError(
            "DeletePersonalAccessTokenRequest.personal_access_token_id required"
        )
    return out
