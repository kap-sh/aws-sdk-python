"""Generated from Smithy shape ``com.amazonaws.efs#LifecycleConfigurationDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_efs.types.lifecycle_policies


class LifecycleConfigurationDescription(TypedDict):
    lifecycle_policies: NotRequired[
        "aws_sdk_efs.types.lifecycle_policies.LifecyclePolicies"
    ]
    """<p>An array of lifecycle management policies. EFS supports a maximum of one policy per file system.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LifecycleConfigurationDescription) -> dict:
    out: dict = {}
    if "lifecycle_policies" in value:
        import aws_sdk_efs.types.lifecycle_policies

        out["LifecyclePolicies"] = aws_sdk_efs.types.lifecycle_policies.serialize_json(
            value["lifecycle_policies"]
        )
    return out


def deserialize_json(data: dict) -> LifecycleConfigurationDescription:
    out: LifecycleConfigurationDescription = {}  # type: ignore[typeddict-item]
    if "LifecyclePolicies" in data:
        import aws_sdk_efs.types.lifecycle_policies

        out["lifecycle_policies"] = (
            aws_sdk_efs.types.lifecycle_policies.deserialize_json(
                data["LifecyclePolicies"]
            )
        )
    return out
