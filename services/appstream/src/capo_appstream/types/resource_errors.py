"""Generated from Smithy shape ``com.amazonaws.appstream#ResourceErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appstream.types.resource_error

ResourceErrors: TypeAlias = list["capo_appstream.types.resource_error.ResourceError"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceErrors) -> list:
    import capo_appstream.types.resource_error

    out: list = []
    for item in value:
        out.append(capo_appstream.types.resource_error.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ResourceErrors:
    import capo_appstream.types.resource_error

    out: ResourceErrors = []
    for item in data:
        out.append(capo_appstream.types.resource_error.deserialize_aws_json_1_1(item))
    return out
