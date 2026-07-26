"""Generated from Smithy shape ``com.amazonaws.quicksight#SpaceQuickSightResourceDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_quicksight.types.arn


class _SpaceQuickSightResourceDetails_resourceArn(TypedDict, closed=True):
    resourceArn: "capo_quicksight.types.arn.Arn"


SpaceQuickSightResourceDetails: TypeAlias = _SpaceQuickSightResourceDetails_resourceArn


# --- restJson1 ser/de ---
def serialize_json(value: SpaceQuickSightResourceDetails) -> dict:
    if "resourceArn" in value:
        return {"resourceArn": value["resourceArn"]}
    else:
        raise SerializationError("SpaceQuickSightResourceDetails: no variant present")


def deserialize_json(data: dict) -> SpaceQuickSightResourceDetails:
    if "resourceArn" in data:
        return {"resourceArn": data["resourceArn"]}
    else:
        raise DeserializationError(
            "SpaceQuickSightResourceDetails: no recognized variant key"
        )
