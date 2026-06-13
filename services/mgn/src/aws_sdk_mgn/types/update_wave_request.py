"""Generated from Smithy shape ``com.amazonaws.mgn#UpdateWaveRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mgn.types.account_id
    import aws_sdk_mgn.types.wave_description
    import aws_sdk_mgn.types.wave_id
    import aws_sdk_mgn.types.wave_name


class UpdateWaveRequest(TypedDict):
    wave_id: "aws_sdk_mgn.types.wave_id.WaveID"
    """<p>Wave ID.</p>"""
    name: NotRequired["aws_sdk_mgn.types.wave_name.WaveName"]
    """<p>Wave name.</p>"""
    description: NotRequired["aws_sdk_mgn.types.wave_description.WaveDescription"]
    """<p>Wave description.</p>"""
    account_id: NotRequired["aws_sdk_mgn.types.account_id.AccountID"]
    """<p>Account ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWaveRequest) -> dict:
    out: dict = {}
    out["waveID"] = value["wave_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "account_id" in value:
        out["accountID"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> UpdateWaveRequest:
    out: UpdateWaveRequest = {}  # type: ignore[typeddict-item]
    if "waveID" in data:
        out["wave_id"] = data["waveID"]
    else:
        raise DeserializationError("UpdateWaveRequest.wave_id required")
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "accountID" in data:
        out["account_id"] = data["accountID"]
    return out
