"""Generated from Smithy shape ``com.amazonaws.eventbridge#RunCommandTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_eventbridge.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.run_command_target_key
    import aws_sdk_eventbridge.types.run_command_target_values


class RunCommandTarget(TypedDict, closed=True):
    key: "aws_sdk_eventbridge.types.run_command_target_key.RunCommandTargetKey"
    """<p>Can be either <code>tag:</code> <i>tag-key</i> or <code>InstanceIds</code>.</p>"""
    values: "aws_sdk_eventbridge.types.run_command_target_values.RunCommandTargetValues"
    """<p>If <code>Key</code> is <code>tag:</code> <i>tag-key</i>, <code>Values</code> is a list of tag values. If <code>Key</code> is <code>InstanceIds</code>, <code>Values</code> is a list of Amazon EC2 instance IDs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RunCommandTarget) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    import aws_sdk_eventbridge.types.run_command_target_values

    out["Values"] = (
        aws_sdk_eventbridge.types.run_command_target_values.serialize_aws_json_1_1(
            value["values"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RunCommandTarget:
    out: RunCommandTarget = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    else:
        raise DeserializationError("RunCommandTarget.key required")
    if "Values" in data:
        import aws_sdk_eventbridge.types.run_command_target_values

        out["values"] = (
            aws_sdk_eventbridge.types.run_command_target_values.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    else:
        raise DeserializationError("RunCommandTarget.values required")
    return out
