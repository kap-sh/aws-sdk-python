"""Generated from Smithy shape ``com.amazonaws.ecs#GetTaskProtectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.string_list


class GetTaskProtectionRequest(TypedDict, closed=True):
    cluster: "aws_sdk_ecs.types.string.String"
    """<p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service that the task sets exist in.</p>"""
    tasks: NotRequired["aws_sdk_ecs.types.string_list.StringList"]
    """<p>A list of up to 100 task IDs or full ARN entries.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetTaskProtectionRequest) -> dict:
    out: dict = {}
    out["cluster"] = value["cluster"]
    if "tasks" in value:
        import aws_sdk_ecs.types.string_list

        out["tasks"] = aws_sdk_ecs.types.string_list.serialize_aws_json_1_1(
            value["tasks"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetTaskProtectionRequest:
    out: GetTaskProtectionRequest = {}  # type: ignore[typeddict-item]
    if "cluster" in data:
        out["cluster"] = data["cluster"]
    else:
        raise DeserializationError("GetTaskProtectionRequest.cluster required")
    if "tasks" in data:
        import aws_sdk_ecs.types.string_list

        out["tasks"] = aws_sdk_ecs.types.string_list.deserialize_aws_json_1_1(
            data["tasks"]
        )
    return out
