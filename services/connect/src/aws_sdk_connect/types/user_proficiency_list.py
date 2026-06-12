"""Generated from Smithy shape ``com.amazonaws.connect#UserProficiencyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.user_proficiency

UserProficiencyList: TypeAlias = list[
    "aws_sdk_connect.types.user_proficiency.UserProficiency"
]


# --- restJson1 ser/de ---
def serialize_json(value: UserProficiencyList) -> list:
    import aws_sdk_connect.types.user_proficiency

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.user_proficiency.serialize_json(item))
    return out


def deserialize_json(data: list) -> UserProficiencyList:
    import aws_sdk_connect.types.user_proficiency

    out: UserProficiencyList = []
    for item in data:
        out.append(aws_sdk_connect.types.user_proficiency.deserialize_json(item))
    return out
