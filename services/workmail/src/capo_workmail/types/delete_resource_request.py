"""Generated from Smithy shape ``com.amazonaws.workmail#DeleteResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workmail.types.entity_identifier
    import capo_workmail.types.organization_id


class DeleteResourceRequest(TypedDict, closed=True):
    organization_id: "capo_workmail.types.organization_id.OrganizationId"
    """<p>The identifier associated with the organization from which the resource is deleted.</p>"""
    resource_id: "capo_workmail.types.entity_identifier.EntityIdentifier"
    """<p>The identifier of the resource to be deleted.</p> <p>The identifier can accept <i>ResourceId</i>, or <i>Resourcename</i>. The following identity formats are available:</p> <ul> <li> <p>Resource ID: r-0123456789a0123456789b0123456789</p> </li> <li> <p>Resource name: resource</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteResourceRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    out["ResourceId"] = value["resource_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteResourceRequest:
    out: DeleteResourceRequest = {}  # type: ignore[typeddict-item]
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    else:
        raise DeserializationError("DeleteResourceRequest.organization_id required")
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    else:
        raise DeserializationError("DeleteResourceRequest.resource_id required")
    return out
