"""Generated from Smithy shape ``com.amazonaws.chime#SigninDelegateGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chime.types.signin_delegate_group

SigninDelegateGroupList: TypeAlias = list[
    "aws_sdk_chime.types.signin_delegate_group.SigninDelegateGroup"
]


# --- restJson1 ser/de ---
def serialize_json(value: SigninDelegateGroupList) -> list:
    import aws_sdk_chime.types.signin_delegate_group

    out: list = []
    for item in value:
        out.append(aws_sdk_chime.types.signin_delegate_group.serialize_json(item))
    return out


def deserialize_json(data: list) -> SigninDelegateGroupList:
    import aws_sdk_chime.types.signin_delegate_group

    out: SigninDelegateGroupList = []
    for item in data:
        out.append(aws_sdk_chime.types.signin_delegate_group.deserialize_json(item))
    return out
