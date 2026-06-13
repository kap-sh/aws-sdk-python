"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#DocumentDbUngracefulBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_arc_region_switch.errors import DeserializationError

DocumentDbUngracefulBehavior: TypeAlias = Literal["failover",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("failover",))


def serialize_aws_json_1_0(value: DocumentDbUngracefulBehavior) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DocumentDbUngracefulBehavior:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DocumentDbUngracefulBehavior value: {data!r}"
        )
    return cast(DocumentDbUngracefulBehavior, data)
