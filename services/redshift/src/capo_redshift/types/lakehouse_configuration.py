"""Generated from Smithy shape ``com.amazonaws.redshift#LakehouseConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.string


class LakehouseConfiguration(TypedDict, closed=True):
    cluster_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>The unique identifier of the cluster associated with this lakehouse configuration.</p>"""
    lakehouse_idc_application_arn: NotRequired["capo_redshift.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the IAM Identity Center application used for enabling Amazon Web Services IAM Identity Center trusted identity propagation on a cluster enabled with Amazon Redshift federated permissions.</p>"""
    lakehouse_registration_status: NotRequired["capo_redshift.types.string.String"]
    """<p>The current status of the lakehouse registration. Indicates whether the cluster is successfully registered with the lakehouse.</p>"""
    catalog_arn: NotRequired["capo_redshift.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Glue data catalog associated with the lakehouse configuration.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: LakehouseConfiguration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cluster_identifier" in value:
        pairs.append((f"{prefix}.ClusterIdentifier", str(value["cluster_identifier"])))
    if "lakehouse_idc_application_arn" in value:
        pairs.append(
            (
                f"{prefix}.LakehouseIdcApplicationArn",
                str(value["lakehouse_idc_application_arn"]),
            )
        )
    if "lakehouse_registration_status" in value:
        pairs.append(
            (
                f"{prefix}.LakehouseRegistrationStatus",
                str(value["lakehouse_registration_status"]),
            )
        )
    if "catalog_arn" in value:
        pairs.append((f"{prefix}.CatalogArn", str(value["catalog_arn"])))


def deserialize_query(el: Element) -> LakehouseConfiguration:
    out: LakehouseConfiguration = {}  # type: ignore[typeddict-item]
    child_cluster_identifier = el.find("ClusterIdentifier")
    if child_cluster_identifier is not None:
        out["cluster_identifier"] = str(child_cluster_identifier.text or "")
    child_lakehouse_idc_application_arn = el.find("LakehouseIdcApplicationArn")
    if child_lakehouse_idc_application_arn is not None:
        out["lakehouse_idc_application_arn"] = str(
            child_lakehouse_idc_application_arn.text or ""
        )
    child_lakehouse_registration_status = el.find("LakehouseRegistrationStatus")
    if child_lakehouse_registration_status is not None:
        out["lakehouse_registration_status"] = str(
            child_lakehouse_registration_status.text or ""
        )
    child_catalog_arn = el.find("CatalogArn")
    if child_catalog_arn is not None:
        out["catalog_arn"] = str(child_catalog_arn.text or "")
    return out
