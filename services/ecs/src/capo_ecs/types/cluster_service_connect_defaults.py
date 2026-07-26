"""Generated from Smithy shape ``com.amazonaws.ecs#ClusterServiceConnectDefaults``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.string


class ClusterServiceConnectDefaults(TypedDict, closed=True):
    namespace: NotRequired["capo_ecs.types.string.String"]
    """<p>The namespace name or full Amazon Resource Name (ARN) of the Cloud Map namespace. When you create a service and don't specify a Service Connect configuration, this namespace is used.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterServiceConnectDefaults) -> dict:
    out: dict = {}
    if "namespace" in value:
        out["namespace"] = value["namespace"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterServiceConnectDefaults:
    out: ClusterServiceConnectDefaults = {}  # type: ignore[typeddict-item]
    if "namespace" in data:
        out["namespace"] = data["namespace"]
    return out
