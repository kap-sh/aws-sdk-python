"""Generated from Smithy shape ``com.amazonaws.devopsagent#ResourceConfigDnsResolution``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_devops_agent.errors import DeserializationError

"""<p>DNS resolution mode for a Resource Gateway.</p>"""
ResourceConfigDnsResolution: TypeAlias = Literal[
    "PUBLIC",
    "IN_VPC",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PUBLIC",
        "IN_VPC",
    )
)


def serialize_json(value: ResourceConfigDnsResolution) -> str:
    return value


def deserialize_json(data: str) -> ResourceConfigDnsResolution:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ResourceConfigDnsResolution value: {data!r}"
        )
    return cast(ResourceConfigDnsResolution, data)
