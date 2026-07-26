"""Generated from Smithy shape ``com.amazonaws.batch#ServiceEnvironmentDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_batch.types.service_environment_detail

ServiceEnvironmentDetailList: TypeAlias = list[
    "capo_batch.types.service_environment_detail.ServiceEnvironmentDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceEnvironmentDetailList) -> list:
    import capo_batch.types.service_environment_detail

    out: list = []
    for item in value:
        out.append(capo_batch.types.service_environment_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> ServiceEnvironmentDetailList:
    import capo_batch.types.service_environment_detail

    out: ServiceEnvironmentDetailList = []
    for item in data:
        out.append(capo_batch.types.service_environment_detail.deserialize_json(item))
    return out
