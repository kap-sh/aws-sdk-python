"""Generated from Smithy shape ``com.amazonaws.devopsagent#AuthFlow``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_devops_agent.errors import DeserializationError

"""<p>Authentication flow type for operator app.</p>"""
AuthFlow: TypeAlias = Literal[
    "iam",
    "idc",
    "idp",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "iam",
        "idc",
        "idp",
    )
)


def serialize_json(value: AuthFlow) -> str:
    return value


def deserialize_json(data: str) -> AuthFlow:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AuthFlow value: {data!r}")
    return cast(AuthFlow, data)
