"""Generated from Smithy shape ``com.amazonaws.ssm#UpdateAssociationStatusRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.association_status
    import aws_sdk_ssm.types.document_arn
    import aws_sdk_ssm.types.instance_id


class UpdateAssociationStatusRequest(TypedDict):
    name: "aws_sdk_ssm.types.document_arn.DocumentARN"
    """<p>The name of the SSM document.</p>"""
    instance_id: "aws_sdk_ssm.types.instance_id.InstanceId"
    """<p>The managed node ID.</p>"""
    association_status: "aws_sdk_ssm.types.association_status.AssociationStatus"
    """<p>The association status.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateAssociationStatusRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["InstanceId"] = value["instance_id"]
    import aws_sdk_ssm.types.association_status

    out["AssociationStatus"] = (
        aws_sdk_ssm.types.association_status.serialize_aws_json_1_1(
            value["association_status"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateAssociationStatusRequest:
    out: UpdateAssociationStatusRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateAssociationStatusRequest.name required")
    if "InstanceId" in data:
        out["instance_id"] = data["InstanceId"]
    else:
        raise DeserializationError(
            "UpdateAssociationStatusRequest.instance_id required"
        )
    if "AssociationStatus" in data:
        import aws_sdk_ssm.types.association_status

        out["association_status"] = (
            aws_sdk_ssm.types.association_status.deserialize_aws_json_1_1(
                data["AssociationStatus"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateAssociationStatusRequest.association_status required"
        )
    return out
