"""Generated from Smithy shape ``com.amazonaws.datazone#UpdateDomainUnitOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.created_at
    import aws_sdk_datazone.types.created_by
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.domain_unit_description
    import aws_sdk_datazone.types.domain_unit_id
    import aws_sdk_datazone.types.domain_unit_name
    import aws_sdk_datazone.types.domain_unit_owners
    import aws_sdk_datazone.types.updated_at
    import aws_sdk_datazone.types.updated_by


class UpdateDomainUnitOutput(TypedDict):
    id: "aws_sdk_datazone.types.domain_unit_id.DomainUnitId"
    """<p>The ID of the domain unit that you want to update.</p>"""
    domain_id: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where you want to update the domain unit.</p>"""
    name: "aws_sdk_datazone.types.domain_unit_name.DomainUnitName"
    """<p>The name of the domain unit that you want to update.</p>"""
    owners: "aws_sdk_datazone.types.domain_unit_owners.DomainUnitOwners"
    """<p>The owners of the domain unit that you want to update.</p>"""
    description: NotRequired[
        "aws_sdk_datazone.types.domain_unit_description.DomainUnitDescription"
    ]
    """<p>The description of the domain unit that you want to update.</p>"""
    parent_domain_unit_id: NotRequired[
        "aws_sdk_datazone.types.domain_unit_id.DomainUnitId"
    ]
    """<p>The ID of the parent domain unit.</p>"""
    created_at: NotRequired["aws_sdk_datazone.types.created_at.CreatedAt"]
    """<p>The time stamp at which the domain unit that you want to update was created.</p>"""
    last_updated_at: NotRequired["aws_sdk_datazone.types.updated_at.UpdatedAt"]
    """<p>The timestamp at which the domain unit was last updated.</p>"""
    created_by: NotRequired["aws_sdk_datazone.types.created_by.CreatedBy"]
    """<p>The user who created the domain unit that you want to update.</p>"""
    last_updated_by: NotRequired["aws_sdk_datazone.types.updated_by.UpdatedBy"]
    """<p>The user who last updated the domain unit.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDomainUnitOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["domainId"] = value["domain_id"]
    out["name"] = value["name"]
    import aws_sdk_datazone.types.domain_unit_owners

    out["owners"] = aws_sdk_datazone.types.domain_unit_owners.serialize_json(
        value["owners"]
    )
    if "description" in value:
        out["description"] = value["description"]
    if "parent_domain_unit_id" in value:
        out["parentDomainUnitId"] = value["parent_domain_unit_id"]
    if "created_at" in value:
        import aws_sdk_datazone.types.created_at

        out["createdAt"] = aws_sdk_datazone.types.created_at.serialize_json(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import aws_sdk_datazone.types.updated_at

        out["lastUpdatedAt"] = aws_sdk_datazone.types.updated_at.serialize_json(
            value["last_updated_at"]
        )
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    if "last_updated_by" in value:
        out["lastUpdatedBy"] = value["last_updated_by"]
    return out


def deserialize_json(data: dict) -> UpdateDomainUnitOutput:
    out: UpdateDomainUnitOutput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("UpdateDomainUnitOutput.id required")
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("UpdateDomainUnitOutput.domain_id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdateDomainUnitOutput.name required")
    if "owners" in data:
        import aws_sdk_datazone.types.domain_unit_owners

        out["owners"] = aws_sdk_datazone.types.domain_unit_owners.deserialize_json(
            data["owners"]
        )
    else:
        raise DeserializationError("UpdateDomainUnitOutput.owners required")
    if "description" in data:
        out["description"] = data["description"]
    if "parentDomainUnitId" in data:
        out["parent_domain_unit_id"] = data["parentDomainUnitId"]
    if "createdAt" in data:
        import aws_sdk_datazone.types.created_at

        out["created_at"] = aws_sdk_datazone.types.created_at.deserialize_json(
            data["createdAt"]
        )
    if "lastUpdatedAt" in data:
        import aws_sdk_datazone.types.updated_at

        out["last_updated_at"] = aws_sdk_datazone.types.updated_at.deserialize_json(
            data["lastUpdatedAt"]
        )
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    if "lastUpdatedBy" in data:
        out["last_updated_by"] = data["lastUpdatedBy"]
    return out
