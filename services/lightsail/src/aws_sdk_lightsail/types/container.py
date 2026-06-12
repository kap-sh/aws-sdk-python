"""Generated from Smithy shape ``com.amazonaws.lightsail#Container``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.environment
    import aws_sdk_lightsail.types.port_map
    import aws_sdk_lightsail.types.string
    import aws_sdk_lightsail.types.string_list


class Container(TypedDict):
    image: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The name of the image used for the container.</p> <p>Container images sourced from your Lightsail container service, that are registered and stored on your service, start with a colon (<code>:</code>). For example, if your container service name is <code>container-service-1</code>, the container image label is <code>mystaticsite</code>, and you want to use the third (<code>3</code>) version of the registered container image, then you should specify <code>:container-service-1.mystaticsite.3</code>. To use the latest version of a container image, specify <code>latest</code> instead of a version number (for example, <code>:container-service-1.mystaticsite.latest</code>). Lightsail will automatically use the highest numbered version of the registered container image.</p> <p>Container images sourced from a public registry like Docker Hub don't start with a colon. For example, <code>nginx:latest</code> or <code>nginx</code>.</p>"""
    command: NotRequired["aws_sdk_lightsail.types.string_list.StringList"]
    """<p>The launch command for the container.</p>"""
    environment: NotRequired["aws_sdk_lightsail.types.environment.Environment"]
    """<p>The environment variables of the container.</p>"""
    ports: NotRequired["aws_sdk_lightsail.types.port_map.PortMap"]
    """<p>The open firewall ports of the container.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Container) -> dict:
    out: dict = {}
    if "image" in value:
        out["image"] = value["image"]
    if "command" in value:
        import aws_sdk_lightsail.types.string_list

        out["command"] = aws_sdk_lightsail.types.string_list.serialize_aws_json_1_1(
            value["command"]
        )
    if "environment" in value:
        import aws_sdk_lightsail.types.environment

        out["environment"] = aws_sdk_lightsail.types.environment.serialize_aws_json_1_1(
            value["environment"]
        )
    if "ports" in value:
        import aws_sdk_lightsail.types.port_map

        out["ports"] = aws_sdk_lightsail.types.port_map.serialize_aws_json_1_1(
            value["ports"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Container:
    out: Container = {}  # type: ignore[typeddict-item]
    if "image" in data:
        out["image"] = data["image"]
    if "command" in data:
        import aws_sdk_lightsail.types.string_list

        out["command"] = aws_sdk_lightsail.types.string_list.deserialize_aws_json_1_1(
            data["command"]
        )
    if "environment" in data:
        import aws_sdk_lightsail.types.environment

        out["environment"] = (
            aws_sdk_lightsail.types.environment.deserialize_aws_json_1_1(
                data["environment"]
            )
        )
    if "ports" in data:
        import aws_sdk_lightsail.types.port_map

        out["ports"] = aws_sdk_lightsail.types.port_map.deserialize_aws_json_1_1(
            data["ports"]
        )
    return out
