"""Generated from Smithy shape ``com.amazonaws.lightsail#RegisterContainerImageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.container_label
    import aws_sdk_lightsail.types.container_service_name
    import aws_sdk_lightsail.types.string


class RegisterContainerImageRequest(TypedDict, closed=True):
    service_name: "aws_sdk_lightsail.types.container_service_name.ContainerServiceName"
    """<p>The name of the container service for which to register a container image.</p>"""
    label: "aws_sdk_lightsail.types.container_label.ContainerLabel"
    """<p>The label for the container image when it's registered to the container service.</p> <p>Use a descriptive label that you can use to track the different versions of your registered container images.</p> <p>Use the <code>GetContainerImages</code> action to return the container images registered to a Lightsail container service. The label is the <code><imagelabel></code> portion of the following image name example:</p> <ul> <li> <p> <code>:container-service-1.<imagelabel>.1</code> </p> </li> </ul> <p>If the name of your container service is <code>mycontainerservice</code>, and the label that you specify is <code>mystaticwebsite</code>, then the name of the registered container image will be <code>:mycontainerservice.mystaticwebsite.1</code>.</p> <p>The number at the end of these image name examples represents the version of the registered container image. If you push and register another container image to the same Lightsail container service, with the same label, then the version number for the new registered container image will be <code>2</code>. If you push and register another container image, the version number will be <code>3</code>, and so on.</p>"""
    digest: "aws_sdk_lightsail.types.string.string"
    """<p>The digest of the container image to be registered.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegisterContainerImageRequest) -> dict:
    out: dict = {}
    out["label"] = value["label"]
    out["digest"] = value["digest"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RegisterContainerImageRequest:
    out: RegisterContainerImageRequest = {}  # type: ignore[typeddict-item]
    if "label" in data:
        out["label"] = data["label"]
    else:
        raise DeserializationError("RegisterContainerImageRequest.label required")
    if "digest" in data:
        out["digest"] = data["digest"]
    else:
        raise DeserializationError("RegisterContainerImageRequest.digest required")
    return out
