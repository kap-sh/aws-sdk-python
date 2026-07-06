"""Generated from Smithy shape ``com.amazonaws.datazone#CreateDomainUnitOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.created_at
    import aws_sdk_datazone.types.created_by
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.domain_unit_description
    import aws_sdk_datazone.types.domain_unit_id
    import aws_sdk_datazone.types.domain_unit_ids
    import aws_sdk_datazone.types.domain_unit_name
    import aws_sdk_datazone.types.domain_unit_owners


class CreateDomainUnitOutput(TypedDict, closed=True):
    id: "aws_sdk_datazone.types.domain_unit_id.DomainUnitId"
    """<p>The ID of the domain unit.</p>"""
    domain_id: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where the domain unit was created.</p>"""
    name: "aws_sdk_datazone.types.domain_unit_name.DomainUnitName"
    """<p>The name of the domain unit.</p>"""
    parent_domain_unit_id: NotRequired[
        "aws_sdk_datazone.types.domain_unit_id.DomainUnitId"
    ]
    """<p>The ID of the parent domain unit.</p>"""
    description: NotRequired[
        "aws_sdk_datazone.types.domain_unit_description.DomainUnitDescription"
    ]
    """<p>The description of the domain unit.</p>"""
    owners: "aws_sdk_datazone.types.domain_unit_owners.DomainUnitOwners"
    """<p>The owners of the domain unit.</p>"""
    ancestor_domain_unit_ids: "aws_sdk_datazone.types.domain_unit_ids.DomainUnitIds"
    """<p>The IDs of the ancestor domain units.</p>"""
    created_at: NotRequired["aws_sdk_datazone.types.created_at.CreatedAt"]
    """<p>The timestamp at which the domain unit was created.</p>"""
    created_by: NotRequired["aws_sdk_datazone.types.created_by.CreatedBy"]
    """<p>The user who created the domain unit.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDomainUnitOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["domainId"] = value["domain_id"]
    out["name"] = value["name"]
    if "parent_domain_unit_id" in value:
        out["parentDomainUnitId"] = value["parent_domain_unit_id"]
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_datazone.types.domain_unit_owners

    out["owners"] = aws_sdk_datazone.types.domain_unit_owners.serialize_json(
        value["owners"]
    )
    import aws_sdk_datazone.types.domain_unit_ids

    out["ancestorDomainUnitIds"] = (
        aws_sdk_datazone.types.domain_unit_ids.serialize_json(
            value["ancestor_domain_unit_ids"]
        )
    )
    if "created_at" in value:
        import aws_sdk_datazone.types.created_at

        out["createdAt"] = aws_sdk_datazone.types.created_at.serialize_json(
            value["created_at"]
        )
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    return out


def deserialize_json(data: dict) -> CreateDomainUnitOutput:
    out: CreateDomainUnitOutput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("CreateDomainUnitOutput.id required")
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("CreateDomainUnitOutput.domain_id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateDomainUnitOutput.name required")
    if "parentDomainUnitId" in data:
        out["parent_domain_unit_id"] = data["parentDomainUnitId"]
    if "description" in data:
        out["description"] = data["description"]
    if "owners" in data:
        import aws_sdk_datazone.types.domain_unit_owners

        out["owners"] = aws_sdk_datazone.types.domain_unit_owners.deserialize_json(
            data["owners"]
        )
    else:
        raise DeserializationError("CreateDomainUnitOutput.owners required")
    if "ancestorDomainUnitIds" in data:
        import aws_sdk_datazone.types.domain_unit_ids

        out["ancestor_domain_unit_ids"] = (
            aws_sdk_datazone.types.domain_unit_ids.deserialize_json(
                data["ancestorDomainUnitIds"]
            )
        )
    else:
        raise DeserializationError(
            "CreateDomainUnitOutput.ancestor_domain_unit_ids required"
        )
    if "createdAt" in data:
        import aws_sdk_datazone.types.created_at

        out["created_at"] = aws_sdk_datazone.types.created_at.deserialize_json(
            data["createdAt"]
        )
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    return out
