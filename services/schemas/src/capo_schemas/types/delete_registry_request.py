"""Generated from Smithy shape ``com.amazonaws.schemas#DeleteRegistryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_schemas.types.__string


class DeleteRegistryRequest(TypedDict, closed=True):
    registry_name: "capo_schemas.types.__string.__string"
    """<p>The name of the registry.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRegistryRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteRegistryRequest:
    out: DeleteRegistryRequest = {}  # type: ignore[typeddict-item]
    return out
