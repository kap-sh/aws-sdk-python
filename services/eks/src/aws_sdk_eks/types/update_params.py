"""Generated from Smithy shape ``com.amazonaws.eks#UpdateParams``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_eks.types.update_param

UpdateParams: TypeAlias = list["aws_sdk_eks.types.update_param.UpdateParam"]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateParams) -> list:
    import aws_sdk_eks.types.update_param

    out: list = []
    for item in value:
        out.append(aws_sdk_eks.types.update_param.serialize_json(item))
    return out


def deserialize_json(data: list) -> UpdateParams:
    import aws_sdk_eks.types.update_param

    out: UpdateParams = []
    for item in data:
        out.append(aws_sdk_eks.types.update_param.deserialize_json(item))
    return out
