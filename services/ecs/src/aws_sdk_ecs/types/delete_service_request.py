"""Generated from Smithy shape ``com.amazonaws.ecs#DeleteServiceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boxed_boolean
    import aws_sdk_ecs.types.string


class DeleteServiceRequest(TypedDict):
    cluster: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service to delete. If you do not specify a cluster, the default cluster is assumed.</p>"""
    service: "aws_sdk_ecs.types.string.String"
    """<p>The name of the service to delete.</p>"""
    force: NotRequired["aws_sdk_ecs.types.boxed_boolean.BoxedBoolean"]
    """<p>If <code>true</code>, allows you to delete a service even if it wasn't scaled down to zero tasks. It's only necessary to use this if the service uses the <code>REPLICA</code> scheduling strategy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteServiceRequest) -> dict:
    out: dict = {}
    if "cluster" in value:
        out["cluster"] = value["cluster"]
    out["service"] = value["service"]
    if "force" in value:
        out["force"] = value["force"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteServiceRequest:
    out: DeleteServiceRequest = {}  # type: ignore[typeddict-item]
    if "cluster" in data:
        out["cluster"] = data["cluster"]
    if "service" in data:
        out["service"] = data["service"]
    else:
        raise DeserializationError("DeleteServiceRequest.service required")
    if "force" in data:
        out["force"] = data["force"]
    return out
