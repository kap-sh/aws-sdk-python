"""Generated from Smithy shape ``com.amazonaws.fms#NetworkAclRuleAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fms.errors import DeserializationError

NetworkAclRuleAction: TypeAlias = Literal[
    "allow",
    "deny",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "allow",
        "deny",
    )
)


def serialize_aws_json_1_1(value: NetworkAclRuleAction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NetworkAclRuleAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NetworkAclRuleAction value: {data!r}")
    return cast(NetworkAclRuleAction, data)
