"""Generated from Smithy shape ``com.amazonaws.lambda#InstanceRequirements``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.architectures_list
    import capo_lambda.types.instance_type_set


class InstanceRequirements(TypedDict, closed=True):
    architectures: NotRequired["capo_lambda.types.architectures_list.ArchitecturesList"]
    """<p>A list of supported CPU architectures for compute instances. Valid values include <code>x86_64</code> and <code>arm64</code>.</p>"""
    allowed_instance_types: NotRequired[
        "capo_lambda.types.instance_type_set.InstanceTypeSet"
    ]
    """<p>A list of EC2 instance types that the capacity provider is allowed to use. If not specified, all compatible instance types are allowed.</p>"""
    excluded_instance_types: NotRequired[
        "capo_lambda.types.instance_type_set.InstanceTypeSet"
    ]
    """<p>A list of EC2 instance types that the capacity provider should not use, even if they meet other requirements.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InstanceRequirements) -> dict:
    out: dict = {}
    if "architectures" in value:
        import capo_lambda.types.architectures_list

        out["Architectures"] = capo_lambda.types.architectures_list.serialize_json(
            value["architectures"]
        )
    if "allowed_instance_types" in value:
        import capo_lambda.types.instance_type_set

        out["AllowedInstanceTypes"] = (
            capo_lambda.types.instance_type_set.serialize_json(
                value["allowed_instance_types"]
            )
        )
    if "excluded_instance_types" in value:
        import capo_lambda.types.instance_type_set

        out["ExcludedInstanceTypes"] = (
            capo_lambda.types.instance_type_set.serialize_json(
                value["excluded_instance_types"]
            )
        )
    return out


def deserialize_json(data: dict) -> InstanceRequirements:
    out: InstanceRequirements = {}  # type: ignore[typeddict-item]
    if "Architectures" in data:
        import capo_lambda.types.architectures_list

        out["architectures"] = capo_lambda.types.architectures_list.deserialize_json(
            data["Architectures"]
        )
    if "AllowedInstanceTypes" in data:
        import capo_lambda.types.instance_type_set

        out["allowed_instance_types"] = (
            capo_lambda.types.instance_type_set.deserialize_json(
                data["AllowedInstanceTypes"]
            )
        )
    if "ExcludedInstanceTypes" in data:
        import capo_lambda.types.instance_type_set

        out["excluded_instance_types"] = (
            capo_lambda.types.instance_type_set.deserialize_json(
                data["ExcludedInstanceTypes"]
            )
        )
    return out
