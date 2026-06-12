"""Generated from Smithy shape ``com.amazonaws.macie2#CreateMemberResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string


class CreateMemberResponse(TypedDict):
    arn: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the account that was associated with the administrator account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMemberResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> CreateMemberResponse:
    out: CreateMemberResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    return out
