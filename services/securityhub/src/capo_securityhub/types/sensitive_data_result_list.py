"""Generated from Smithy shape ``com.amazonaws.securityhub#SensitiveDataResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.sensitive_data_result

SensitiveDataResultList: TypeAlias = list[
    "capo_securityhub.types.sensitive_data_result.SensitiveDataResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: SensitiveDataResultList) -> list:
    import capo_securityhub.types.sensitive_data_result

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.sensitive_data_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> SensitiveDataResultList:
    import capo_securityhub.types.sensitive_data_result

    out: SensitiveDataResultList = []
    for item in data:
        out.append(capo_securityhub.types.sensitive_data_result.deserialize_json(item))
    return out
