"""Generated from Smithy shape ``com.amazonaws.securityir#ImpactedAwsRegionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_security_ir.types.impacted_aws_region

ImpactedAwsRegionList: TypeAlias = list[
    "aws_sdk_security_ir.types.impacted_aws_region.ImpactedAwsRegion"
]


# --- restJson1 ser/de ---
def serialize_json(value: ImpactedAwsRegionList) -> list:
    import aws_sdk_security_ir.types.impacted_aws_region

    out: list = []
    for item in value:
        out.append(aws_sdk_security_ir.types.impacted_aws_region.serialize_json(item))
    return out


def deserialize_json(data: list) -> ImpactedAwsRegionList:
    import aws_sdk_security_ir.types.impacted_aws_region

    out: ImpactedAwsRegionList = []
    for item in data:
        out.append(aws_sdk_security_ir.types.impacted_aws_region.deserialize_json(item))
    return out
