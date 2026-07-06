"""Generated from Smithy shape ``com.amazonaws.quicksight#NamedEntityRef``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.limited_string


class NamedEntityRef(TypedDict, closed=True):
    named_entity_name: NotRequired[
        "aws_sdk_quicksight.types.limited_string.LimitedString"
    ]
    """<p>The <code>NamedEntityName</code> for the <code>NamedEntityRef</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NamedEntityRef) -> dict:
    out: dict = {}
    if "named_entity_name" in value:
        out["NamedEntityName"] = value["named_entity_name"]
    return out


def deserialize_json(data: dict) -> NamedEntityRef:
    out: NamedEntityRef = {}  # type: ignore[typeddict-item]
    if "NamedEntityName" in data:
        out["named_entity_name"] = data["NamedEntityName"]
    return out
