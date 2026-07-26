"""Generated from Smithy shape ``com.amazonaws.configservice#ConformancePackStatusDetailsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_config_service.types.conformance_pack_status_detail

ConformancePackStatusDetailsList: TypeAlias = list[
    "capo_config_service.types.conformance_pack_status_detail.ConformancePackStatusDetail"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConformancePackStatusDetailsList) -> list:
    import capo_config_service.types.conformance_pack_status_detail

    out: list = []
    for item in value:
        out.append(
            capo_config_service.types.conformance_pack_status_detail.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ConformancePackStatusDetailsList:
    import capo_config_service.types.conformance_pack_status_detail

    out: ConformancePackStatusDetailsList = []
    for item in data:
        out.append(
            capo_config_service.types.conformance_pack_status_detail.deserialize_aws_json_1_1(
                item
            )
        )
    return out
