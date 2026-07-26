"""Generated from Smithy shape ``com.amazonaws.route53resolver#FirewallDomainImportOperation``."""

from typing import Literal, TypeAlias, cast

FirewallDomainImportOperation: TypeAlias = Literal["REPLACE",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FirewallDomainImportOperation) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FirewallDomainImportOperation:
    return cast(FirewallDomainImportOperation, data)
