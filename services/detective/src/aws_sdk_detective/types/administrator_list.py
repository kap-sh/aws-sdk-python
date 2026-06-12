"""Generated from Smithy shape ``com.amazonaws.detective#AdministratorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_detective.types.administrator

AdministratorList: TypeAlias = list[
    "aws_sdk_detective.types.administrator.Administrator"
]


# --- restJson1 ser/de ---
def serialize_json(value: AdministratorList) -> list:
    import aws_sdk_detective.types.administrator

    out: list = []
    for item in value:
        out.append(aws_sdk_detective.types.administrator.serialize_json(item))
    return out


def deserialize_json(data: list) -> AdministratorList:
    import aws_sdk_detective.types.administrator

    out: AdministratorList = []
    for item in data:
        out.append(aws_sdk_detective.types.administrator.deserialize_json(item))
    return out
