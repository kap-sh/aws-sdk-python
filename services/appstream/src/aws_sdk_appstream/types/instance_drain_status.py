"""Generated from Smithy shape ``com.amazonaws.appstream#InstanceDrainStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appstream.errors import DeserializationError

"""<p>Possible values for the drain status of a streaming instance.</p>"""
InstanceDrainStatus: TypeAlias = Literal[
    "ACTIVE",
    "DRAINING",
    "NOT_APPLICABLE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "DRAINING",
        "NOT_APPLICABLE",
    )
)


def serialize_aws_json_1_1(value: InstanceDrainStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstanceDrainStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InstanceDrainStatus value: {data!r}")
    return cast(InstanceDrainStatus, data)
