"""Generated from Smithy shape ``com.amazonaws.datazone#ManagedPolicyType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_datazone.errors import DeserializationError
from aws_sdk_datazone._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

ManagedPolicyType: TypeAlias = Literal[
    "CREATE_DOMAIN_UNIT",
    "OVERRIDE_DOMAIN_UNIT_OWNERS",
    "ADD_TO_PROJECT_MEMBER_POOL",
    "OVERRIDE_PROJECT_OWNERS",
    "CREATE_GLOSSARY",
    "CREATE_FORM_TYPE",
    "CREATE_ASSET_TYPE",
    "CREATE_PROJECT",
    "CREATE_ENVIRONMENT_PROFILE",
    "DELEGATE_CREATE_ENVIRONMENT_PROFILE",
    "CREATE_ENVIRONMENT",
    "CREATE_ENVIRONMENT_FROM_BLUEPRINT",
    "CREATE_PROJECT_FROM_PROJECT_PROFILE",
    "USE_ASSET_TYPE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATE_DOMAIN_UNIT",
        "OVERRIDE_DOMAIN_UNIT_OWNERS",
        "ADD_TO_PROJECT_MEMBER_POOL",
        "OVERRIDE_PROJECT_OWNERS",
        "CREATE_GLOSSARY",
        "CREATE_FORM_TYPE",
        "CREATE_ASSET_TYPE",
        "CREATE_PROJECT",
        "CREATE_ENVIRONMENT_PROFILE",
        "DELEGATE_CREATE_ENVIRONMENT_PROFILE",
        "CREATE_ENVIRONMENT",
        "CREATE_ENVIRONMENT_FROM_BLUEPRINT",
        "CREATE_PROJECT_FROM_PROJECT_PROFILE",
        "USE_ASSET_TYPE",
    )
)


def serialize_json(value: ManagedPolicyType) -> str:
    return value


def deserialize_json(data: str) -> ManagedPolicyType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ManagedPolicyType value: {data!r}")
    return cast(ManagedPolicyType, data)
