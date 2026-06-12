"""Generated from Smithy shape ``com.amazonaws.securityhub#SensitiveDataResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.sensitive_data_result

SensitiveDataResultList: TypeAlias = list[
    "aws_sdk_securityhub.types.sensitive_data_result.SensitiveDataResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: SensitiveDataResultList) -> list:
    import aws_sdk_securityhub.types.sensitive_data_result

    out: list = []
    for item in value:
        out.append(aws_sdk_securityhub.types.sensitive_data_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> SensitiveDataResultList:
    import aws_sdk_securityhub.types.sensitive_data_result

    out: SensitiveDataResultList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.sensitive_data_result.deserialize_json(item)
        )
    return out
