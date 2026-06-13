"""Generated from Smithy shape ``com.amazonaws.securitylake#DataLakeLifecycleTransitionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securitylake.types.data_lake_lifecycle_transition

DataLakeLifecycleTransitionList: TypeAlias = list[
    "aws_sdk_securitylake.types.data_lake_lifecycle_transition.DataLakeLifecycleTransition"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataLakeLifecycleTransitionList) -> list:
    import aws_sdk_securitylake.types.data_lake_lifecycle_transition

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securitylake.types.data_lake_lifecycle_transition.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DataLakeLifecycleTransitionList:
    import aws_sdk_securitylake.types.data_lake_lifecycle_transition

    out: DataLakeLifecycleTransitionList = []
    for item in data:
        out.append(
            aws_sdk_securitylake.types.data_lake_lifecycle_transition.deserialize_json(
                item
            )
        )
    return out
