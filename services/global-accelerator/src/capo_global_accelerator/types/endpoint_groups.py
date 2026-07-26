"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#EndpointGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_global_accelerator.types.endpoint_group

EndpointGroups: TypeAlias = list[
    "capo_global_accelerator.types.endpoint_group.EndpointGroup"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EndpointGroups) -> list:
    import capo_global_accelerator.types.endpoint_group

    out: list = []
    for item in value:
        out.append(
            capo_global_accelerator.types.endpoint_group.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EndpointGroups:
    import capo_global_accelerator.types.endpoint_group

    out: EndpointGroups = []
    for item in data:
        out.append(
            capo_global_accelerator.types.endpoint_group.deserialize_aws_json_1_1(item)
        )
    return out
