"""Generated from Smithy shape ``com.amazonaws.securityhub#OcsfNumberFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.ocsf_number_filter

OcsfNumberFilterList: TypeAlias = list[
    "aws_sdk_securityhub.types.ocsf_number_filter.OcsfNumberFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: OcsfNumberFilterList) -> list:
    import aws_sdk_securityhub.types.ocsf_number_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_securityhub.types.ocsf_number_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> OcsfNumberFilterList:
    import aws_sdk_securityhub.types.ocsf_number_filter

    out: OcsfNumberFilterList = []
    for item in data:
        out.append(aws_sdk_securityhub.types.ocsf_number_filter.deserialize_json(item))
    return out
