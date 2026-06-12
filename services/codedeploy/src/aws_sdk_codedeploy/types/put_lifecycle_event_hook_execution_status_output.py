"""Generated from Smithy shape ``com.amazonaws.codedeploy#PutLifecycleEventHookExecutionStatusOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.lifecycle_event_hook_execution_id


class PutLifecycleEventHookExecutionStatusOutput(TypedDict):
    lifecycle_event_hook_execution_id: NotRequired[
        "aws_sdk_codedeploy.types.lifecycle_event_hook_execution_id.LifecycleEventHookExecutionId"
    ]
    """<p>The execution ID of the lifecycle event hook. A hook is specified in the <code>hooks</code> section of the deployment's AppSpec file.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutLifecycleEventHookExecutionStatusOutput) -> dict:
    out: dict = {}
    if "lifecycle_event_hook_execution_id" in value:
        out["lifecycleEventHookExecutionId"] = value[
            "lifecycle_event_hook_execution_id"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutLifecycleEventHookExecutionStatusOutput:
    out: PutLifecycleEventHookExecutionStatusOutput = {}  # type: ignore[typeddict-item]
    if "lifecycleEventHookExecutionId" in data:
        out["lifecycle_event_hook_execution_id"] = data["lifecycleEventHookExecutionId"]
    return out
