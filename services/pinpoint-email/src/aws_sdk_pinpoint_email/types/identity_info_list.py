"""Generated from Smithy shape ``com.amazonaws.pinpointemail#IdentityInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint_email.types.identity_info

IdentityInfoList: TypeAlias = list[
    "aws_sdk_pinpoint_email.types.identity_info.IdentityInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: IdentityInfoList) -> list:
    import aws_sdk_pinpoint_email.types.identity_info

    out: list = []
    for item in value:
        out.append(aws_sdk_pinpoint_email.types.identity_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> IdentityInfoList:
    import aws_sdk_pinpoint_email.types.identity_info

    out: IdentityInfoList = []
    for item in data:
        out.append(aws_sdk_pinpoint_email.types.identity_info.deserialize_json(item))
    return out
