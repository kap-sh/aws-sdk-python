"""Generated from Smithy shape ``com.amazonaws.mailmanager#TrustStoreResponseOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mailmanager.errors import DeserializationError

"""<p>Specifies whether to include trust store contents in the GetIngressPoint response.</p>"""
TrustStoreResponseOption: TypeAlias = Literal[
    "EXCLUDE",
    "INCLUDE",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EXCLUDE",
        "INCLUDE",
    )
)


def serialize_aws_json_1_0(value: TrustStoreResponseOption) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> TrustStoreResponseOption:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TrustStoreResponseOption value: {data!r}")
    return cast(TrustStoreResponseOption, data)
