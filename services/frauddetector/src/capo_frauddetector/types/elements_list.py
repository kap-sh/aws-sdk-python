"""Generated from Smithy shape ``com.amazonaws.frauddetector#ElementsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_frauddetector.types.elements

ElementsList: TypeAlias = list["capo_frauddetector.types.elements.Elements"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ElementsList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ElementsList:
    return list(data)
