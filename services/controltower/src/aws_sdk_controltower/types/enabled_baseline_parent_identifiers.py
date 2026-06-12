"""Generated from Smithy shape ``com.amazonaws.controltower#EnabledBaselineParentIdentifiers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_controltower.types.arn

EnabledBaselineParentIdentifiers: TypeAlias = list["aws_sdk_controltower.types.arn.Arn"]


# --- restJson1 ser/de ---
def serialize_json(value: EnabledBaselineParentIdentifiers) -> list:
    return list(value)


def deserialize_json(data: list) -> EnabledBaselineParentIdentifiers:
    return list(data)
