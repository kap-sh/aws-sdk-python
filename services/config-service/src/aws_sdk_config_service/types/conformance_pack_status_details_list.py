"""Generated from Smithy shape ``com.amazonaws.configservice#ConformancePackStatusDetailsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_config_service.types.conformance_pack_status_detail

ConformancePackStatusDetailsList: TypeAlias = list[
    "aws_sdk_config_service.types.conformance_pack_status_detail.ConformancePackStatusDetail"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConformancePackStatusDetailsList) -> list:
    import aws_sdk_config_service.types.conformance_pack_status_detail

    out: list = []
    for item in value:
        out.append(
            aws_sdk_config_service.types.conformance_pack_status_detail.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ConformancePackStatusDetailsList:
    import aws_sdk_config_service.types.conformance_pack_status_detail

    out: ConformancePackStatusDetailsList = []
    for item in data:
        out.append(
            aws_sdk_config_service.types.conformance_pack_status_detail.deserialize_aws_json_1_1(
                item
            )
        )
    return out
