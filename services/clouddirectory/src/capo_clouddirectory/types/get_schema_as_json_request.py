"""Generated from Smithy shape ``com.amazonaws.clouddirectory#GetSchemaAsJsonRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.arn


class GetSchemaAsJsonRequest(TypedDict, closed=True):
    schema_arn: "capo_clouddirectory.types.arn.Arn"
    """<p>The ARN of the schema to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSchemaAsJsonRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSchemaAsJsonRequest:
    out: GetSchemaAsJsonRequest = {}  # type: ignore[typeddict-item]
    return out
