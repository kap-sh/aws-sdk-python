"""Generated from Smithy shape ``com.amazonaws.codedeploy#GetOnPremisesInstanceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codedeploy.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.instance_name


class GetOnPremisesInstanceInput(TypedDict, closed=True):
    instance_name: "aws_sdk_codedeploy.types.instance_name.InstanceName"
    """<p> The name of the on-premises instance about which to get information. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetOnPremisesInstanceInput) -> dict:
    out: dict = {}
    out["instanceName"] = value["instance_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetOnPremisesInstanceInput:
    out: GetOnPremisesInstanceInput = {}  # type: ignore[typeddict-item]
    if "instanceName" in data:
        out["instance_name"] = data["instanceName"]
    else:
        raise DeserializationError("GetOnPremisesInstanceInput.instance_name required")
    return out
