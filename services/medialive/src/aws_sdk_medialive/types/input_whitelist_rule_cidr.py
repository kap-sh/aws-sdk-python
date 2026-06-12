"""Generated from Smithy shape ``com.amazonaws.medialive#InputWhitelistRuleCidr``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class InputWhitelistRuleCidr(TypedDict):
    cidr: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The IPv4 CIDR to whitelist."""


# --- restJson1 ser/de ---
def serialize_json(value: InputWhitelistRuleCidr) -> dict:
    out: dict = {}
    if "cidr" in value:
        out["cidr"] = value["cidr"]
    return out


def deserialize_json(data: dict) -> InputWhitelistRuleCidr:
    out: InputWhitelistRuleCidr = {}  # type: ignore[typeddict-item]
    if "cidr" in data:
        out["cidr"] = data["cidr"]
    return out
