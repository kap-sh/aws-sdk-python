"""Generated from Smithy shape ``com.amazonaws.glacier#CreateVaultOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glacier.types.string


class CreateVaultOutput(TypedDict, closed=True):
    location: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>The URI of the vault that was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateVaultOutput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CreateVaultOutput:
    out: CreateVaultOutput = {}  # type: ignore[typeddict-item]
    return out
