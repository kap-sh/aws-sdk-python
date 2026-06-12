"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ResourceDriftList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.resource_drift

ResourceDriftList: TypeAlias = list[
    "aws_sdk_resiliencehub.types.resource_drift.ResourceDrift"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceDriftList) -> list:
    import aws_sdk_resiliencehub.types.resource_drift

    out: list = []
    for item in value:
        out.append(aws_sdk_resiliencehub.types.resource_drift.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResourceDriftList:
    import aws_sdk_resiliencehub.types.resource_drift

    out: ResourceDriftList = []
    for item in data:
        out.append(aws_sdk_resiliencehub.types.resource_drift.deserialize_json(item))
    return out
