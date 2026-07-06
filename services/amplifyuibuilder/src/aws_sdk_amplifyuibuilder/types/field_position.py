"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#FieldPosition``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_amplifyuibuilder.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.fixed_position


class _FieldPosition_fixed(TypedDict, closed=True):
    fixed: "aws_sdk_amplifyuibuilder.types.fixed_position.FixedPosition"


class _FieldPosition_rightOf(TypedDict, closed=True):
    rightOf: "str"


class _FieldPosition_below(TypedDict, closed=True):
    below: "str"


FieldPosition: TypeAlias = (
    _FieldPosition_fixed | _FieldPosition_rightOf | _FieldPosition_below
)


# --- restJson1 ser/de ---
def serialize_json(value: FieldPosition) -> dict:
    if "fixed" in value:
        import aws_sdk_amplifyuibuilder.types.fixed_position

        return {
            "fixed": aws_sdk_amplifyuibuilder.types.fixed_position.serialize_json(
                value["fixed"]
            )
        }
    elif "rightOf" in value:
        return {"rightOf": value["rightOf"]}
    elif "below" in value:
        return {"below": value["below"]}
    else:
        raise SerializationError("FieldPosition: no variant present")


def deserialize_json(data: dict) -> FieldPosition:
    if "fixed" in data:
        import aws_sdk_amplifyuibuilder.types.fixed_position

        return {
            "fixed": aws_sdk_amplifyuibuilder.types.fixed_position.deserialize_json(
                data["fixed"]
            )
        }
    elif "rightOf" in data:
        return {"rightOf": data["rightOf"]}
    elif "below" in data:
        return {"below": data["below"]}
    else:
        raise DeserializationError("FieldPosition: no recognized variant key")
