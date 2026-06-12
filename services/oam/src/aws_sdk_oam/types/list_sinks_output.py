"""Generated from Smithy shape ``com.amazonaws.oam#ListSinksOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_oam.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_oam.types.list_sinks_items


class ListSinksOutput(TypedDict):
    items: "aws_sdk_oam.types.list_sinks_items.ListSinksItems"
    """<p>An array of structures that contain the information about the returned sinks.</p>"""
    next_token: NotRequired["str"]
    """<p>The token to use when requesting the next set of sinks.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSinksOutput) -> dict:
    out: dict = {}
    import aws_sdk_oam.types.list_sinks_items

    out["Items"] = aws_sdk_oam.types.list_sinks_items.serialize_json(value["items"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSinksOutput:
    out: ListSinksOutput = {}  # type: ignore[typeddict-item]
    if "Items" in data:
        import aws_sdk_oam.types.list_sinks_items

        out["items"] = aws_sdk_oam.types.list_sinks_items.deserialize_json(
            data["Items"]
        )
    else:
        raise DeserializationError("ListSinksOutput.items required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
