"""Generated from Smithy shape ``com.amazonaws.mgn#UnarchiveWaveRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mgn.types.account_id
    import aws_sdk_mgn.types.wave_id


class UnarchiveWaveRequest(TypedDict, closed=True):
    wave_id: "aws_sdk_mgn.types.wave_id.WaveID"
    """<p>Wave ID.</p>"""
    account_id: NotRequired["aws_sdk_mgn.types.account_id.AccountID"]
    """<p>Account ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UnarchiveWaveRequest) -> dict:
    out: dict = {}
    out["waveID"] = value["wave_id"]
    if "account_id" in value:
        out["accountID"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> UnarchiveWaveRequest:
    out: UnarchiveWaveRequest = {}  # type: ignore[typeddict-item]
    if "waveID" in data:
        out["wave_id"] = data["waveID"]
    else:
        raise DeserializationError("UnarchiveWaveRequest.wave_id required")
    if "accountID" in data:
        out["account_id"] = data["accountID"]
    return out
