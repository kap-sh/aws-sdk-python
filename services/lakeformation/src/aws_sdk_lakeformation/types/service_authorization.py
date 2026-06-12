"""Generated from Smithy shape ``com.amazonaws.lakeformation#ServiceAuthorization``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lakeformation.errors import DeserializationError

"""<p>Authorization status for service integrations. Specify a value of <code>ENABLED</code> or <code>DISABLED</code>.</p>"""
ServiceAuthorization: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: ServiceAuthorization) -> str:
    return value


def deserialize_json(data: str) -> ServiceAuthorization:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ServiceAuthorization value: {data!r}")
    return cast(ServiceAuthorization, data)
