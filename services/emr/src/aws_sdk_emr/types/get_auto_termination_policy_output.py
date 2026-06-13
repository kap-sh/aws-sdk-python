"""Generated from Smithy shape ``com.amazonaws.emr#GetAutoTerminationPolicyOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.auto_termination_policy


class GetAutoTerminationPolicyOutput(TypedDict):
    auto_termination_policy: NotRequired[
        "aws_sdk_emr.types.auto_termination_policy.AutoTerminationPolicy"
    ]
    """<p>Specifies the auto-termination policy that is attached to an Amazon EMR cluster. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAutoTerminationPolicyOutput) -> dict:
    out: dict = {}
    if "auto_termination_policy" in value:
        import aws_sdk_emr.types.auto_termination_policy

        out["AutoTerminationPolicy"] = (
            aws_sdk_emr.types.auto_termination_policy.serialize_aws_json_1_1(
                value["auto_termination_policy"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAutoTerminationPolicyOutput:
    out: GetAutoTerminationPolicyOutput = {}  # type: ignore[typeddict-item]
    if "AutoTerminationPolicy" in data:
        import aws_sdk_emr.types.auto_termination_policy

        out["auto_termination_policy"] = (
            aws_sdk_emr.types.auto_termination_policy.deserialize_aws_json_1_1(
                data["AutoTerminationPolicy"]
            )
        )
    return out
