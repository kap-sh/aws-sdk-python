"""Generated from Smithy shape ``com.amazonaws.connectcases#LayoutContent``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connectcases.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_connectcases.types.basic_layout


class _LayoutContent_basic(TypedDict, closed=True):
    basic: "capo_connectcases.types.basic_layout.BasicLayout"


LayoutContent: TypeAlias = _LayoutContent_basic


# --- restJson1 ser/de ---
def serialize_json(value: LayoutContent) -> dict:
    if "basic" in value:
        import capo_connectcases.types.basic_layout

        return {
            "basic": capo_connectcases.types.basic_layout.serialize_json(value["basic"])
        }
    else:
        raise SerializationError("LayoutContent: no variant present")


def deserialize_json(data: dict) -> LayoutContent:
    if "basic" in data:
        import capo_connectcases.types.basic_layout

        return {
            "basic": capo_connectcases.types.basic_layout.deserialize_json(
                data["basic"]
            )
        }
    else:
        raise DeserializationError("LayoutContent: no recognized variant key")
