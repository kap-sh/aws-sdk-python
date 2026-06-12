"""Generated from Smithy shape ``com.amazonaws.glacier#AccessControlPolicyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glacier.types.grant

AccessControlPolicyList: TypeAlias = list["aws_sdk_glacier.types.grant.Grant"]


# --- restJson1 ser/de ---
def serialize_json(value: AccessControlPolicyList) -> list:
    import aws_sdk_glacier.types.grant

    out: list = []
    for item in value:
        out.append(aws_sdk_glacier.types.grant.serialize_json(item))
    return out


def deserialize_json(data: list) -> AccessControlPolicyList:
    import aws_sdk_glacier.types.grant

    out: AccessControlPolicyList = []
    for item in data:
        out.append(aws_sdk_glacier.types.grant.deserialize_json(item))
    return out
