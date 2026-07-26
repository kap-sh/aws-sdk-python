"""Generated from Smithy shape ``com.amazonaws.emr#GetAutoTerminationPolicyOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.auto_termination_policy


class GetAutoTerminationPolicyOutput(TypedDict, closed=True):
    auto_termination_policy: NotRequired[
        "capo_emr.types.auto_termination_policy.AutoTerminationPolicy"
    ]
    """<p>Specifies the auto-termination policy that is attached to an Amazon EMR cluster. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAutoTerminationPolicyOutput) -> dict:
    out: dict = {}
    if "auto_termination_policy" in value:
        import capo_emr.types.auto_termination_policy

        out["AutoTerminationPolicy"] = (
            capo_emr.types.auto_termination_policy.serialize_aws_json_1_1(
                value["auto_termination_policy"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAutoTerminationPolicyOutput:
    out: GetAutoTerminationPolicyOutput = {}  # type: ignore[typeddict-item]
    if "AutoTerminationPolicy" in data:
        import capo_emr.types.auto_termination_policy

        out["auto_termination_policy"] = (
            capo_emr.types.auto_termination_policy.deserialize_aws_json_1_1(
                data["AutoTerminationPolicy"]
            )
        )
    return out
