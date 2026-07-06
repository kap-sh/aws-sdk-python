"""Generated from Smithy shape ``com.amazonaws.codedeploy#GetOnPremisesInstanceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.instance_info


class GetOnPremisesInstanceOutput(TypedDict, closed=True):
    instance_info: NotRequired["aws_sdk_codedeploy.types.instance_info.InstanceInfo"]
    """<p> Information about the on-premises instance. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetOnPremisesInstanceOutput) -> dict:
    out: dict = {}
    if "instance_info" in value:
        import aws_sdk_codedeploy.types.instance_info

        out["instanceInfo"] = (
            aws_sdk_codedeploy.types.instance_info.serialize_aws_json_1_1(
                value["instance_info"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetOnPremisesInstanceOutput:
    out: GetOnPremisesInstanceOutput = {}  # type: ignore[typeddict-item]
    if "instanceInfo" in data:
        import aws_sdk_codedeploy.types.instance_info

        out["instance_info"] = (
            aws_sdk_codedeploy.types.instance_info.deserialize_aws_json_1_1(
                data["instanceInfo"]
            )
        )
    return out
