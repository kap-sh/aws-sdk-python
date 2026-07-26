"""Generated from Smithy shape ``com.amazonaws.directoryservice#ConditionalForwarders``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_directory_service.types.conditional_forwarder

ConditionalForwarders: TypeAlias = list[
    "capo_directory_service.types.conditional_forwarder.ConditionalForwarder"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConditionalForwarders) -> list:
    import capo_directory_service.types.conditional_forwarder

    out: list = []
    for item in value:
        out.append(
            capo_directory_service.types.conditional_forwarder.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ConditionalForwarders:
    import capo_directory_service.types.conditional_forwarder

    out: ConditionalForwarders = []
    for item in data:
        out.append(
            capo_directory_service.types.conditional_forwarder.deserialize_aws_json_1_1(
                item
            )
        )
    return out
