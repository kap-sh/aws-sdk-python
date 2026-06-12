"""Generated from Smithy shape ``com.amazonaws.vpclattice#DeleteServiceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.service_arn
    import aws_sdk_vpc_lattice.types.service_id
    import aws_sdk_vpc_lattice.types.service_name
    import aws_sdk_vpc_lattice.types.service_status


class DeleteServiceResponse(TypedDict):
    id: NotRequired["aws_sdk_vpc_lattice.types.service_id.ServiceId"]
    """<p>The ID of the service.</p>"""
    arn: NotRequired["aws_sdk_vpc_lattice.types.service_arn.ServiceArn"]
    """<p>The Amazon Resource Name (ARN) of the service.</p>"""
    name: NotRequired["aws_sdk_vpc_lattice.types.service_name.ServiceName"]
    """<p>The name of the service.</p>"""
    status: NotRequired["aws_sdk_vpc_lattice.types.service_status.ServiceStatus"]
    """<p>The status. You can retry the operation if the status is <code>DELETE_FAILED</code>. However, if you retry it while the status is <code>DELETE_IN_PROGRESS</code>, the status doesn't change.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteServiceResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> DeleteServiceResponse:
    out: DeleteServiceResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "name" in data:
        out["name"] = data["name"]
    if "status" in data:
        out["status"] = data["status"]
    return out
