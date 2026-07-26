"""Generated from Smithy shape ``com.amazonaws.codedeploy#GetDeploymentInstanceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.instance_summary


class GetDeploymentInstanceOutput(TypedDict, closed=True):
    instance_summary: NotRequired[
        "capo_codedeploy.types.instance_summary.InstanceSummary"
    ]
    """<p> Information about the instance. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDeploymentInstanceOutput) -> dict:
    out: dict = {}
    if "instance_summary" in value:
        import capo_codedeploy.types.instance_summary

        out["instanceSummary"] = (
            capo_codedeploy.types.instance_summary.serialize_aws_json_1_1(
                value["instance_summary"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDeploymentInstanceOutput:
    out: GetDeploymentInstanceOutput = {}  # type: ignore[typeddict-item]
    if "instanceSummary" in data:
        import capo_codedeploy.types.instance_summary

        out["instance_summary"] = (
            capo_codedeploy.types.instance_summary.deserialize_aws_json_1_1(
                data["instanceSummary"]
            )
        )
    return out
