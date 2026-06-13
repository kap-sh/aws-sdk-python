"""Generated from Smithy shape ``com.amazonaws.inspector2#DeleteFilterResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.filter_arn


class DeleteFilterResponse(TypedDict):
    arn: "aws_sdk_inspector2.types.filter_arn.FilterArn"
    """<p>The Amazon Resource Number (ARN) of the filter that has been deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteFilterResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> DeleteFilterResponse:
    out: DeleteFilterResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("DeleteFilterResponse.arn required")
    return out
