"""Generated from Smithy shape ``com.amazonaws.servicecatalog#LaunchPaths``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.launch_path

LaunchPaths: TypeAlias = list["aws_sdk_service_catalog.types.launch_path.LaunchPath"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LaunchPaths) -> list:
    import aws_sdk_service_catalog.types.launch_path

    out: list = []
    for item in value:
        out.append(
            aws_sdk_service_catalog.types.launch_path.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> LaunchPaths:
    import aws_sdk_service_catalog.types.launch_path

    out: LaunchPaths = []
    for item in data:
        out.append(
            aws_sdk_service_catalog.types.launch_path.deserialize_aws_json_1_1(item)
        )
    return out
