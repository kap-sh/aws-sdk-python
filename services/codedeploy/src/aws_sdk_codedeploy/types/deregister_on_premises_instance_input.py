"""Generated from Smithy shape ``com.amazonaws.codedeploy#DeregisterOnPremisesInstanceInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codedeploy.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.instance_name


class DeregisterOnPremisesInstanceInput(TypedDict):
    instance_name: "aws_sdk_codedeploy.types.instance_name.InstanceName"
    """<p>The name of the on-premises instance to deregister.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeregisterOnPremisesInstanceInput) -> dict:
    out: dict = {}
    out["instanceName"] = value["instance_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeregisterOnPremisesInstanceInput:
    out: DeregisterOnPremisesInstanceInput = {}  # type: ignore[typeddict-item]
    if "instanceName" in data:
        out["instance_name"] = data["instanceName"]
    else:
        raise DeserializationError(
            "DeregisterOnPremisesInstanceInput.instance_name required"
        )
    return out
