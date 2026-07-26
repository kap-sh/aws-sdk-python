"""Generated from Smithy shape ``com.amazonaws.organizations#InviteOrganizationToTransferResponsibilityResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_organizations.types.handshake


class InviteOrganizationToTransferResponsibilityResponse(TypedDict, closed=True):
    handshake: NotRequired["capo_organizations.types.handshake.Handshake"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: InviteOrganizationToTransferResponsibilityResponse,
) -> dict:
    out: dict = {}
    if "handshake" in value:
        import capo_organizations.types.handshake

        out["Handshake"] = capo_organizations.types.handshake.serialize_aws_json_1_1(
            value["handshake"]
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> InviteOrganizationToTransferResponsibilityResponse:
    out: InviteOrganizationToTransferResponsibilityResponse = {}  # type: ignore[typeddict-item]
    if "Handshake" in data:
        import capo_organizations.types.handshake

        out["handshake"] = capo_organizations.types.handshake.deserialize_aws_json_1_1(
            data["Handshake"]
        )
    return out
