"""Generated from Smithy shape ``com.amazonaws.networkmanager#DeleteConnectionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.connection


class DeleteConnectionResponse(TypedDict, closed=True):
    connection: NotRequired["capo_networkmanager.types.connection.Connection"]
    """<p>Information about the connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteConnectionResponse) -> dict:
    out: dict = {}
    if "connection" in value:
        import capo_networkmanager.types.connection

        out["Connection"] = capo_networkmanager.types.connection.serialize_json(
            value["connection"]
        )
    return out


def deserialize_json(data: dict) -> DeleteConnectionResponse:
    out: DeleteConnectionResponse = {}  # type: ignore[typeddict-item]
    if "Connection" in data:
        import capo_networkmanager.types.connection

        out["connection"] = capo_networkmanager.types.connection.deserialize_json(
            data["Connection"]
        )
    return out
