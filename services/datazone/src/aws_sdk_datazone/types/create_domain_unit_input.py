"""Generated from Smithy shape ``com.amazonaws.datazone#CreateDomainUnitInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.client_token
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.domain_unit_description
    import aws_sdk_datazone.types.domain_unit_id
    import aws_sdk_datazone.types.domain_unit_name


class CreateDomainUnitInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where you want to crate a domain unit.</p>"""
    name: "aws_sdk_datazone.types.domain_unit_name.DomainUnitName"
    """<p>The name of the domain unit.</p>"""
    parent_domain_unit_identifier: "aws_sdk_datazone.types.domain_unit_id.DomainUnitId"
    """<p>The ID of the parent domain unit.</p>"""
    description: NotRequired[
        "aws_sdk_datazone.types.domain_unit_description.DomainUnitDescription"
    ]
    """<p>The description of the domain unit.</p>"""
    client_token: NotRequired["aws_sdk_datazone.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDomainUnitInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["parentDomainUnitIdentifier"] = value["parent_domain_unit_identifier"]
    if "description" in value:
        out["description"] = value["description"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateDomainUnitInput:
    out: CreateDomainUnitInput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateDomainUnitInput.name required")
    if "parentDomainUnitIdentifier" in data:
        out["parent_domain_unit_identifier"] = data["parentDomainUnitIdentifier"]
    else:
        raise DeserializationError(
            "CreateDomainUnitInput.parent_domain_unit_identifier required"
        )
    if "description" in data:
        out["description"] = data["description"]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
