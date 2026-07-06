"""Generated from Smithy shape ``com.amazonaws.ecs#DockerVolumeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boxed_boolean
    import aws_sdk_ecs.types.scope
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.string_map


class DockerVolumeConfiguration(TypedDict, closed=True):
    scope: NotRequired["aws_sdk_ecs.types.scope.Scope"]
    """<p>The scope for the Docker volume that determines its lifecycle. Docker volumes that are scoped to a <code>task</code> are automatically provisioned when the task starts and destroyed when the task stops. Docker volumes that are scoped as <code>shared</code> persist after the task stops.</p>"""
    autoprovision: NotRequired["aws_sdk_ecs.types.boxed_boolean.BoxedBoolean"]
    """<p>If this value is <code>true</code>, the Docker volume is created if it doesn't already exist.</p> <note> <p>This field is only used if the <code>scope</code> is <code>shared</code>.</p> </note>"""
    driver: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Docker volume driver to use. The driver value must match the driver name provided by Docker because it is used for task placement. If the driver was installed using the Docker plugin CLI, use <code>docker plugin ls</code> to retrieve the driver name from your container instance. If the driver was installed using another method, use Docker plugin discovery to retrieve the driver name. This parameter maps to <code>Driver</code> in the docker container create command and the <code>xxdriver</code> option to docker volume create.</p>"""
    driver_opts: NotRequired["aws_sdk_ecs.types.string_map.StringMap"]
    """<p>A map of Docker driver-specific options passed through. This parameter maps to <code>DriverOpts</code> in the docker create-volume command and the <code>xxopt</code> option to docker volume create.</p>"""
    labels: NotRequired["aws_sdk_ecs.types.string_map.StringMap"]
    """<p>Custom metadata to add to your Docker volume. This parameter maps to <code>Labels</code> in the docker container create command and the <code>xxlabel</code> option to docker volume create.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DockerVolumeConfiguration) -> dict:
    out: dict = {}
    if "scope" in value:
        import aws_sdk_ecs.types.scope

        out["scope"] = aws_sdk_ecs.types.scope.serialize_aws_json_1_1(value["scope"])
    if "autoprovision" in value:
        out["autoprovision"] = value["autoprovision"]
    if "driver" in value:
        out["driver"] = value["driver"]
    if "driver_opts" in value:
        import aws_sdk_ecs.types.string_map

        out["driverOpts"] = aws_sdk_ecs.types.string_map.serialize_aws_json_1_1(
            value["driver_opts"]
        )
    if "labels" in value:
        import aws_sdk_ecs.types.string_map

        out["labels"] = aws_sdk_ecs.types.string_map.serialize_aws_json_1_1(
            value["labels"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DockerVolumeConfiguration:
    out: DockerVolumeConfiguration = {}  # type: ignore[typeddict-item]
    if "scope" in data:
        import aws_sdk_ecs.types.scope

        out["scope"] = aws_sdk_ecs.types.scope.deserialize_aws_json_1_1(data["scope"])
    if "autoprovision" in data:
        out["autoprovision"] = data["autoprovision"]
    if "driver" in data:
        out["driver"] = data["driver"]
    if "driverOpts" in data:
        import aws_sdk_ecs.types.string_map

        out["driver_opts"] = aws_sdk_ecs.types.string_map.deserialize_aws_json_1_1(
            data["driverOpts"]
        )
    if "labels" in data:
        import aws_sdk_ecs.types.string_map

        out["labels"] = aws_sdk_ecs.types.string_map.deserialize_aws_json_1_1(
            data["labels"]
        )
    return out
