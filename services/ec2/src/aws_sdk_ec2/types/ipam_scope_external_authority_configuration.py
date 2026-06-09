"""Generated from Smithy shape ``com.amazonaws.ec2#IpamScopeExternalAuthorityConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_scope_external_authority_type
    import aws_sdk_ec2.types.string


class IpamScopeExternalAuthorityConfiguration(TypedDict):
    type: NotRequired[
        "aws_sdk_ec2.types.ipam_scope_external_authority_type.IpamScopeExternalAuthorityType"
    ]
    """<p>The type of external authority managing this scope. Currently supports <code>Infoblox</code> for integration with Infoblox Universal DDI.</p>"""
    external_resource_identifier: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The identifier for the external resource managing this scope. For Infoblox integrations, this is the Infoblox resource identifier in the format <code><version>.identity.account.<entity_realm>.<entity_id></code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamScopeExternalAuthorityConfiguration,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "type" in value:
        import aws_sdk_ec2.types.ipam_scope_external_authority_type

        aws_sdk_ec2.types.ipam_scope_external_authority_type.serialize_ec2_query(
            value["type"], pairs, f"{prefix}.Type"
        )
    if "external_resource_identifier" in value:
        pairs.append(
            (
                f"{prefix}.ExternalResourceIdentifier",
                str(value["external_resource_identifier"]),
            )
        )


def deserialize_ec2_query(el: Element) -> IpamScopeExternalAuthorityConfiguration:
    out: IpamScopeExternalAuthorityConfiguration = {}  # type: ignore[typeddict-item]
    child_type = el.find("Type")
    if child_type is not None:
        import aws_sdk_ec2.types.ipam_scope_external_authority_type

        out["type"] = (
            aws_sdk_ec2.types.ipam_scope_external_authority_type.deserialize_ec2_query(
                child_type
            )
        )
    child_external_resource_identifier = el.find("ExternalResourceIdentifier")
    if child_external_resource_identifier is not None:
        out["external_resource_identifier"] = str(
            child_external_resource_identifier.text or ""
        )
    return out
