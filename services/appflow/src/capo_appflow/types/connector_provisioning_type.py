"""Generated from Smithy shape ``com.amazonaws.appflow#ConnectorProvisioningType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of provisioning that the connector supports, such as Lambda.</p>"""
ConnectorProvisioningType: TypeAlias = Literal["LAMBDA",]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorProvisioningType) -> str:
    return value


def deserialize_json(data: str) -> ConnectorProvisioningType:
    return cast(ConnectorProvisioningType, data)
