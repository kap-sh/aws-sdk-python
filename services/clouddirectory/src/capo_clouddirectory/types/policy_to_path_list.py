"""Generated from Smithy shape ``com.amazonaws.clouddirectory#PolicyToPathList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_clouddirectory.types.policy_to_path

PolicyToPathList: TypeAlias = list[
    "capo_clouddirectory.types.policy_to_path.PolicyToPath"
]


# --- restJson1 ser/de ---
def serialize_json(value: PolicyToPathList) -> list:
    import capo_clouddirectory.types.policy_to_path

    out: list = []
    for item in value:
        out.append(capo_clouddirectory.types.policy_to_path.serialize_json(item))
    return out


def deserialize_json(data: list) -> PolicyToPathList:
    import capo_clouddirectory.types.policy_to_path

    out: PolicyToPathList = []
    for item in data:
        out.append(capo_clouddirectory.types.policy_to_path.deserialize_json(item))
    return out
