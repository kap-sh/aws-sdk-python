"""Generated from Smithy shape ``com.amazonaws.controlcatalog#ObjectiveResourceFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_controlcatalog.types.objective_resource_filter

ObjectiveResourceFilterList: TypeAlias = list[
    "aws_sdk_controlcatalog.types.objective_resource_filter.ObjectiveResourceFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: ObjectiveResourceFilterList) -> list:
    import aws_sdk_controlcatalog.types.objective_resource_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_controlcatalog.types.objective_resource_filter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ObjectiveResourceFilterList:
    import aws_sdk_controlcatalog.types.objective_resource_filter

    out: ObjectiveResourceFilterList = []
    for item in data:
        out.append(
            aws_sdk_controlcatalog.types.objective_resource_filter.deserialize_json(
                item
            )
        )
    return out
