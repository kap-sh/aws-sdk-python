"""Generated from Smithy shape ``com.amazonaws.iot#HttpUrlDestinationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.url


class HttpUrlDestinationSummary(TypedDict, closed=True):
    confirmation_url: NotRequired["capo_iot.types.url.Url"]
    """<p>The URL used to confirm ownership of or access to the HTTP topic rule destination URL.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HttpUrlDestinationSummary) -> dict:
    out: dict = {}
    if "confirmation_url" in value:
        out["confirmationUrl"] = value["confirmation_url"]
    return out


def deserialize_json(data: dict) -> HttpUrlDestinationSummary:
    out: HttpUrlDestinationSummary = {}  # type: ignore[typeddict-item]
    if "confirmationUrl" in data:
        out["confirmation_url"] = data["confirmationUrl"]
    return out
