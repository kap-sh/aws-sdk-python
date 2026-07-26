"""Generated from Smithy shape ``com.amazonaws.lightsail#HeaderForwardList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.header_enum

HeaderForwardList: TypeAlias = list["capo_lightsail.types.header_enum.HeaderEnum"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HeaderForwardList) -> list:
    import capo_lightsail.types.header_enum

    out: list = []
    for item in value:
        out.append(capo_lightsail.types.header_enum.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> HeaderForwardList:
    import capo_lightsail.types.header_enum

    out: HeaderForwardList = []
    for item in data:
        out.append(capo_lightsail.types.header_enum.deserialize_aws_json_1_1(item))
    return out
