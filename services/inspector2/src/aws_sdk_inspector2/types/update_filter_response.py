"""Generated from Smithy shape ``com.amazonaws.inspector2#UpdateFilterResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.filter_arn


class UpdateFilterResponse(TypedDict, closed=True):
    arn: "aws_sdk_inspector2.types.filter_arn.FilterArn"
    """<p>The Amazon Resource Number (ARN) of the successfully updated filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFilterResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> UpdateFilterResponse:
    out: UpdateFilterResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("UpdateFilterResponse.arn required")
    return out
