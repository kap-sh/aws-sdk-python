"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateVPCConnectionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string
    import capo_quicksight.types.vpc_connection_availability_status
    import capo_quicksight.types.vpc_connection_resource_id_restricted
    import capo_quicksight.types.vpc_connection_resource_status


class CreateVPCConnectionResponse(TypedDict, closed=True):
    arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the VPC connection.</p>"""
    vpc_connection_id: NotRequired[
        "capo_quicksight.types.vpc_connection_resource_id_restricted.VPCConnectionResourceIdRestricted"
    ]
    """<p>The ID for the VPC connection that you're creating. This ID is unique per Amazon Web Services Region for each Amazon Web Services account.</p>"""
    creation_status: NotRequired[
        "capo_quicksight.types.vpc_connection_resource_status.VPCConnectionResourceStatus"
    ]
    """<p>The status of the creation of the VPC connection.</p>"""
    availability_status: NotRequired[
        "capo_quicksight.types.vpc_connection_availability_status.VPCConnectionAvailabilityStatus"
    ]
    """<p>The availability status of the VPC connection.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateVPCConnectionResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "vpc_connection_id" in value:
        out["VPCConnectionId"] = value["vpc_connection_id"]
    if "creation_status" in value:
        import capo_quicksight.types.vpc_connection_resource_status

        out["CreationStatus"] = (
            capo_quicksight.types.vpc_connection_resource_status.serialize_json(
                value["creation_status"]
            )
        )
    if "availability_status" in value:
        import capo_quicksight.types.vpc_connection_availability_status

        out["AvailabilityStatus"] = (
            capo_quicksight.types.vpc_connection_availability_status.serialize_json(
                value["availability_status"]
            )
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> CreateVPCConnectionResponse:
    out: CreateVPCConnectionResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "VPCConnectionId" in data:
        out["vpc_connection_id"] = data["VPCConnectionId"]
    if "CreationStatus" in data:
        import capo_quicksight.types.vpc_connection_resource_status

        out["creation_status"] = (
            capo_quicksight.types.vpc_connection_resource_status.deserialize_json(
                data["CreationStatus"]
            )
        )
    if "AvailabilityStatus" in data:
        import capo_quicksight.types.vpc_connection_availability_status

        out["availability_status"] = (
            capo_quicksight.types.vpc_connection_availability_status.deserialize_json(
                data["AvailabilityStatus"]
            )
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
