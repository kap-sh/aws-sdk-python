"""Generated from Smithy shape ``com.amazonaws.amplify#Branches``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_amplify.types.branch

Branches: TypeAlias = list["aws_sdk_amplify.types.branch.Branch"]


# --- restJson1 ser/de ---
def serialize_json(value: Branches) -> list:
    import aws_sdk_amplify.types.branch

    out: list = []
    for item in value:
        out.append(aws_sdk_amplify.types.branch.serialize_json(item))
    return out


def deserialize_json(data: list) -> Branches:
    import aws_sdk_amplify.types.branch

    out: Branches = []
    for item in data:
        out.append(aws_sdk_amplify.types.branch.deserialize_json(item))
    return out
