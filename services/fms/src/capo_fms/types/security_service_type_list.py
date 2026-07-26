"""Generated from Smithy shape ``com.amazonaws.fms#SecurityServiceTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fms.types.security_service_type

SecurityServiceTypeList: TypeAlias = list[
    "capo_fms.types.security_service_type.SecurityServiceType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SecurityServiceTypeList) -> list:
    import capo_fms.types.security_service_type

    out: list = []
    for item in value:
        out.append(capo_fms.types.security_service_type.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SecurityServiceTypeList:
    import capo_fms.types.security_service_type

    out: SecurityServiceTypeList = []
    for item in data:
        out.append(capo_fms.types.security_service_type.deserialize_aws_json_1_1(item))
    return out
