"""Generated from Smithy shape ``com.amazonaws.eks#LogSetups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_eks.types.log_setup

LogSetups: TypeAlias = list["aws_sdk_eks.types.log_setup.LogSetup"]


# --- restJson1 ser/de ---
def serialize_json(value: LogSetups) -> list:
    import aws_sdk_eks.types.log_setup

    out: list = []
    for item in value:
        out.append(aws_sdk_eks.types.log_setup.serialize_json(item))
    return out


def deserialize_json(data: list) -> LogSetups:
    import aws_sdk_eks.types.log_setup

    out: LogSetups = []
    for item in data:
        out.append(aws_sdk_eks.types.log_setup.deserialize_json(item))
    return out
