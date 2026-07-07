"""Generated from Smithy shape ``com.amazonaws.quicksight#JoinKeyProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.boolean


class JoinKeyProperties(TypedDict, closed=True):
    unique_key: NotRequired["aws_sdk_quicksight.types.boolean.Boolean"]
    """<p>A value that indicates that a row in a table is uniquely identified by the columns in a join key. This is used by Quick Sight to optimize query performance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JoinKeyProperties) -> dict:
    out: dict = {}
    if "unique_key" in value:
        out["UniqueKey"] = value["unique_key"]
    return out


def deserialize_json(data: dict) -> JoinKeyProperties:
    out: JoinKeyProperties = {}  # type: ignore[typeddict-item]
    if "UniqueKey" in data:
        out["unique_key"] = data["UniqueKey"]
    return out
