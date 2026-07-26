"""Generated from Smithy shape ``com.amazonaws.mediaconnect#BatchGetRouterOutputError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mediaconnect.types.router_output_arn


class BatchGetRouterOutputError(TypedDict, closed=True):
    arn: "capo_mediaconnect.types.router_output_arn.RouterOutputArn"
    """<p>The Amazon Resource Name (ARN) of the router output for which the error occurred.</p>"""
    code: "str"
    """<p>The error code associated with the error.</p>"""
    message: "str"
    """<p>A message describing the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetRouterOutputError) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["code"] = value["code"]
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BatchGetRouterOutputError:
    out: BatchGetRouterOutputError = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("BatchGetRouterOutputError.arn required")
    if "code" in data:
        out["code"] = data["code"]
    else:
        raise DeserializationError("BatchGetRouterOutputError.code required")
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("BatchGetRouterOutputError.message required")
    return out
