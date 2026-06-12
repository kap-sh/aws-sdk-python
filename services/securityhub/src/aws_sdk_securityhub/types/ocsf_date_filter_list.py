"""Generated from Smithy shape ``com.amazonaws.securityhub#OcsfDateFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.ocsf_date_filter

OcsfDateFilterList: TypeAlias = list[
    "aws_sdk_securityhub.types.ocsf_date_filter.OcsfDateFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: OcsfDateFilterList) -> list:
    import aws_sdk_securityhub.types.ocsf_date_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_securityhub.types.ocsf_date_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> OcsfDateFilterList:
    import aws_sdk_securityhub.types.ocsf_date_filter

    out: OcsfDateFilterList = []
    for item in data:
        out.append(aws_sdk_securityhub.types.ocsf_date_filter.deserialize_json(item))
    return out
