"""Generated from Smithy shape ``com.amazonaws.lightsail#CreateContainerServiceRegistryLoginResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.container_service_registry_login


class CreateContainerServiceRegistryLoginResult(TypedDict):
    registry_login: NotRequired[
        "aws_sdk_lightsail.types.container_service_registry_login.ContainerServiceRegistryLogin"
    ]
    """<p>An object that describes the log in information for the container service registry of your Lightsail account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateContainerServiceRegistryLoginResult) -> dict:
    out: dict = {}
    if "registry_login" in value:
        import aws_sdk_lightsail.types.container_service_registry_login

        out["registryLogin"] = (
            aws_sdk_lightsail.types.container_service_registry_login.serialize_aws_json_1_1(
                value["registry_login"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateContainerServiceRegistryLoginResult:
    out: CreateContainerServiceRegistryLoginResult = {}  # type: ignore[typeddict-item]
    if "registryLogin" in data:
        import aws_sdk_lightsail.types.container_service_registry_login

        out["registry_login"] = (
            aws_sdk_lightsail.types.container_service_registry_login.deserialize_aws_json_1_1(
                data["registryLogin"]
            )
        )
    return out
