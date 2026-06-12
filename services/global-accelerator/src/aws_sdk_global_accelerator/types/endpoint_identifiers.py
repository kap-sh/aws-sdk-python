"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#EndpointIdentifiers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.endpoint_identifier

EndpointIdentifiers: TypeAlias = list[
    "aws_sdk_global_accelerator.types.endpoint_identifier.EndpointIdentifier"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EndpointIdentifiers) -> list:
    import aws_sdk_global_accelerator.types.endpoint_identifier

    out: list = []
    for item in value:
        out.append(
            aws_sdk_global_accelerator.types.endpoint_identifier.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EndpointIdentifiers:
    import aws_sdk_global_accelerator.types.endpoint_identifier

    out: EndpointIdentifiers = []
    for item in data:
        out.append(
            aws_sdk_global_accelerator.types.endpoint_identifier.deserialize_aws_json_1_1(
                item
            )
        )
    return out
