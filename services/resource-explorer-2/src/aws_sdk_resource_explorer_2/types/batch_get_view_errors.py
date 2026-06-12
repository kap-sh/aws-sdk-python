"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#BatchGetViewErrors``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_resource_explorer_2.types.batch_get_view_error

BatchGetViewErrors: TypeAlias = list["aws_sdk_resource_explorer_2.types.batch_get_view_error.BatchGetViewError"]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetViewErrors) -> list:
    import aws_sdk_resource_explorer_2.types.batch_get_view_error
    out: list = []
    for item in value:
        out.append(aws_sdk_resource_explorer_2.types.batch_get_view_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchGetViewErrors:
    import aws_sdk_resource_explorer_2.types.batch_get_view_error
    out: BatchGetViewErrors = []
    for item in data:
        out.append(aws_sdk_resource_explorer_2.types.batch_get_view_error.deserialize_json(item))
    return out