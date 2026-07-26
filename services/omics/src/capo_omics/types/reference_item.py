"""Generated from Smithy shape ``com.amazonaws.omics#ReferenceItem``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_omics.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_omics.types.reference_arn


class _ReferenceItem_referenceArn(TypedDict, closed=True):
    referenceArn: "capo_omics.types.reference_arn.ReferenceArn"


ReferenceItem: TypeAlias = _ReferenceItem_referenceArn


# --- restJson1 ser/de ---
def serialize_json(value: ReferenceItem) -> dict:
    if "referenceArn" in value:
        return {"referenceArn": value["referenceArn"]}
    else:
        raise SerializationError("ReferenceItem: no variant present")


def deserialize_json(data: dict) -> ReferenceItem:
    if "referenceArn" in data:
        return {"referenceArn": data["referenceArn"]}
    else:
        raise DeserializationError("ReferenceItem: no recognized variant key")
