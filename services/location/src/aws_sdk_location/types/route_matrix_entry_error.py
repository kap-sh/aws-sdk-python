"""Generated from Smithy shape ``com.amazonaws.location#RouteMatrixEntryError``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_location.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_location.types.route_matrix_error_code


class RouteMatrixEntryError(TypedDict):
    code: "aws_sdk_location.types.route_matrix_error_code.RouteMatrixErrorCode"
    """<p>The type of error which occurred for the route calculation.</p>"""
    message: NotRequired["str"]
    """<p>A message about the error that occurred for the route calculation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteMatrixEntryError) -> dict:
    out: dict = {}
    out["Code"] = value["code"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> RouteMatrixEntryError:
    out: RouteMatrixEntryError = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        out["code"] = data["Code"]
    else:
        raise DeserializationError("RouteMatrixEntryError.code required")
    if "Message" in data:
        out["message"] = data["Message"]
    return out
