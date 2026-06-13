"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#UserDefined``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sagemaker_geospatial.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sagemaker_geospatial.types.unit


class UserDefined(TypedDict):
    value: "float"
    """<p>The value for output resolution of the result.</p>"""
    unit: "aws_sdk_sagemaker_geospatial.types.unit.Unit"
    """<p>The units for output resolution of the result.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserDefined) -> dict:
    out: dict = {}
    out["Value"] = value["value"]
    out["Unit"] = value["unit"]
    return out


def deserialize_json(data: dict) -> UserDefined:
    out: UserDefined = {}  # type: ignore[typeddict-item]
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("UserDefined.value required")
    if "Unit" in data:
        out["unit"] = data["Unit"]
    else:
        raise DeserializationError("UserDefined.unit required")
    return out
