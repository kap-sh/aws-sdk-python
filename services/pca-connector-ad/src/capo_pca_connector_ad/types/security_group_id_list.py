"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#SecurityGroupIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pca_connector_ad.types.security_group_id

SecurityGroupIdList: TypeAlias = list[
    "capo_pca_connector_ad.types.security_group_id.SecurityGroupId"
]


# --- restJson1 ser/de ---
def serialize_json(value: SecurityGroupIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> SecurityGroupIdList:
    return list(data)
