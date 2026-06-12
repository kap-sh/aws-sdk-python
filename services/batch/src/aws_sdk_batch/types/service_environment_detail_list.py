"""Generated from Smithy shape ``com.amazonaws.batch#ServiceEnvironmentDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_batch.types.service_environment_detail

ServiceEnvironmentDetailList: TypeAlias = list[
    "aws_sdk_batch.types.service_environment_detail.ServiceEnvironmentDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceEnvironmentDetailList) -> list:
    import aws_sdk_batch.types.service_environment_detail

    out: list = []
    for item in value:
        out.append(aws_sdk_batch.types.service_environment_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> ServiceEnvironmentDetailList:
    import aws_sdk_batch.types.service_environment_detail

    out: ServiceEnvironmentDetailList = []
    for item in data:
        out.append(
            aws_sdk_batch.types.service_environment_detail.deserialize_json(item)
        )
    return out
