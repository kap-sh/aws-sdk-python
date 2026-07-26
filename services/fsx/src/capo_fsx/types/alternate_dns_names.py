"""Generated from Smithy shape ``com.amazonaws.fsx#AlternateDNSNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fsx.types.alternate_dns_name

AlternateDNSNames: TypeAlias = list[
    "capo_fsx.types.alternate_dns_name.AlternateDNSName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AlternateDNSNames) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AlternateDNSNames:
    return list(data)
