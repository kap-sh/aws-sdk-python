"""Generated from Smithy shape ``com.amazonaws.networkmanager#UpdateConnectionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.connection


class UpdateConnectionResponse(TypedDict, closed=True):
    connection: NotRequired["aws_sdk_networkmanager.types.connection.Connection"]
    """<p>Information about the connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConnectionResponse) -> dict:
    out: dict = {}
    if "connection" in value:
        import aws_sdk_networkmanager.types.connection

        out["Connection"] = aws_sdk_networkmanager.types.connection.serialize_json(
            value["connection"]
        )
    return out


def deserialize_json(data: dict) -> UpdateConnectionResponse:
    out: UpdateConnectionResponse = {}  # type: ignore[typeddict-item]
    if "Connection" in data:
        import aws_sdk_networkmanager.types.connection

        out["connection"] = aws_sdk_networkmanager.types.connection.deserialize_json(
            data["Connection"]
        )
    return out
