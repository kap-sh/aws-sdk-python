"""Generated from Smithy shape ``com.amazonaws.iot#PolicyVersions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.policy_version

PolicyVersions: TypeAlias = list["capo_iot.types.policy_version.PolicyVersion"]


# --- restJson1 ser/de ---
def serialize_json(value: PolicyVersions) -> list:
    import capo_iot.types.policy_version

    out: list = []
    for item in value:
        out.append(capo_iot.types.policy_version.serialize_json(item))
    return out


def deserialize_json(data: list) -> PolicyVersions:
    import capo_iot.types.policy_version

    out: PolicyVersions = []
    for item in data:
        out.append(capo_iot.types.policy_version.deserialize_json(item))
    return out
