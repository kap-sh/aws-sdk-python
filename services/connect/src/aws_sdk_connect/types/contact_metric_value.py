"""Generated from Smithy shape ``com.amazonaws.connect#ContactMetricValue``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_connect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.double


class _ContactMetricValue_Number(TypedDict, closed=True):
    Number: "aws_sdk_connect.types.double.Double"


ContactMetricValue: TypeAlias = _ContactMetricValue_Number


# --- restJson1 ser/de ---
def serialize_json(value: ContactMetricValue) -> dict:
    if "Number" in value:
        return {"Number": value["Number"]}
    else:
        raise SerializationError("ContactMetricValue: no variant present")


def deserialize_json(data: dict) -> ContactMetricValue:
    if "Number" in data:
        return {"Number": data["Number"]}
    else:
        raise DeserializationError("ContactMetricValue: no recognized variant key")
