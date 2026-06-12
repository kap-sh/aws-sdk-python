"""Generated from Smithy shape ``com.amazonaws.networkfirewall#OverrideAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_network_firewall.errors import DeserializationError

OverrideAction: TypeAlias = Literal["DROP_TO_ALERT",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("DROP_TO_ALERT",))


def serialize_aws_json_1_0(value: OverrideAction) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> OverrideAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OverrideAction value: {data!r}")
    return cast(OverrideAction, data)
