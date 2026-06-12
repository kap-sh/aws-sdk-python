"""Generated from Smithy shape ``com.amazonaws.amplifybackend#BackendAuthAppleProviderConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_amplifybackend.types.__string


class BackendAuthAppleProviderConfig(TypedDict):
    client_id: NotRequired["aws_sdk_amplifybackend.types.__string.__string"]
    """<p>Describes the client_id (also called Services ID) that comes from Apple.</p>"""
    key_id: NotRequired["aws_sdk_amplifybackend.types.__string.__string"]
    """<p>Describes the key_id that comes from Apple.</p>"""
    private_key: NotRequired["aws_sdk_amplifybackend.types.__string.__string"]
    """<p>Describes the private_key that comes from Apple.</p>"""
    team_id: NotRequired["aws_sdk_amplifybackend.types.__string.__string"]
    """<p>Describes the team_id that comes from Apple.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BackendAuthAppleProviderConfig) -> dict:
    out: dict = {}
    if "client_id" in value:
        out["client_id"] = value["client_id"]
    if "key_id" in value:
        out["key_id"] = value["key_id"]
    if "private_key" in value:
        out["private_key"] = value["private_key"]
    if "team_id" in value:
        out["team_id"] = value["team_id"]
    return out


def deserialize_json(data: dict) -> BackendAuthAppleProviderConfig:
    out: BackendAuthAppleProviderConfig = {}  # type: ignore[typeddict-item]
    if "client_id" in data:
        out["client_id"] = data["client_id"]
    if "key_id" in data:
        out["key_id"] = data["key_id"]
    if "private_key" in data:
        out["private_key"] = data["private_key"]
    if "team_id" in data:
        out["team_id"] = data["team_id"]
    return out
