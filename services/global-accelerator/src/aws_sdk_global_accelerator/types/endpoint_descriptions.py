"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#EndpointDescriptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.endpoint_description

EndpointDescriptions: TypeAlias = list[
    "aws_sdk_global_accelerator.types.endpoint_description.EndpointDescription"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EndpointDescriptions) -> list:
    import aws_sdk_global_accelerator.types.endpoint_description

    out: list = []
    for item in value:
        out.append(
            aws_sdk_global_accelerator.types.endpoint_description.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EndpointDescriptions:
    import aws_sdk_global_accelerator.types.endpoint_description

    out: EndpointDescriptions = []
    for item in data:
        out.append(
            aws_sdk_global_accelerator.types.endpoint_description.deserialize_aws_json_1_1(
                item
            )
        )
    return out
