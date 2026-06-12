"""Generated from Smithy shape ``com.amazonaws.configservice#ConformancePackDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_config_service.types.conformance_pack_detail

ConformancePackDetailList: TypeAlias = list[
    "aws_sdk_config_service.types.conformance_pack_detail.ConformancePackDetail"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConformancePackDetailList) -> list:
    import aws_sdk_config_service.types.conformance_pack_detail

    out: list = []
    for item in value:
        out.append(
            aws_sdk_config_service.types.conformance_pack_detail.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ConformancePackDetailList:
    import aws_sdk_config_service.types.conformance_pack_detail

    out: ConformancePackDetailList = []
    for item in data:
        out.append(
            aws_sdk_config_service.types.conformance_pack_detail.deserialize_aws_json_1_1(
                item
            )
        )
    return out
