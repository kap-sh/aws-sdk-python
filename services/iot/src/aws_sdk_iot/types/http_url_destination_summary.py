"""Generated from Smithy shape ``com.amazonaws.iot#HttpUrlDestinationSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.url


class HttpUrlDestinationSummary(TypedDict):
    confirmation_url: NotRequired["aws_sdk_iot.types.url.Url"]
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
