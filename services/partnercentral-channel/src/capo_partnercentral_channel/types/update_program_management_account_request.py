"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#UpdateProgramManagementAccountRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_channel.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_channel.types.catalog
    import capo_partnercentral_channel.types.program_management_account_display_name
    import capo_partnercentral_channel.types.program_management_account_identifier
    import capo_partnercentral_channel.types.revision


class UpdateProgramManagementAccountRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_channel.types.catalog.Catalog"
    """<p>The catalog identifier for the program management account.</p>"""
    identifier: "capo_partnercentral_channel.types.program_management_account_identifier.ProgramManagementAccountIdentifier"
    """<p>The unique identifier of the program management account to update.</p>"""
    revision: NotRequired["capo_partnercentral_channel.types.revision.Revision"]
    """<p>The current revision number of the program management account.</p>"""
    display_name: NotRequired[
        "capo_partnercentral_channel.types.program_management_account_display_name.ProgramManagementAccountDisplayName"
    ]
    """<p>The new display name for the program management account.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateProgramManagementAccountRequest) -> dict:
    out: dict = {}
    out["catalog"] = value["catalog"]
    out["identifier"] = value["identifier"]
    if "revision" in value:
        out["revision"] = value["revision"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateProgramManagementAccountRequest:
    out: UpdateProgramManagementAccountRequest = {}  # type: ignore[typeddict-item]
    if "catalog" in data:
        out["catalog"] = data["catalog"]
    else:
        raise DeserializationError(
            "UpdateProgramManagementAccountRequest.catalog required"
        )
    if "identifier" in data:
        out["identifier"] = data["identifier"]
    else:
        raise DeserializationError(
            "UpdateProgramManagementAccountRequest.identifier required"
        )
    if "revision" in data:
        out["revision"] = data["revision"]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    return out
