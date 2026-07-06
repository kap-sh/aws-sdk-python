"""Generated from Smithy shape ``com.amazonaws.medialive#InputWhitelistRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class InputWhitelistRule(TypedDict, closed=True):
    cidr: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The IPv4 CIDR that's whitelisted."""


# --- restJson1 ser/de ---
def serialize_json(value: InputWhitelistRule) -> dict:
    out: dict = {}
    if "cidr" in value:
        out["cidr"] = value["cidr"]
    return out


def deserialize_json(data: dict) -> InputWhitelistRule:
    out: InputWhitelistRule = {}  # type: ignore[typeddict-item]
    if "cidr" in data:
        out["cidr"] = data["cidr"]
    return out
