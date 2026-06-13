"""Generated from Smithy shape ``com.amazonaws.odb#DeleteOdbPeeringConnectionInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_odb.types.resource_id_or_arn


class DeleteOdbPeeringConnectionInput(TypedDict):
    odb_peering_connection_id: "aws_sdk_odb.types.resource_id_or_arn.ResourceIdOrArn"
    """<p>The unique identifier of the ODB peering connection to delete.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteOdbPeeringConnectionInput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteOdbPeeringConnectionInput:
    out: DeleteOdbPeeringConnectionInput = {}  # type: ignore[typeddict-item]
    return out
