"""Generated from Smithy shape ``com.amazonaws.lightsail#CreateCloudFormationStackRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.instance_entry_list


class CreateCloudFormationStackRequest(TypedDict):
    instances: "aws_sdk_lightsail.types.instance_entry_list.InstanceEntryList"
    """<p>An array of parameters that will be used to create the new Amazon EC2 instance. You can only pass one instance entry at a time in this array. You will get an invalid parameter error if you pass more than one instance entry in this array.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateCloudFormationStackRequest) -> dict:
    out: dict = {}
    import aws_sdk_lightsail.types.instance_entry_list

    out["instances"] = (
        aws_sdk_lightsail.types.instance_entry_list.serialize_aws_json_1_1(
            value["instances"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateCloudFormationStackRequest:
    out: CreateCloudFormationStackRequest = {}  # type: ignore[typeddict-item]
    if "instances" in data:
        import aws_sdk_lightsail.types.instance_entry_list

        out["instances"] = (
            aws_sdk_lightsail.types.instance_entry_list.deserialize_aws_json_1_1(
                data["instances"]
            )
        )
    else:
        raise DeserializationError(
            "CreateCloudFormationStackRequest.instances required"
        )
    return out
