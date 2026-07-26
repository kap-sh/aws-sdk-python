"""Generated from Smithy shape ``com.amazonaws.mediatailor#AdDecisionServerConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediatailor.types.http_request


class AdDecisionServerConfiguration(TypedDict, closed=True):
    http_request: NotRequired["capo_mediatailor.types.http_request.HttpRequest"]
    """<p>The HTTP request configuration parameters for the ad decision server.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AdDecisionServerConfiguration) -> dict:
    out: dict = {}
    if "http_request" in value:
        import capo_mediatailor.types.http_request

        out["HttpRequest"] = capo_mediatailor.types.http_request.serialize_json(
            value["http_request"]
        )
    return out


def deserialize_json(data: dict) -> AdDecisionServerConfiguration:
    out: AdDecisionServerConfiguration = {}  # type: ignore[typeddict-item]
    if "HttpRequest" in data:
        import capo_mediatailor.types.http_request

        out["http_request"] = capo_mediatailor.types.http_request.deserialize_json(
            data["HttpRequest"]
        )
    return out
