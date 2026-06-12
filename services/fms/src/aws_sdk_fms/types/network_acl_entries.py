"""Generated from Smithy shape ``com.amazonaws.fms#NetworkAclEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fms.types.network_acl_entry

NetworkAclEntries: TypeAlias = list[
    "aws_sdk_fms.types.network_acl_entry.NetworkAclEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NetworkAclEntries) -> list:
    import aws_sdk_fms.types.network_acl_entry

    out: list = []
    for item in value:
        out.append(aws_sdk_fms.types.network_acl_entry.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> NetworkAclEntries:
    import aws_sdk_fms.types.network_acl_entry

    out: NetworkAclEntries = []
    for item in data:
        out.append(aws_sdk_fms.types.network_acl_entry.deserialize_aws_json_1_1(item))
    return out
