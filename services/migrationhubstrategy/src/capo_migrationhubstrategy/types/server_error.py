"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#ServerError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.server_error_category


class ServerError(TypedDict, closed=True):
    server_error_category: NotRequired[
        "capo_migrationhubstrategy.types.server_error_category.ServerErrorCategory"
    ]
    """<p>The error category of server analysis.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServerError) -> dict:
    out: dict = {}
    if "server_error_category" in value:
        out["serverErrorCategory"] = value["server_error_category"]
    return out


def deserialize_json(data: dict) -> ServerError:
    out: ServerError = {}  # type: ignore[typeddict-item]
    if "serverErrorCategory" in data:
        out["server_error_category"] = data["serverErrorCategory"]
    return out
