"""Generated from Smithy shape ``com.amazonaws.redshift#ModifyLakehouseConfigurationMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.boolean_optional
    import capo_redshift.types.catalog_name_string
    import capo_redshift.types.lakehouse_idc_registration
    import capo_redshift.types.lakehouse_registration
    import capo_redshift.types.string


class ModifyLakehouseConfigurationMessage(TypedDict, closed=True):
    cluster_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>The unique identifier of the cluster whose lakehouse configuration you want to modify.</p>"""
    lakehouse_registration: NotRequired[
        "capo_redshift.types.lakehouse_registration.LakehouseRegistration"
    ]
    """<p>Specifies whether to register or deregister the cluster with Amazon Redshift federated permissions. Valid values are <code>Register</code> or <code>Deregister</code>.</p>"""
    catalog_name: NotRequired[
        "capo_redshift.types.catalog_name_string.CatalogNameString"
    ]
    """<p>The name of the Glue data catalog that will be associated with the cluster enabled with Amazon Redshift federated permissions.</p> <p>Constraints:</p> <ul> <li> <p>Must contain at least one lowercase letter.</p> </li> <li> <p>Can only contain lowercase letters (a-z), numbers (0-9), underscores (_), and hyphens (-).</p> </li> </ul> <p>Pattern: <code>^[a-z0-9_-]*[a-z]+[a-z0-9_-]*$</code> </p> <p>Example: <code>my-catalog_01</code> </p>"""
    lakehouse_idc_registration: NotRequired[
        "capo_redshift.types.lakehouse_idc_registration.LakehouseIdcRegistration"
    ]
    """<p>Modifies the Amazon Web Services IAM Identity Center trusted identity propagation on a cluster enabled with Amazon Redshift federated permissions. Valid values are <code>Associate</code> or <code>Disassociate</code>.</p>"""
    lakehouse_idc_application_arn: NotRequired["capo_redshift.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the IAM Identity Center application used for enabling Amazon Web Services IAM Identity Center trusted identity propagation on a cluster enabled with Amazon Redshift federated permissions.</p>"""
    dry_run: NotRequired["capo_redshift.types.boolean_optional.BooleanOptional"]
    """<p>A boolean value that, if <code>true</code>, validates the request without actually modifying the lakehouse configuration. Use this to check for errors before making changes.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyLakehouseConfigurationMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "cluster_identifier" in value:
        pairs.append((f"{prefix}.ClusterIdentifier", str(value["cluster_identifier"])))
    if "lakehouse_registration" in value:
        import capo_redshift.types.lakehouse_registration

        capo_redshift.types.lakehouse_registration.serialize_query(
            value["lakehouse_registration"], pairs, f"{prefix}.LakehouseRegistration"
        )
    if "catalog_name" in value:
        pairs.append((f"{prefix}.CatalogName", str(value["catalog_name"])))
    if "lakehouse_idc_registration" in value:
        import capo_redshift.types.lakehouse_idc_registration

        capo_redshift.types.lakehouse_idc_registration.serialize_query(
            value["lakehouse_idc_registration"],
            pairs,
            f"{prefix}.LakehouseIdcRegistration",
        )
    if "lakehouse_idc_application_arn" in value:
        pairs.append(
            (
                f"{prefix}.LakehouseIdcApplicationArn",
                str(value["lakehouse_idc_application_arn"]),
            )
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_query(el: Element) -> ModifyLakehouseConfigurationMessage:
    out: ModifyLakehouseConfigurationMessage = {}  # type: ignore[typeddict-item]
    child_cluster_identifier = el.find("ClusterIdentifier")
    if child_cluster_identifier is not None:
        out["cluster_identifier"] = str(child_cluster_identifier.text or "")
    child_lakehouse_registration = el.find("LakehouseRegistration")
    if child_lakehouse_registration is not None:
        import capo_redshift.types.lakehouse_registration

        out["lakehouse_registration"] = (
            capo_redshift.types.lakehouse_registration.deserialize_query(
                child_lakehouse_registration
            )
        )
    child_catalog_name = el.find("CatalogName")
    if child_catalog_name is not None:
        out["catalog_name"] = str(child_catalog_name.text or "")
    child_lakehouse_idc_registration = el.find("LakehouseIdcRegistration")
    if child_lakehouse_idc_registration is not None:
        import capo_redshift.types.lakehouse_idc_registration

        out["lakehouse_idc_registration"] = (
            capo_redshift.types.lakehouse_idc_registration.deserialize_query(
                child_lakehouse_idc_registration
            )
        )
    child_lakehouse_idc_application_arn = el.find("LakehouseIdcApplicationArn")
    if child_lakehouse_idc_application_arn is not None:
        out["lakehouse_idc_application_arn"] = str(
            child_lakehouse_idc_application_arn.text or ""
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
