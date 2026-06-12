"""Generated from Smithy shape ``com.amazonaws.mturk#HITAccessActions``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mturk.errors import DeserializationError

HITAccessActions: TypeAlias = Literal[
    "Accept",
    "PreviewAndAccept",
    "DiscoverPreviewAndAccept",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Accept",
        "PreviewAndAccept",
        "DiscoverPreviewAndAccept",
    )
)


def serialize_aws_json_1_1(value: HITAccessActions) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HITAccessActions:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HITAccessActions value: {data!r}")
    return cast(HITAccessActions, data)
