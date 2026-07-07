"""Generated from Smithy shape ``com.amazonaws.appintegrations#CreateApplicationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appintegrations.types.arn
    import aws_sdk_appintegrations.types.uuid


class CreateApplicationResponse(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_appintegrations.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the Application.</p>"""
    id: NotRequired["aws_sdk_appintegrations.types.uuid.UUID"]
    """<p>A unique identifier for the Application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateApplicationResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "id" in value:
        out["Id"] = value["id"]
    return out


def deserialize_json(data: dict) -> CreateApplicationResponse:
    out: CreateApplicationResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Id" in data:
        out["id"] = data["Id"]
    return out
