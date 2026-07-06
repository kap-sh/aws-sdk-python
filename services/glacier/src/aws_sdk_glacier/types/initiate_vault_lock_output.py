"""Generated from Smithy shape ``com.amazonaws.glacier#InitiateVaultLockOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glacier.types.string


class InitiateVaultLockOutput(TypedDict, closed=True):
    lock_id: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>The lock ID, which is used to complete the vault locking process.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InitiateVaultLockOutput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> InitiateVaultLockOutput:
    out: InitiateVaultLockOutput = {}  # type: ignore[typeddict-item]
    return out
