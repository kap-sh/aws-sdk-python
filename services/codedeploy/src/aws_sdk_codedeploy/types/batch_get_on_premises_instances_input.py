"""Generated from Smithy shape ``com.amazonaws.codedeploy#BatchGetOnPremisesInstancesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codedeploy.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.instance_name_list


class BatchGetOnPremisesInstancesInput(TypedDict, closed=True):
    instance_names: "aws_sdk_codedeploy.types.instance_name_list.InstanceNameList"
    """<p>The names of the on-premises instances about which to get information. The maximum number of instance names you can specify is 25.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetOnPremisesInstancesInput) -> dict:
    out: dict = {}
    import aws_sdk_codedeploy.types.instance_name_list

    out["instanceNames"] = (
        aws_sdk_codedeploy.types.instance_name_list.serialize_aws_json_1_1(
            value["instance_names"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetOnPremisesInstancesInput:
    out: BatchGetOnPremisesInstancesInput = {}  # type: ignore[typeddict-item]
    if "instanceNames" in data:
        import aws_sdk_codedeploy.types.instance_name_list

        out["instance_names"] = (
            aws_sdk_codedeploy.types.instance_name_list.deserialize_aws_json_1_1(
                data["instanceNames"]
            )
        )
    else:
        raise DeserializationError(
            "BatchGetOnPremisesInstancesInput.instance_names required"
        )
    return out
