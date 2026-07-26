"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2NetworkAclEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_ec2_network_acl_entry

AwsEc2NetworkAclEntryList: TypeAlias = list[
    "capo_securityhub.types.aws_ec2_network_acl_entry.AwsEc2NetworkAclEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2NetworkAclEntryList) -> list:
    import capo_securityhub.types.aws_ec2_network_acl_entry

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_ec2_network_acl_entry.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AwsEc2NetworkAclEntryList:
    import capo_securityhub.types.aws_ec2_network_acl_entry

    out: AwsEc2NetworkAclEntryList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_ec2_network_acl_entry.deserialize_json(item)
        )
    return out
