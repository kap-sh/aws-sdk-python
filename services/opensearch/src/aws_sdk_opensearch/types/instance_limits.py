"""Generated from Smithy shape ``com.amazonaws.opensearch#InstanceLimits``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.instance_count_limits


class InstanceLimits(TypedDict, closed=True):
    instance_count_limits: NotRequired[
        "aws_sdk_opensearch.types.instance_count_limits.InstanceCountLimits"
    ]
    """<p>Limits on the number of instances that can be created for a given instance type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InstanceLimits) -> dict:
    out: dict = {}
    if "instance_count_limits" in value:
        import aws_sdk_opensearch.types.instance_count_limits

        out["InstanceCountLimits"] = (
            aws_sdk_opensearch.types.instance_count_limits.serialize_json(
                value["instance_count_limits"]
            )
        )
    return out


def deserialize_json(data: dict) -> InstanceLimits:
    out: InstanceLimits = {}  # type: ignore[typeddict-item]
    if "InstanceCountLimits" in data:
        import aws_sdk_opensearch.types.instance_count_limits

        out["instance_count_limits"] = (
            aws_sdk_opensearch.types.instance_count_limits.deserialize_json(
                data["InstanceCountLimits"]
            )
        )
    return out
