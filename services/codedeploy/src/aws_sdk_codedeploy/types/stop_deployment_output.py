"""Generated from Smithy shape ``com.amazonaws.codedeploy#StopDeploymentOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.message
    import aws_sdk_codedeploy.types.stop_status


class StopDeploymentOutput(TypedDict):
    status: NotRequired["aws_sdk_codedeploy.types.stop_status.StopStatus"]
    """<p>The status of the stop deployment operation:</p> <ul> <li> <p>Pending: The stop operation is pending.</p> </li> <li> <p>Succeeded: The stop operation was successful.</p> </li> </ul>"""
    status_message: NotRequired["aws_sdk_codedeploy.types.message.Message"]
    """<p>An accompanying status message.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopDeploymentOutput) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_codedeploy.types.stop_status

        out["status"] = aws_sdk_codedeploy.types.stop_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopDeploymentOutput:
    out: StopDeploymentOutput = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_codedeploy.types.stop_status

        out["status"] = aws_sdk_codedeploy.types.stop_status.deserialize_aws_json_1_1(
            data["status"]
        )
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    return out
