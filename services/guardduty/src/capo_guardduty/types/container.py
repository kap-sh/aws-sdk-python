"""Generated from Smithy shape ``com.amazonaws.guardduty#Container``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.security_context
    import capo_guardduty.types.string
    import capo_guardduty.types.volume_mounts


class Container(TypedDict, closed=True):
    container_runtime: NotRequired["capo_guardduty.types.string.String"]
    """<p>The container runtime (such as, Docker or containerd) used to run the container.</p>"""
    id: NotRequired["capo_guardduty.types.string.String"]
    """<p>Container ID.</p>"""
    name: NotRequired["capo_guardduty.types.string.String"]
    """<p>Container name.</p>"""
    image: NotRequired["capo_guardduty.types.string.String"]
    """<p>Container image.</p>"""
    image_prefix: NotRequired["capo_guardduty.types.string.String"]
    """<p>Part of the image name before the last slash. For example, imagePrefix for public.ecr.aws/amazonlinux/amazonlinux:latest would be public.ecr.aws/amazonlinux. If the image name is relative and does not have a slash, this field is empty.</p>"""
    volume_mounts: NotRequired["capo_guardduty.types.volume_mounts.VolumeMounts"]
    """<p>Container volume mounts.</p>"""
    security_context: NotRequired[
        "capo_guardduty.types.security_context.SecurityContext"
    ]
    """<p>Container security context.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Container) -> dict:
    out: dict = {}
    if "container_runtime" in value:
        out["containerRuntime"] = value["container_runtime"]
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "image" in value:
        out["image"] = value["image"]
    if "image_prefix" in value:
        out["imagePrefix"] = value["image_prefix"]
    if "volume_mounts" in value:
        import capo_guardduty.types.volume_mounts

        out["volumeMounts"] = capo_guardduty.types.volume_mounts.serialize_json(
            value["volume_mounts"]
        )
    if "security_context" in value:
        import capo_guardduty.types.security_context

        out["securityContext"] = capo_guardduty.types.security_context.serialize_json(
            value["security_context"]
        )
    return out


def deserialize_json(data: dict) -> Container:
    out: Container = {}  # type: ignore[typeddict-item]
    if "containerRuntime" in data:
        out["container_runtime"] = data["containerRuntime"]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "image" in data:
        out["image"] = data["image"]
    if "imagePrefix" in data:
        out["image_prefix"] = data["imagePrefix"]
    if "volumeMounts" in data:
        import capo_guardduty.types.volume_mounts

        out["volume_mounts"] = capo_guardduty.types.volume_mounts.deserialize_json(
            data["volumeMounts"]
        )
    if "securityContext" in data:
        import capo_guardduty.types.security_context

        out["security_context"] = (
            capo_guardduty.types.security_context.deserialize_json(
                data["securityContext"]
            )
        )
    return out
