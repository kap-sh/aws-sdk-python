"""Generated from Smithy shape ``com.amazonaws.emr#PortRanges``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_emr.types.port_range

PortRanges: TypeAlias = list["capo_emr.types.port_range.PortRange"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PortRanges) -> list:
    import capo_emr.types.port_range

    out: list = []
    for item in value:
        out.append(capo_emr.types.port_range.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PortRanges:
    import capo_emr.types.port_range

    out: PortRanges = []
    for item in data:
        out.append(capo_emr.types.port_range.deserialize_aws_json_1_1(item))
    return out
