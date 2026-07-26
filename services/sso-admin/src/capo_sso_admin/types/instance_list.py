"""Generated from Smithy shape ``com.amazonaws.ssoadmin#InstanceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sso_admin.types.instance_metadata

InstanceList: TypeAlias = list[
    "capo_sso_admin.types.instance_metadata.InstanceMetadata"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceList) -> list:
    import capo_sso_admin.types.instance_metadata

    out: list = []
    for item in value:
        out.append(capo_sso_admin.types.instance_metadata.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> InstanceList:
    import capo_sso_admin.types.instance_metadata

    out: InstanceList = []
    for item in data:
        out.append(
            capo_sso_admin.types.instance_metadata.deserialize_aws_json_1_1(item)
        )
    return out
