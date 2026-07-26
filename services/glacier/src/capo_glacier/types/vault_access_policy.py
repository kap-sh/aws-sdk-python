"""Generated from Smithy shape ``com.amazonaws.glacier#VaultAccessPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glacier.types.string


class VaultAccessPolicy(TypedDict, closed=True):
    policy: NotRequired["capo_glacier.types.string.string"]
    """<p>The vault access policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VaultAccessPolicy) -> dict:
    out: dict = {}
    if "policy" in value:
        out["Policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> VaultAccessPolicy:
    out: VaultAccessPolicy = {}  # type: ignore[typeddict-item]
    if "Policy" in data:
        out["policy"] = data["Policy"]
    return out
