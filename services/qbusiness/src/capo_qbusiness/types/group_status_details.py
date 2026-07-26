"""Generated from Smithy shape ``com.amazonaws.qbusiness#GroupStatusDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qbusiness.types.group_status_detail

GroupStatusDetails: TypeAlias = list[
    "capo_qbusiness.types.group_status_detail.GroupStatusDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: GroupStatusDetails) -> list:
    import capo_qbusiness.types.group_status_detail

    out: list = []
    for item in value:
        out.append(capo_qbusiness.types.group_status_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> GroupStatusDetails:
    import capo_qbusiness.types.group_status_detail

    out: GroupStatusDetails = []
    for item in data:
        out.append(capo_qbusiness.types.group_status_detail.deserialize_json(item))
    return out
