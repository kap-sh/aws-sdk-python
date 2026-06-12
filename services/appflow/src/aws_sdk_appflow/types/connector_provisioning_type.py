"""Generated from Smithy shape ``com.amazonaws.appflow#ConnectorProvisioningType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appflow.errors import DeserializationError

"""<p>The type of provisioning that the connector supports, such as Lambda.</p>"""
ConnectorProvisioningType: TypeAlias = Literal["LAMBDA",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("LAMBDA",))


def serialize_json(value: ConnectorProvisioningType) -> str:
    return value


def deserialize_json(data: str) -> ConnectorProvisioningType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConnectorProvisioningType value: {data!r}")
    return cast(ConnectorProvisioningType, data)
