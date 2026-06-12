"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#CreateProgramManagementAccountRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_partnercentral_channel.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_channel.types.account_id
    import aws_sdk_partnercentral_channel.types.catalog
    import aws_sdk_partnercentral_channel.types.client_token
    import aws_sdk_partnercentral_channel.types.program
    import aws_sdk_partnercentral_channel.types.program_management_account_display_name
    import aws_sdk_partnercentral_channel.types.tag_list


class CreateProgramManagementAccountRequest(TypedDict):
    catalog: "aws_sdk_partnercentral_channel.types.catalog.Catalog"
    """<p>The catalog identifier for the program management account.</p>"""
    program: "aws_sdk_partnercentral_channel.types.program.Program"
    """<p>The program type for the management account.</p>"""
    display_name: "aws_sdk_partnercentral_channel.types.program_management_account_display_name.ProgramManagementAccountDisplayName"
    """<p>A human-readable name for the program management account.</p>"""
    account_id: "aws_sdk_partnercentral_channel.types.account_id.AccountId"
    """<p>The AWS account ID to associate with the program management account.</p>"""
    client_token: NotRequired[
        "aws_sdk_partnercentral_channel.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>"""
    tags: NotRequired["aws_sdk_partnercentral_channel.types.tag_list.TagList"]
    """<p>Key-value pairs to associate with the program management account.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateProgramManagementAccountRequest) -> dict:
    out: dict = {}
    out["catalog"] = value["catalog"]
    import aws_sdk_partnercentral_channel.types.program

    out["program"] = (
        aws_sdk_partnercentral_channel.types.program.serialize_aws_json_1_0(
            value["program"]
        )
    )
    out["displayName"] = value["display_name"]
    out["accountId"] = value["account_id"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import aws_sdk_partnercentral_channel.types.tag_list

        out["tags"] = (
            aws_sdk_partnercentral_channel.types.tag_list.serialize_aws_json_1_0(
                value["tags"]
            )
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
        import aws_sdk_partnercentral_channel.types.program

        out["program"] = (
            aws_sdk_partnercentral_channel.types.program.deserialize_aws_json_1_0(
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
        import aws_sdk_partnercentral_channel.types.tag_list

        out["tags"] = (
            aws_sdk_partnercentral_channel.types.tag_list.deserialize_aws_json_1_0(
                data["tags"]
            )
        )
    return out
