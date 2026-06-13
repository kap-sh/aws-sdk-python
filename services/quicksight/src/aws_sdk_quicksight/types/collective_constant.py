"""Generated from Smithy shape ``com.amazonaws.quicksight#CollectiveConstant``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.string_list


class CollectiveConstant(TypedDict):
    value_list: NotRequired["aws_sdk_quicksight.types.string_list.StringList"]
    """<p>A list of values for the collective constant.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CollectiveConstant) -> dict:
    out: dict = {}
    if "value_list" in value:
        import aws_sdk_quicksight.types.string_list

        out["ValueList"] = aws_sdk_quicksight.types.string_list.serialize_json(
            value["value_list"]
        )
    return out


def deserialize_json(data: dict) -> CollectiveConstant:
    out: CollectiveConstant = {}  # type: ignore[typeddict-item]
    if "ValueList" in data:
        import aws_sdk_quicksight.types.string_list

        out["value_list"] = aws_sdk_quicksight.types.string_list.deserialize_json(
            data["ValueList"]
        )
    return out
