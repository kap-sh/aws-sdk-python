"""Generated from Smithy shape ``com.amazonaws.mgn#DisassociateSourceServersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mgn.types.account_id
    import capo_mgn.types.application_id
    import capo_mgn.types.disassociate_source_servers_request_source_server_i_ds


class DisassociateSourceServersRequest(TypedDict, closed=True):
    application_id: "capo_mgn.types.application_id.ApplicationID"
    """<p>Application ID.</p>"""
    source_server_i_ds: "capo_mgn.types.disassociate_source_servers_request_source_server_i_ds.DisassociateSourceServersRequestSourceServerIDs"
    """<p>Source server IDs list.</p>"""
    account_id: NotRequired["capo_mgn.types.account_id.AccountID"]
    """<p>Account ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateSourceServersRequest) -> dict:
    out: dict = {}
    out["applicationID"] = value["application_id"]
    import capo_mgn.types.disassociate_source_servers_request_source_server_i_ds

    out["sourceServerIDs"] = (
        capo_mgn.types.disassociate_source_servers_request_source_server_i_ds.serialize_json(
            value["source_server_i_ds"]
        )
    )
    if "account_id" in value:
        out["accountID"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> DisassociateSourceServersRequest:
    out: DisassociateSourceServersRequest = {}  # type: ignore[typeddict-item]
    if "applicationID" in data:
        out["application_id"] = data["applicationID"]
    else:
        raise DeserializationError(
            "DisassociateSourceServersRequest.application_id required"
        )
    if "sourceServerIDs" in data:
        import capo_mgn.types.disassociate_source_servers_request_source_server_i_ds

        out["source_server_i_ds"] = (
            capo_mgn.types.disassociate_source_servers_request_source_server_i_ds.deserialize_json(
                data["sourceServerIDs"]
            )
        )
    else:
        raise DeserializationError(
            "DisassociateSourceServersRequest.source_server_i_ds required"
        )
    if "accountID" in data:
        out["account_id"] = data["accountID"]
    return out
