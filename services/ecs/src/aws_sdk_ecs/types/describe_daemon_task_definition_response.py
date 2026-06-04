"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeDaemonTaskDefinitionResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.daemon_task_definition


class DescribeDaemonTaskDefinitionResponse(TypedDict):
    daemon_task_definition: NotRequired[
        "aws_sdk_ecs.types.daemon_task_definition.DaemonTaskDefinition"
    ]
    """<p>The full daemon task definition description.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDaemonTaskDefinitionResponse) -> dict:
    out: dict = {}
    if "daemon_task_definition" in value:
        import aws_sdk_ecs.types.daemon_task_definition

        out["daemonTaskDefinition"] = (
            aws_sdk_ecs.types.daemon_task_definition.serialize_aws_json_1_1(
                value["daemon_task_definition"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDaemonTaskDefinitionResponse:
    out: DescribeDaemonTaskDefinitionResponse = {}  # type: ignore[typeddict-item]
    if "daemonTaskDefinition" in data:
        import aws_sdk_ecs.types.daemon_task_definition

        out["daemon_task_definition"] = (
            aws_sdk_ecs.types.daemon_task_definition.deserialize_aws_json_1_1(
                data["daemonTaskDefinition"]
            )
        )
    return out
