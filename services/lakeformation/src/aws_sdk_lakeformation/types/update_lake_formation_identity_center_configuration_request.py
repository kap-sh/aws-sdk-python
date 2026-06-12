"""Generated from Smithy shape ``com.amazonaws.lakeformation#UpdateLakeFormationIdentityCenterConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.application_status
    import aws_sdk_lakeformation.types.catalog_id_string
    import aws_sdk_lakeformation.types.data_lake_principal_list
    import aws_sdk_lakeformation.types.external_filtering_configuration
    import aws_sdk_lakeformation.types.service_integration_list


class UpdateLakeFormationIdentityCenterConfigurationRequest(TypedDict):
    catalog_id: NotRequired[
        "aws_sdk_lakeformation.types.catalog_id_string.CatalogIdString"
    ]
    """<p>The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, view definitions, and other control information to manage your Lake Formation environment.</p>"""
    share_recipients: NotRequired[
        "aws_sdk_lakeformation.types.data_lake_principal_list.DataLakePrincipalList"
    ]
    """<p>A list of Amazon Web Services account IDs or Amazon Web Services organization/organizational unit ARNs that are allowed to access to access data managed by Lake Formation. </p> <p>If the <code>ShareRecipients</code> list includes valid values, then the resource share is updated with the principals you want to have access to the resources.</p> <p>If the <code>ShareRecipients</code> value is null, both the list of share recipients and the resource share remain unchanged.</p> <p>If the <code>ShareRecipients</code> value is an empty list, then the existing share recipients list will be cleared, and the resource share will be deleted.</p>"""
    service_integrations: NotRequired[
        "aws_sdk_lakeformation.types.service_integration_list.ServiceIntegrationList"
    ]
    """<p>A list of service integrations for enabling trusted identity propagation with external services such as Redshift.</p>"""
    application_status: NotRequired[
        "aws_sdk_lakeformation.types.application_status.ApplicationStatus"
    ]
    """<p>Allows to enable or disable the IAM Identity Center connection.</p>"""
    external_filtering: NotRequired[
        "aws_sdk_lakeformation.types.external_filtering_configuration.ExternalFilteringConfiguration"
    ]
    """<p>A list of the account IDs of Amazon Web Services accounts of third-party applications that are allowed to access data managed by Lake Formation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: UpdateLakeFormationIdentityCenterConfigurationRequest,
) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    if "share_recipients" in value:
        import aws_sdk_lakeformation.types.data_lake_principal_list

        out["ShareRecipients"] = (
            aws_sdk_lakeformation.types.data_lake_principal_list.serialize_json(
                value["share_recipients"]
            )
        )
    if "service_integrations" in value:
        import aws_sdk_lakeformation.types.service_integration_list

        out["ServiceIntegrations"] = (
            aws_sdk_lakeformation.types.service_integration_list.serialize_json(
                value["service_integrations"]
            )
        )
    if "application_status" in value:
        import aws_sdk_lakeformation.types.application_status

        out["ApplicationStatus"] = (
            aws_sdk_lakeformation.types.application_status.serialize_json(
                value["application_status"]
            )
        )
    if "external_filtering" in value:
        import aws_sdk_lakeformation.types.external_filtering_configuration

        out["ExternalFiltering"] = (
            aws_sdk_lakeformation.types.external_filtering_configuration.serialize_json(
                value["external_filtering"]
            )
        )
    return out


def deserialize_json(
    data: dict,
) -> UpdateLakeFormationIdentityCenterConfigurationRequest:
    out: UpdateLakeFormationIdentityCenterConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "ShareRecipients" in data:
        import aws_sdk_lakeformation.types.data_lake_principal_list

        out["share_recipients"] = (
            aws_sdk_lakeformation.types.data_lake_principal_list.deserialize_json(
                data["ShareRecipients"]
            )
        )
    if "ServiceIntegrations" in data:
        import aws_sdk_lakeformation.types.service_integration_list

        out["service_integrations"] = (
            aws_sdk_lakeformation.types.service_integration_list.deserialize_json(
                data["ServiceIntegrations"]
            )
        )
    if "ApplicationStatus" in data:
        import aws_sdk_lakeformation.types.application_status

        out["application_status"] = (
            aws_sdk_lakeformation.types.application_status.deserialize_json(
                data["ApplicationStatus"]
            )
        )
    if "ExternalFiltering" in data:
        import aws_sdk_lakeformation.types.external_filtering_configuration

        out["external_filtering"] = (
            aws_sdk_lakeformation.types.external_filtering_configuration.deserialize_json(
                data["ExternalFiltering"]
            )
        )
    return out
