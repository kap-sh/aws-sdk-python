"""Generated from Smithy shape ``com.amazonaws.ssm#CancelCommandRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.command_id
    import aws_sdk_ssm.types.instance_id_list


class CancelCommandRequest(TypedDict):
    command_id: "aws_sdk_ssm.types.command_id.CommandId"
    """<p>The ID of the command you want to cancel.</p>"""
    instance_ids: NotRequired["aws_sdk_ssm.types.instance_id_list.InstanceIdList"]
    """<p>(Optional) A list of managed node IDs on which you want to cancel the command. If not provided, the command is canceled on every node on which it was requested.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CancelCommandRequest) -> dict:
    out: dict = {}
    out["CommandId"] = value["command_id"]
    if "instance_ids" in value:
        import aws_sdk_ssm.types.instance_id_list

        out["InstanceIds"] = aws_sdk_ssm.types.instance_id_list.serialize_aws_json_1_1(
            value["instance_ids"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CancelCommandRequest:
    out: CancelCommandRequest = {}  # type: ignore[typeddict-item]
    if "CommandId" in data:
        out["command_id"] = data["CommandId"]
    else:
        raise DeserializationError("CancelCommandRequest.command_id required")
    if "InstanceIds" in data:
        import aws_sdk_ssm.types.instance_id_list

        out["instance_ids"] = (
            aws_sdk_ssm.types.instance_id_list.deserialize_aws_json_1_1(
                data["InstanceIds"]
            )
        )
    return out
