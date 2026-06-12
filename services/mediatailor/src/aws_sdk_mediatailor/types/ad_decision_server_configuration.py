"""Generated from Smithy shape ``com.amazonaws.mediatailor#AdDecisionServerConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.http_request


class AdDecisionServerConfiguration(TypedDict):
    http_request: NotRequired["aws_sdk_mediatailor.types.http_request.HttpRequest"]
    """<p>The HTTP request configuration parameters for the ad decision server.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AdDecisionServerConfiguration) -> dict:
    out: dict = {}
    if "http_request" in value:
        import aws_sdk_mediatailor.types.http_request

        out["HttpRequest"] = aws_sdk_mediatailor.types.http_request.serialize_json(
            value["http_request"]
        )
    return out


def deserialize_json(data: dict) -> AdDecisionServerConfiguration:
    out: AdDecisionServerConfiguration = {}  # type: ignore[typeddict-item]
    if "HttpRequest" in data:
        import aws_sdk_mediatailor.types.http_request

        out["http_request"] = aws_sdk_mediatailor.types.http_request.deserialize_json(
            data["HttpRequest"]
        )
    return out
