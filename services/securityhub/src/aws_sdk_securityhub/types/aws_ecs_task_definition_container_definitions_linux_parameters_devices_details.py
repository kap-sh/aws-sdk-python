"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.non_empty_string_list


class AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetails(
    TypedDict, closed=True
):
    container_path: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The path inside the container at which to expose the host device.</p>"""
    host_path: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The path for the device on the host container instance.</p>"""
    permissions: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>The explicit permissions to provide to the container for the device. By default, the container has permissions for read, write, and <code>mknod</code> for the device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetails,
) -> dict:
    out: dict = {}
    if "container_path" in value:
        out["ContainerPath"] = value["container_path"]
    if "host_path" in value:
        out["HostPath"] = value["host_path"]
    if "permissions" in value:
        import aws_sdk_securityhub.types.non_empty_string_list

        out["Permissions"] = (
            aws_sdk_securityhub.types.non_empty_string_list.serialize_json(
                value["permissions"]
            )
        )
    return out


def deserialize_json(
    data: dict,
) -> AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetails:
    out: AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetails = {}  # type: ignore[typeddict-item]
    if "ContainerPath" in data:
        out["container_path"] = data["ContainerPath"]
    if "HostPath" in data:
        out["host_path"] = data["HostPath"]
    if "Permissions" in data:
        import aws_sdk_securityhub.types.non_empty_string_list

        out["permissions"] = (
            aws_sdk_securityhub.types.non_empty_string_list.deserialize_json(
                data["Permissions"]
            )
        )
    return out
