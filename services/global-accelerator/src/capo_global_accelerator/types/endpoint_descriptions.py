"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#EndpointDescriptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_global_accelerator.types.endpoint_description

EndpointDescriptions: TypeAlias = list[
    "capo_global_accelerator.types.endpoint_description.EndpointDescription"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EndpointDescriptions) -> list:
    import capo_global_accelerator.types.endpoint_description

    out: list = []
    for item in value:
        out.append(
            capo_global_accelerator.types.endpoint_description.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EndpointDescriptions:
    import capo_global_accelerator.types.endpoint_description

    out: EndpointDescriptions = []
    for item in data:
        out.append(
            capo_global_accelerator.types.endpoint_description.deserialize_aws_json_1_1(
                item
            )
        )
    return out
