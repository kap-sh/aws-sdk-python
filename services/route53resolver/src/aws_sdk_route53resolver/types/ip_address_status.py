"""Generated from Smithy shape ``com.amazonaws.route53resolver#IpAddressStatus``."""

from typing import Literal, TypeAlias, cast

IpAddressStatus: TypeAlias = Literal[
    "CREATING",
    "FAILED_CREATION",
    "ATTACHING",
    "ATTACHED",
    "REMAP_DETACHING",
    "REMAP_ATTACHING",
    "DETACHING",
    "FAILED_RESOURCE_GONE",
    "DELETING",
    "DELETE_FAILED_FAS_EXPIRED",
    "UPDATING",
    "UPDATE_FAILED",
    "ISOLATED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IpAddressStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IpAddressStatus:
    return cast(IpAddressStatus, data)
