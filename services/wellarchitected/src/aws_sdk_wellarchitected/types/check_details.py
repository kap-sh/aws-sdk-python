"""Generated from Smithy shape ``com.amazonaws.wellarchitected#CheckDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.check_detail

CheckDetails: TypeAlias = list["aws_sdk_wellarchitected.types.check_detail.CheckDetail"]


# --- restJson1 ser/de ---
def serialize_json(value: CheckDetails) -> list:
    import aws_sdk_wellarchitected.types.check_detail

    out: list = []
    for item in value:
        out.append(aws_sdk_wellarchitected.types.check_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> CheckDetails:
    import aws_sdk_wellarchitected.types.check_detail

    out: CheckDetails = []
    for item in data:
        out.append(aws_sdk_wellarchitected.types.check_detail.deserialize_json(item))
    return out
