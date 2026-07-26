"""Generated from Smithy shape ``com.amazonaws.appflow#ConnectorProfileDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appflow.types.connector_profile

ConnectorProfileDetailList: TypeAlias = list[
    "capo_appflow.types.connector_profile.ConnectorProfile"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorProfileDetailList) -> list:
    import capo_appflow.types.connector_profile

    out: list = []
    for item in value:
        out.append(capo_appflow.types.connector_profile.serialize_json(item))
    return out


def deserialize_json(data: list) -> ConnectorProfileDetailList:
    import capo_appflow.types.connector_profile

    out: ConnectorProfileDetailList = []
    for item in data:
        out.append(capo_appflow.types.connector_profile.deserialize_json(item))
    return out
