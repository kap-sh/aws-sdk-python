"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#CreateProgramManagementAccountRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_channel.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_channel.types.account_id
    import capo_partnercentral_channel.types.catalog
    import capo_partnercentral_channel.types.client_token
    import capo_partnercentral_channel.types.program
    import capo_partnercentral_channel.types.program_management_account_display_name
    import capo_partnercentral_channel.types.tag_list


class CreateProgramManagementAccountRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_channel.types.catalog.Catalog"
    """<p>The catalog identifier for the program management account.</p>"""
    program: "capo_partnercentral_channel.types.program.Program"
    """<p>The program type for the management account.</p>"""
    display_name: "capo_partnercentral_channel.types.program_management_account_display_name.ProgramManagementAccountDisplayName"
    """<p>A human-readable name for the program management account.</p>"""
    account_id: "capo_partnercentral_channel.types.account_id.AccountId"
    """<p>The AWS account ID to associate with the program management account.</p>"""
    client_token: NotRequired[
        "capo_partnercentral_channel.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>"""
    tags: NotRequired["capo_partnercentral_channel.types.tag_list.TagList"]
    """<p>Key-value pairs to associate with the program management account.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateProgramManagementAccountRequest) -> dict:
    out: dict = {}
    out["catalog"] = value["catalog"]
    import capo_partnercentral_channel.types.program

    out["program"] = capo_partnercentral_channel.types.program.serialize_aws_json_1_0(
        value["program"]
    )
    out["displayName"] = value["display_name"]
    out["accountId"] = value["account_id"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_partnercentral_channel.types.tag_list

        out["tags"] = capo_partnercentral_channel.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateProgramManagementAccountRequest:
    out: CreateProgramManagementAccountRequest = {}  # type: ignore[typeddict-item]
    if "catalog" in data:
        out["catalog"] = data["catalog"]
    else:
        raise DeserializationError(
            "CreateProgramManagementAccountRequest.catalog required"
        )
    if "program" in data:
        import capo_partnercentral_channel.types.program

        out["program"] = (
            capo_partnercentral_channel.types.program.deserialize_aws_json_1_0(
                data["program"]
            )
        )
    else:
        raise DeserializationError(
            "CreateProgramManagementAccountRequest.program required"
        )
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    else:
        raise DeserializationError(
            "CreateProgramManagementAccountRequest.display_name required"
        )
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    else:
        raise DeserializationError(
            "CreateProgramManagementAccountRequest.account_id required"
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "tags" in data:
        import capo_partnercentral_channel.types.tag_list

        out["tags"] = (
            capo_partnercentral_channel.types.tag_list.deserialize_aws_json_1_0(
                data["tags"]
            )
        )
    return out
