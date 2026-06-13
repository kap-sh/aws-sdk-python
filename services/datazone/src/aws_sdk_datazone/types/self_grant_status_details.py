"""Generated from Smithy shape ``com.amazonaws.datazone#SelfGrantStatusDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.self_grant_status_detail

SelfGrantStatusDetails: TypeAlias = list[
    "aws_sdk_datazone.types.self_grant_status_detail.SelfGrantStatusDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: SelfGrantStatusDetails) -> list:
    import aws_sdk_datazone.types.self_grant_status_detail

    out: list = []
    for item in value:
        out.append(aws_sdk_datazone.types.self_grant_status_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> SelfGrantStatusDetails:
    import aws_sdk_datazone.types.self_grant_status_detail

    out: SelfGrantStatusDetails = []
    for item in data:
        out.append(
            aws_sdk_datazone.types.self_grant_status_detail.deserialize_json(item)
        )
    return out
