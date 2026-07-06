"""Generated from Smithy shape ``com.amazonaws.datazone#Model``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.smithy


class _Model_smithy(TypedDict, closed=True):
    smithy: "aws_sdk_datazone.types.smithy.Smithy"


Model: TypeAlias = _Model_smithy


# --- restJson1 ser/de ---
def serialize_json(value: Model) -> dict:
    if "smithy" in value:
        return {"smithy": value["smithy"]}
    else:
        raise SerializationError("Model: no variant present")


def deserialize_json(data: dict) -> Model:
    if "smithy" in data:
        return {"smithy": data["smithy"]}
    else:
        raise DeserializationError("Model: no recognized variant key")
