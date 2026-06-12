"""Generated from Smithy shape ``com.amazonaws.glacier#VaultLockPolicy``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glacier.types.string


class VaultLockPolicy(TypedDict):
    policy: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>The vault lock policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VaultLockPolicy) -> dict:
    out: dict = {}
    if "policy" in value:
        out["Policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> VaultLockPolicy:
    out: VaultLockPolicy = {}  # type: ignore[typeddict-item]
    if "Policy" in data:
        out["policy"] = data["Policy"]
    return out
