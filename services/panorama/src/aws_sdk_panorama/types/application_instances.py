"""Generated from Smithy shape ``com.amazonaws.panorama#ApplicationInstances``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_panorama.types.application_instance

ApplicationInstances: TypeAlias = list[
    "aws_sdk_panorama.types.application_instance.ApplicationInstance"
]


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationInstances) -> list:
    import aws_sdk_panorama.types.application_instance

    out: list = []
    for item in value:
        out.append(aws_sdk_panorama.types.application_instance.serialize_json(item))
    return out


def deserialize_json(data: list) -> ApplicationInstances:
    import aws_sdk_panorama.types.application_instance

    out: ApplicationInstances = []
    for item in data:
        out.append(aws_sdk_panorama.types.application_instance.deserialize_json(item))
    return out
