"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#DeleteProgramManagementAccountRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_partnercentral_channel.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_channel.types.catalog
    import aws_sdk_partnercentral_channel.types.client_token
    import aws_sdk_partnercentral_channel.types.program_management_account_identifier


class DeleteProgramManagementAccountRequest(TypedDict):
    catalog: "aws_sdk_partnercentral_channel.types.catalog.Catalog"
    """<p>The catalog identifier for the program management account.</p>"""
    identifier: "aws_sdk_partnercentral_channel.types.program_management_account_identifier.ProgramManagementAccountIdentifier"
    """<p>The unique identifier of the program management account to delete.</p>"""
    client_token: NotRequired[
        "aws_sdk_partnercentral_channel.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteProgramManagementAccountRequest) -> dict:
    out: dict = {}
    out["catalog"] = value["catalog"]
    out["identifier"] = value["identifier"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteProgramManagementAccountRequest:
    out: DeleteProgramManagementAccountRequest = {}  # type: ignore[typeddict-item]
    if "catalog" in data:
        out["catalog"] = data["catalog"]
    else:
        raise DeserializationError(
            "DeleteProgramManagementAccountRequest.catalog required"
        )
    if "identifier" in data:
        out["identifier"] = data["identifier"]
    else:
        raise DeserializationError(
            "DeleteProgramManagementAccountRequest.identifier required"
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
