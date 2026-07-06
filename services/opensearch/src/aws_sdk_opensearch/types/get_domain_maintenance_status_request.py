"""Generated from Smithy shape ``com.amazonaws.opensearch#GetDomainMaintenanceStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.domain_name
    import aws_sdk_opensearch.types.request_id


class GetDomainMaintenanceStatusRequest(TypedDict, closed=True):
    domain_name: "aws_sdk_opensearch.types.domain_name.DomainName"
    """<p>The name of the domain.</p>"""
    maintenance_id: "aws_sdk_opensearch.types.request_id.RequestId"
    """<p>The request ID of the maintenance action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDomainMaintenanceStatusRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDomainMaintenanceStatusRequest:
    out: GetDomainMaintenanceStatusRequest = {}  # type: ignore[typeddict-item]
    return out
