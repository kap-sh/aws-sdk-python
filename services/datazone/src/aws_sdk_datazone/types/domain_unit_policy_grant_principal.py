"""Generated from Smithy shape ``com.amazonaws.datazone#DomainUnitPolicyGrantPrincipal``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_unit_designation
    import aws_sdk_datazone.types.domain_unit_grant_filter
    import aws_sdk_datazone.types.domain_unit_id


class DomainUnitPolicyGrantPrincipal(TypedDict, closed=True):
    domain_unit_designation: (
        "aws_sdk_datazone.types.domain_unit_designation.DomainUnitDesignation"
    )
    """<p>Specifes the designation of the domain unit users.</p>"""
    domain_unit_identifier: NotRequired[
        "aws_sdk_datazone.types.domain_unit_id.DomainUnitId"
    ]
    """<p>The ID of the domain unit.</p>"""
    domain_unit_grant_filter: NotRequired[
        "aws_sdk_datazone.types.domain_unit_grant_filter.DomainUnitGrantFilter"
    ]
    """<p>The grant filter for the domain unit.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DomainUnitPolicyGrantPrincipal) -> dict:
    out: dict = {}
    import aws_sdk_datazone.types.domain_unit_designation

    out["domainUnitDesignation"] = (
        aws_sdk_datazone.types.domain_unit_designation.serialize_json(
            value["domain_unit_designation"]
        )
    )
    if "domain_unit_identifier" in value:
        out["domainUnitIdentifier"] = value["domain_unit_identifier"]
    if "domain_unit_grant_filter" in value:
        import aws_sdk_datazone.types.domain_unit_grant_filter

        out["domainUnitGrantFilter"] = (
            aws_sdk_datazone.types.domain_unit_grant_filter.serialize_json(
                value["domain_unit_grant_filter"]
            )
        )
    return out


def deserialize_json(data: dict) -> DomainUnitPolicyGrantPrincipal:
    out: DomainUnitPolicyGrantPrincipal = {}  # type: ignore[typeddict-item]
    if "domainUnitDesignation" in data:
        import aws_sdk_datazone.types.domain_unit_designation

        out["domain_unit_designation"] = (
            aws_sdk_datazone.types.domain_unit_designation.deserialize_json(
                data["domainUnitDesignation"]
            )
        )
    else:
        raise DeserializationError(
            "DomainUnitPolicyGrantPrincipal.domain_unit_designation required"
        )
    if "domainUnitIdentifier" in data:
        out["domain_unit_identifier"] = data["domainUnitIdentifier"]
    if "domainUnitGrantFilter" in data:
        import aws_sdk_datazone.types.domain_unit_grant_filter

        out["domain_unit_grant_filter"] = (
            aws_sdk_datazone.types.domain_unit_grant_filter.deserialize_json(
                data["domainUnitGrantFilter"]
            )
        )
    return out
