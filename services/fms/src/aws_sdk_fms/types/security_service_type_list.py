"""Generated from Smithy shape ``com.amazonaws.fms#SecurityServiceTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fms.types.security_service_type

SecurityServiceTypeList: TypeAlias = list[
    "aws_sdk_fms.types.security_service_type.SecurityServiceType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SecurityServiceTypeList) -> list:
    import aws_sdk_fms.types.security_service_type

    out: list = []
    for item in value:
        out.append(aws_sdk_fms.types.security_service_type.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SecurityServiceTypeList:
    import aws_sdk_fms.types.security_service_type

    out: SecurityServiceTypeList = []
    for item in data:
        out.append(
            aws_sdk_fms.types.security_service_type.deserialize_aws_json_1_1(item)
        )
    return out
