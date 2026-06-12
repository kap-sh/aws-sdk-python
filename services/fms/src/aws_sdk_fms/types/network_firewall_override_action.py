"""Generated from Smithy shape ``com.amazonaws.fms#NetworkFirewallOverrideAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fms.errors import DeserializationError

NetworkFirewallOverrideAction: TypeAlias = Literal["DROP_TO_ALERT",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("DROP_TO_ALERT",))


def serialize_aws_json_1_1(value: NetworkFirewallOverrideAction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NetworkFirewallOverrideAction:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown NetworkFirewallOverrideAction value: {data!r}"
        )
    return cast(NetworkFirewallOverrideAction, data)
