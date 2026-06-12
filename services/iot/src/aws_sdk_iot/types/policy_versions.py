"""Generated from Smithy shape ``com.amazonaws.iot#PolicyVersions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.policy_version

PolicyVersions: TypeAlias = list["aws_sdk_iot.types.policy_version.PolicyVersion"]


# --- restJson1 ser/de ---
def serialize_json(value: PolicyVersions) -> list:
    import aws_sdk_iot.types.policy_version

    out: list = []
    for item in value:
        out.append(aws_sdk_iot.types.policy_version.serialize_json(item))
    return out


def deserialize_json(data: list) -> PolicyVersions:
    import aws_sdk_iot.types.policy_version

    out: PolicyVersions = []
    for item in data:
        out.append(aws_sdk_iot.types.policy_version.deserialize_json(item))
    return out
