"""Generated from Smithy shape ``com.amazonaws.mgn#AssociateApplicationsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_mgn.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_mgn.types.account_id
    import aws_sdk_mgn.types.application_i_ds
    import aws_sdk_mgn.types.wave_id

class AssociateApplicationsRequest(TypedDict):
    wave_id: "aws_sdk_mgn.types.wave_id.WaveID"
    """<p>Wave ID.</p>"""
    application_i_ds: "aws_sdk_mgn.types.application_i_ds.ApplicationIDs"
    """<p>Application IDs list.</p>"""
    account_id: NotRequired["aws_sdk_mgn.types.account_id.AccountID"]
    """<p>Account ID.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: AssociateApplicationsRequest) -> dict:
    out: dict = {}
    out["waveID"] = value["wave_id"]
    import aws_sdk_mgn.types.application_i_ds
    out["applicationIDs"] = aws_sdk_mgn.types.application_i_ds.serialize_json(value["application_i_ds"])
    if "account_id" in value:
        out["accountID"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> AssociateApplicationsRequest:
    out: AssociateApplicationsRequest = {}  # type: ignore[typeddict-item]
    if "waveID" in data:
        out["wave_id"] = data["waveID"]
    else:
        raise DeserializationError("AssociateApplicationsRequest.wave_id required")
    if "applicationIDs" in data:
        import aws_sdk_mgn.types.application_i_ds
        out["application_i_ds"] = aws_sdk_mgn.types.application_i_ds.deserialize_json(data["applicationIDs"])
    else:
        raise DeserializationError("AssociateApplicationsRequest.application_i_ds required")
    if "accountID" in data:
        out["account_id"] = data["accountID"]
    return out