"""Generated from Smithy shape ``com.amazonaws.route53resolver#FirewallDomainImportOperation``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route53resolver.errors import DeserializationError

FirewallDomainImportOperation: TypeAlias = Literal["REPLACE",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("REPLACE",))


def serialize_aws_json_1_1(value: FirewallDomainImportOperation) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FirewallDomainImportOperation:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown FirewallDomainImportOperation value: {data!r}"
        )
    return cast(FirewallDomainImportOperation, data)
