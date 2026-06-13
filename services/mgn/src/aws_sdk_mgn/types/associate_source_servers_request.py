"""Generated from Smithy shape ``com.amazonaws.mgn#AssociateSourceServersRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mgn.types.account_id
    import aws_sdk_mgn.types.application_id
    import aws_sdk_mgn.types.associate_source_servers_request_source_server_i_ds


class AssociateSourceServersRequest(TypedDict):
    application_id: "aws_sdk_mgn.types.application_id.ApplicationID"
    """<p>Application ID.</p>"""
    source_server_i_ds: "aws_sdk_mgn.types.associate_source_servers_request_source_server_i_ds.AssociateSourceServersRequestSourceServerIDs"
    """<p>Source server IDs list.</p>"""
    account_id: NotRequired["aws_sdk_mgn.types.account_id.AccountID"]
    """<p>Account ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateSourceServersRequest) -> dict:
    out: dict = {}
    out["applicationID"] = value["application_id"]
    import aws_sdk_mgn.types.associate_source_servers_request_source_server_i_ds

    out["sourceServerIDs"] = (
        aws_sdk_mgn.types.associate_source_servers_request_source_server_i_ds.serialize_json(
            value["source_server_i_ds"]
        )
    )
    if "account_id" in value:
        out["accountID"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> AssociateSourceServersRequest:
    out: AssociateSourceServersRequest = {}  # type: ignore[typeddict-item]
    if "applicationID" in data:
        out["application_id"] = data["applicationID"]
    else:
        raise DeserializationError(
            "AssociateSourceServersRequest.application_id required"
        )
    if "sourceServerIDs" in data:
        import aws_sdk_mgn.types.associate_source_servers_request_source_server_i_ds

        out["source_server_i_ds"] = (
            aws_sdk_mgn.types.associate_source_servers_request_source_server_i_ds.deserialize_json(
                data["sourceServerIDs"]
            )
        )
    else:
        raise DeserializationError(
            "AssociateSourceServersRequest.source_server_i_ds required"
        )
    if "accountID" in data:
        out["account_id"] = data["accountID"]
    return out
