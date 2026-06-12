"""Generated from Smithy shape ``com.amazonaws.macie2#SensitiveData``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_macie2.types.sensitive_data_item

SensitiveData: TypeAlias = list[
    "aws_sdk_macie2.types.sensitive_data_item.SensitiveDataItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: SensitiveData) -> list:
    import aws_sdk_macie2.types.sensitive_data_item

    out: list = []
    for item in value:
        out.append(aws_sdk_macie2.types.sensitive_data_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> SensitiveData:
    import aws_sdk_macie2.types.sensitive_data_item

    out: SensitiveData = []
    for item in data:
        out.append(aws_sdk_macie2.types.sensitive_data_item.deserialize_json(item))
    return out
