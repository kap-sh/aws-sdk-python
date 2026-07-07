"""Generated from Smithy shape ``com.amazonaws.quicksight#DeleteVPCConnectionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string
    import aws_sdk_quicksight.types.vpc_connection_availability_status
    import aws_sdk_quicksight.types.vpc_connection_resource_id_unrestricted
    import aws_sdk_quicksight.types.vpc_connection_resource_status


class DeleteVPCConnectionResponse(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the deleted VPC connection.</p>"""
    vpc_connection_id: NotRequired[
        "aws_sdk_quicksight.types.vpc_connection_resource_id_unrestricted.VPCConnectionResourceIdUnrestricted"
    ]
    """<p>The ID of the VPC connection that you're creating. This ID is a unique identifier for each Amazon Web Services Region in an Amazon Web Services account.</p>"""
    deletion_status: NotRequired[
        "aws_sdk_quicksight.types.vpc_connection_resource_status.VPCConnectionResourceStatus"
    ]
    """<p>The deletion status of the VPC connection.</p>"""
    availability_status: NotRequired[
        "aws_sdk_quicksight.types.vpc_connection_availability_status.VPCConnectionAvailabilityStatus"
    ]
    """<p>The availability status of the VPC connection.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteVPCConnectionResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "vpc_connection_id" in value:
        out["VPCConnectionId"] = value["vpc_connection_id"]
    if "deletion_status" in value:
        import aws_sdk_quicksight.types.vpc_connection_resource_status

        out["DeletionStatus"] = (
            aws_sdk_quicksight.types.vpc_connection_resource_status.serialize_json(
                value["deletion_status"]
            )
        )
    if "availability_status" in value:
        import aws_sdk_quicksight.types.vpc_connection_availability_status

        out["AvailabilityStatus"] = (
            aws_sdk_quicksight.types.vpc_connection_availability_status.serialize_json(
                value["availability_status"]
            )
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DeleteVPCConnectionResponse:
    out: DeleteVPCConnectionResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "VPCConnectionId" in data:
        out["vpc_connection_id"] = data["VPCConnectionId"]
    if "DeletionStatus" in data:
        import aws_sdk_quicksight.types.vpc_connection_resource_status

        out["deletion_status"] = (
            aws_sdk_quicksight.types.vpc_connection_resource_status.deserialize_json(
                data["DeletionStatus"]
            )
        )
    if "AvailabilityStatus" in data:
        import aws_sdk_quicksight.types.vpc_connection_availability_status

        out["availability_status"] = (
            aws_sdk_quicksight.types.vpc_connection_availability_status.deserialize_json(
                data["AvailabilityStatus"]
            )
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
