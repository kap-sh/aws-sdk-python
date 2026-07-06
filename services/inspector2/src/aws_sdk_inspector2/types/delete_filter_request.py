"""Generated from Smithy shape ``com.amazonaws.inspector2#DeleteFilterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.filter_arn


class DeleteFilterRequest(TypedDict, closed=True):
    arn: "aws_sdk_inspector2.types.filter_arn.FilterArn"
    """<p>The Amazon Resource Number (ARN) of the filter to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteFilterRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> DeleteFilterRequest:
    out: DeleteFilterRequest = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("DeleteFilterRequest.arn required")
    return out
