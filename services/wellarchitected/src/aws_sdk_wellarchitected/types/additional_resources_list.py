"""Generated from Smithy shape ``com.amazonaws.wellarchitected#AdditionalResourcesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.additional_resources

AdditionalResourcesList: TypeAlias = list[
    "aws_sdk_wellarchitected.types.additional_resources.AdditionalResources"
]


# --- restJson1 ser/de ---
def serialize_json(value: AdditionalResourcesList) -> list:
    import aws_sdk_wellarchitected.types.additional_resources

    out: list = []
    for item in value:
        out.append(
            aws_sdk_wellarchitected.types.additional_resources.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AdditionalResourcesList:
    import aws_sdk_wellarchitected.types.additional_resources

    out: AdditionalResourcesList = []
    for item in data:
        out.append(
            aws_sdk_wellarchitected.types.additional_resources.deserialize_json(item)
        )
    return out
