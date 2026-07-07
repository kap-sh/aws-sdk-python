"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#SortProperty``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_amplifyuibuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.sort_direction


class SortProperty(TypedDict, closed=True):
    field: "str"
    """<p>The field to perform the sort on.</p>"""
    direction: "aws_sdk_amplifyuibuilder.types.sort_direction.SortDirection"
    """<p>The direction of the sort, either ascending or descending.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SortProperty) -> dict:
    out: dict = {}
    out["field"] = value["field"]
    import aws_sdk_amplifyuibuilder.types.sort_direction

    out["direction"] = aws_sdk_amplifyuibuilder.types.sort_direction.serialize_json(
        value["direction"]
    )
    return out


def deserialize_json(data: dict) -> SortProperty:
    out: SortProperty = {}  # type: ignore[typeddict-item]
    if "field" in data:
        out["field"] = data["field"]
    else:
        raise DeserializationError("SortProperty.field required")
    if "direction" in data:
        import aws_sdk_amplifyuibuilder.types.sort_direction

        out["direction"] = (
            aws_sdk_amplifyuibuilder.types.sort_direction.deserialize_json(
                data["direction"]
            )
        )
    else:
        raise DeserializationError("SortProperty.direction required")
    return out
