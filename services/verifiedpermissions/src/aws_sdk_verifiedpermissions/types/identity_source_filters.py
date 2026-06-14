"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#IdentitySourceFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.identity_source_filter

IdentitySourceFilters: TypeAlias = list[
    "aws_sdk_verifiedpermissions.types.identity_source_filter.IdentitySourceFilter"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IdentitySourceFilters) -> list:
    import aws_sdk_verifiedpermissions.types.identity_source_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_verifiedpermissions.types.identity_source_filter.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> IdentitySourceFilters:
    import aws_sdk_verifiedpermissions.types.identity_source_filter

    out: IdentitySourceFilters = []
    for item in data:
        out.append(
            aws_sdk_verifiedpermissions.types.identity_source_filter.deserialize_aws_json_1_0(
                item
            )
        )
    return out
