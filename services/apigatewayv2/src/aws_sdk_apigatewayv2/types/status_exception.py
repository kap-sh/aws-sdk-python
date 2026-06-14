"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#StatusException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__string_min1_max256
    import aws_sdk_apigatewayv2.types.__string_min1_max2048


class StatusException(TypedDict):
    exception: NotRequired[
        "aws_sdk_apigatewayv2.types.__string_min1_max256.__stringMin1Max256"
    ]
    """<p>The exception.</p>"""
    message: NotRequired[
        "aws_sdk_apigatewayv2.types.__string_min1_max2048.__stringMin1Max2048"
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
