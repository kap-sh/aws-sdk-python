"""Generated from Smithy shape ``com.amazonaws.lakeformation#DescribeLakeFormationIdentityCenterConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.application_arn
    import capo_lakeformation.types.catalog_id_string
    import capo_lakeformation.types.data_lake_principal_list
    import capo_lakeformation.types.external_filtering_configuration
    import capo_lakeformation.types.identity_center_instance_arn
    import capo_lakeformation.types.ram_resource_share_arn
    import capo_lakeformation.types.service_integration_list


class DescribeLakeFormationIdentityCenterConfigurationResponse(TypedDict, closed=True):
    catalog_id: NotRequired[
        "capo_lakeformation.types.catalog_id_string.CatalogIdString"
    ]
    """<p>The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment.</p>"""
    instance_arn: NotRequired[
        "capo_lakeformation.types.identity_center_instance_arn.IdentityCenterInstanceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the connection.</p>"""
    application_arn: NotRequired[
        "capo_lakeformation.types.application_arn.ApplicationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the Lake Formation application integrated with IAM Identity Center.</p>"""
    external_filtering: NotRequired[
        "capo_lakeformation.types.external_filtering_configuration.ExternalFilteringConfiguration"
    ]
    """<p>Indicates if external filtering is enabled.</p>"""
    share_recipients: NotRequired[
        "capo_lakeformation.types.data_lake_principal_list.DataLakePrincipalList"
    ]
    """<p>A list of Amazon Web Services account IDs or Amazon Web Services organization/organizational unit ARNs that are allowed to access data managed by Lake Formation. </p> <p>If the <code>ShareRecipients</code> list includes valid values, a resource share is created with the principals you want to have access to the resources as the <code>ShareRecipients</code>.</p> <p>If the <code>ShareRecipients</code> value is null or the list is empty, no resource share is created.</p>"""
    service_integrations: NotRequired[
        "capo_lakeformation.types.service_integration_list.ServiceIntegrationList"
    ]
    """<p>A list of service integrations for enabling trusted identity propagation with external services such as Redshift.</p>"""
    resource_share: NotRequired[
        "capo_lakeformation.types.ram_resource_share_arn.RAMResourceShareArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the RAM share.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: DescribeLakeFormationIdentityCenterConfigurationResponse,
) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    if "instance_arn" in value:
        out["InstanceArn"] = value["instance_arn"]
    if "application_arn" in value:
        out["ApplicationArn"] = value["application_arn"]
    if "external_filtering" in value:
        import capo_lakeformation.types.external_filtering_configuration

        out["ExternalFiltering"] = (
            capo_lakeformation.types.external_filtering_configuration.serialize_json(
                value["external_filtering"]
            )
        )
    if "share_recipients" in value:
        import capo_lakeformation.types.data_lake_principal_list

        out["ShareRecipients"] = (
            capo_lakeformation.types.data_lake_principal_list.serialize_json(
                value["share_recipients"]
            )
        )
    if "service_integrations" in value:
        import capo_lakeformation.types.service_integration_list

        out["ServiceIntegrations"] = (
            capo_lakeformation.types.service_integration_list.serialize_json(
                value["service_integrations"]
            )
        )
    if "resource_share" in value:
        out["ResourceShare"] = value["resource_share"]
    return out


def deserialize_json(
    data: dict,
) -> DescribeLakeFormationIdentityCenterConfigurationResponse:
    out: DescribeLakeFormationIdentityCenterConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "InstanceArn" in data:
        out["instance_arn"] = data["InstanceArn"]
    if "ApplicationArn" in data:
        out["application_arn"] = data["ApplicationArn"]
    if "ExternalFiltering" in data:
        import capo_lakeformation.types.external_filtering_configuration

        out["external_filtering"] = (
            capo_lakeformation.types.external_filtering_configuration.deserialize_json(
                data["ExternalFiltering"]
            )
        )
    if "ShareRecipients" in data:
        import capo_lakeformation.types.data_lake_principal_list

        out["share_recipients"] = (
            capo_lakeformation.types.data_lake_principal_list.deserialize_json(
                data["ShareRecipients"]
            )
        )
    if "ServiceIntegrations" in data:
        import capo_lakeformation.types.service_integration_list

        out["service_integrations"] = (
            capo_lakeformation.types.service_integration_list.deserialize_json(
                data["ServiceIntegrations"]
            )
        )
    if "ResourceShare" in data:
        out["resource_share"] = data["ResourceShare"]
    return out
