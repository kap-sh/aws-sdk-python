"""Generated from Smithy shape ``com.amazonaws.macie2#UpdateFindingsFilterResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string


class UpdateFindingsFilterResponse(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the filter that was updated.</p>"""
    id: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The unique identifier for the filter that was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFindingsFilterResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "id" in value:
        out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> UpdateFindingsFilterResponse:
    out: UpdateFindingsFilterResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "id" in data:
        out["id"] = data["id"]
    return out
