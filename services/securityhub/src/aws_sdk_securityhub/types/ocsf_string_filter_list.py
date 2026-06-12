"""Generated from Smithy shape ``com.amazonaws.securityhub#OcsfStringFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.ocsf_string_filter

OcsfStringFilterList: TypeAlias = list[
    "aws_sdk_securityhub.types.ocsf_string_filter.OcsfStringFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: OcsfStringFilterList) -> list:
    import aws_sdk_securityhub.types.ocsf_string_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_securityhub.types.ocsf_string_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> OcsfStringFilterList:
    import aws_sdk_securityhub.types.ocsf_string_filter

    out: OcsfStringFilterList = []
    for item in data:
        out.append(aws_sdk_securityhub.types.ocsf_string_filter.deserialize_json(item))
    return out
