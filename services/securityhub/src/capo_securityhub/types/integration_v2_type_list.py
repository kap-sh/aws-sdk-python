"""Generated from Smithy shape ``com.amazonaws.securityhub#IntegrationV2TypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.integration_v2_type

IntegrationV2TypeList: TypeAlias = list[
    "capo_securityhub.types.integration_v2_type.IntegrationV2Type"
]


# --- restJson1 ser/de ---
def serialize_json(value: IntegrationV2TypeList) -> list:
    import capo_securityhub.types.integration_v2_type

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.integration_v2_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> IntegrationV2TypeList:
    import capo_securityhub.types.integration_v2_type

    out: IntegrationV2TypeList = []
    for item in data:
        out.append(capo_securityhub.types.integration_v2_type.deserialize_json(item))
    return out
