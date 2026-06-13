"""Generated from Smithy shape ``com.amazonaws.securityagent#IntegratedRepositoryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.integrated_repository

IntegratedRepositoryList: TypeAlias = list[
    "aws_sdk_securityagent.types.integrated_repository.IntegratedRepository"
]


# --- restJson1 ser/de ---
def serialize_json(value: IntegratedRepositoryList) -> list:
    import aws_sdk_securityagent.types.integrated_repository

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityagent.types.integrated_repository.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> IntegratedRepositoryList:
    import aws_sdk_securityagent.types.integrated_repository

    out: IntegratedRepositoryList = []
    for item in data:
        out.append(
            aws_sdk_securityagent.types.integrated_repository.deserialize_json(item)
        )
    return out
