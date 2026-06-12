"""Generated from Smithy shape ``com.amazonaws.organizations#InviteOrganizationToTransferResponsibilityResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_organizations.types.handshake


class InviteOrganizationToTransferResponsibilityResponse(TypedDict):
    handshake: NotRequired["aws_sdk_organizations.types.handshake.Handshake"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: InviteOrganizationToTransferResponsibilityResponse,
) -> dict:
    out: dict = {}
    if "handshake" in value:
        import aws_sdk_organizations.types.handshake

        out["Handshake"] = aws_sdk_organizations.types.handshake.serialize_aws_json_1_1(
            value["handshake"]
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> InviteOrganizationToTransferResponsibilityResponse:
    out: InviteOrganizationToTransferResponsibilityResponse = {}  # type: ignore[typeddict-item]
    if "Handshake" in data:
        import aws_sdk_organizations.types.handshake

        out["handshake"] = (
            aws_sdk_organizations.types.handshake.deserialize_aws_json_1_1(
                data["Handshake"]
            )
        )
    return out
