"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceRevisionOverrides``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.runtime_platform_override


class ServiceRevisionOverrides(TypedDict, closed=True):
    runtime_platform: NotRequired[
        "capo_ecs.types.runtime_platform_override.RuntimePlatformOverride"
    ]
    """<p>The runtime platform override that Amazon ECS automatically applies to the service revision. You can't set this value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceRevisionOverrides) -> dict:
    out: dict = {}
    if "runtime_platform" in value:
        import capo_ecs.types.runtime_platform_override

        out["runtimePlatform"] = (
            capo_ecs.types.runtime_platform_override.serialize_aws_json_1_1(
                value["runtime_platform"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceRevisionOverrides:
    out: ServiceRevisionOverrides = {}  # type: ignore[typeddict-item]
    if data.get("runtimePlatform") is not None:
        import capo_ecs.types.runtime_platform_override

        out["runtime_platform"] = (
            capo_ecs.types.runtime_platform_override.deserialize_aws_json_1_1(
                data["runtimePlatform"]
            )
        )
    return out
