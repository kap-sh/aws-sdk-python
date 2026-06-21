"""Generated from Smithy shape ``com.amazonaws.route53resolver#FirewallFailOpenStatus``."""

from typing import Literal, TypeAlias, cast

FirewallFailOpenStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
    "USE_LOCAL_RESOURCE_SETTING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FirewallFailOpenStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FirewallFailOpenStatus:
    return cast(FirewallFailOpenStatus, data)
