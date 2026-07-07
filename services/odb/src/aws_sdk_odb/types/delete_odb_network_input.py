"""Generated from Smithy shape ``com.amazonaws.odb#DeleteOdbNetworkInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_odb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_odb.types.resource_id_or_arn


class DeleteOdbNetworkInput(TypedDict, closed=True):
    odb_network_id: "aws_sdk_odb.types.resource_id_or_arn.ResourceIdOrArn"
    """<p>The unique identifier of the ODB network to delete.</p>"""
    delete_associated_resources: "bool"
    """<p>Specifies whether to delete associated OCI networking resources along with the ODB network.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteOdbNetworkInput) -> dict:
    out: dict = {}
    out["deleteAssociatedResources"] = value["delete_associated_resources"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteOdbNetworkInput:
    out: DeleteOdbNetworkInput = {}  # type: ignore[typeddict-item]
    if "deleteAssociatedResources" in data:
        out["delete_associated_resources"] = data["deleteAssociatedResources"]
    else:
        raise DeserializationError(
            "DeleteOdbNetworkInput.delete_associated_resources required"
        )
    return out
