"""Generated from Smithy shape ``com.amazonaws.macie2#AwsService``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string


class AwsService(TypedDict):
    invoked_by: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The name of the Amazon Web Service that performed the action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsService) -> dict:
    out: dict = {}
    if "invoked_by" in value:
        out["invokedBy"] = value["invoked_by"]
    return out


def deserialize_json(data: dict) -> AwsService:
    out: AwsService = {}  # type: ignore[typeddict-item]
    if "invokedBy" in data:
        out["invoked_by"] = data["invokedBy"]
    return out
