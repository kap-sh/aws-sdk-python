"""Generated from Smithy shape ``com.amazonaws.ssmquicksetup#FiltersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm_quicksetup.types.filter

FiltersList: TypeAlias = list["aws_sdk_ssm_quicksetup.types.filter.Filter"]


# --- restJson1 ser/de ---
def serialize_json(value: FiltersList) -> list:
    import aws_sdk_ssm_quicksetup.types.filter

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm_quicksetup.types.filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> FiltersList:
    import aws_sdk_ssm_quicksetup.types.filter

    out: FiltersList = []
    for item in data:
        out.append(aws_sdk_ssm_quicksetup.types.filter.deserialize_json(item))
    return out
