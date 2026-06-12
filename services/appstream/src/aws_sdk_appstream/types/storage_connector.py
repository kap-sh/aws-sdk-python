"""Generated from Smithy shape ``com.amazonaws.appstream#StorageConnector``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appstream.types.domain_list
    import aws_sdk_appstream.types.resource_identifier
    import aws_sdk_appstream.types.storage_connector_type


class StorageConnector(TypedDict):
    connector_type: NotRequired[
        "aws_sdk_appstream.types.storage_connector_type.StorageConnectorType"
    ]
    """<p>The type of storage connector.</p>"""
    resource_identifier: NotRequired[
        "aws_sdk_appstream.types.resource_identifier.ResourceIdentifier"
    ]
    """<p>The ARN of the storage connector.</p>"""
    domains: NotRequired["aws_sdk_appstream.types.domain_list.DomainList"]
    """<p>The names of the domains for the account.</p>"""
    domains_require_admin_consent: NotRequired[
        "aws_sdk_appstream.types.domain_list.DomainList"
    ]
    """<p>The OneDrive for Business domains where you require admin consent when users try to link their OneDrive account to WorkSpaces Applications. The attribute can only be specified when ConnectorType=ONE_DRIVE.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StorageConnector) -> dict:
    out: dict = {}
    if "connector_type" in value:
        import aws_sdk_appstream.types.storage_connector_type

        out["ConnectorType"] = (
            aws_sdk_appstream.types.storage_connector_type.serialize_aws_json_1_1(
                value["connector_type"]
            )
        )
    if "resource_identifier" in value:
        out["ResourceIdentifier"] = value["resource_identifier"]
    if "domains" in value:
        import aws_sdk_appstream.types.domain_list

        out["Domains"] = aws_sdk_appstream.types.domain_list.serialize_aws_json_1_1(
            value["domains"]
        )
    if "domains_require_admin_consent" in value:
        import aws_sdk_appstream.types.domain_list

        out["DomainsRequireAdminConsent"] = (
            aws_sdk_appstream.types.domain_list.serialize_aws_json_1_1(
                value["domains_require_admin_consent"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StorageConnector:
    out: StorageConnector = {}  # type: ignore[typeddict-item]
    if "ConnectorType" in data:
        import aws_sdk_appstream.types.storage_connector_type

        out["connector_type"] = (
            aws_sdk_appstream.types.storage_connector_type.deserialize_aws_json_1_1(
                data["ConnectorType"]
            )
        )
    if "ResourceIdentifier" in data:
        out["resource_identifier"] = data["ResourceIdentifier"]
    if "Domains" in data:
        import aws_sdk_appstream.types.domain_list

        out["domains"] = aws_sdk_appstream.types.domain_list.deserialize_aws_json_1_1(
            data["Domains"]
        )
    if "DomainsRequireAdminConsent" in data:
        import aws_sdk_appstream.types.domain_list

        out["domains_require_admin_consent"] = (
            aws_sdk_appstream.types.domain_list.deserialize_aws_json_1_1(
                data["DomainsRequireAdminConsent"]
            )
        )
    return out
