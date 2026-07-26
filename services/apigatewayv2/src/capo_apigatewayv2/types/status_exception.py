"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#StatusException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_apigatewayv2.types.__string_min1_max256
    import capo_apigatewayv2.types.__string_min1_max2048


class StatusException(TypedDict, closed=True):
    exception: NotRequired[
        "capo_apigatewayv2.types.__string_min1_max256.__stringMin1Max256"
    ]
    """<p>The exception.</p>"""
    message: NotRequired[
        "capo_apigatewayv2.types.__string_min1_max2048.__stringMin1Max2048"
    ]
    """<p>The error message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StatusException) -> dict:
    out: dict = {}
    if "exception" in value:
        out["exception"] = value["exception"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> StatusException:
    out: StatusException = {}  # type: ignore[typeddict-item]
    if "exception" in data:
        out["exception"] = data["exception"]
    if "message" in data:
        out["message"] = data["message"]
    return out
