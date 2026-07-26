"""Generated from Smithy shape ``com.amazonaws.redshift#CreateHsmConfigurationMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.string
    import capo_redshift.types.tag_list


class CreateHsmConfigurationMessage(TypedDict, closed=True):
    hsm_configuration_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>The identifier to be assigned to the new Amazon Redshift HSM configuration.</p>"""
    description: NotRequired["capo_redshift.types.string.String"]
    """<p>A text description of the HSM configuration to be created.</p>"""
    hsm_ip_address: NotRequired["capo_redshift.types.string.String"]
    """<p>The IP address that the Amazon Redshift cluster must use to access the HSM.</p>"""
    hsm_partition_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The name of the partition in the HSM where the Amazon Redshift clusters will store their database encryption keys.</p>"""
    hsm_partition_password: NotRequired["capo_redshift.types.string.String"]
    """<p>The password required to access the HSM partition.</p>"""
    hsm_server_public_certificate: NotRequired["capo_redshift.types.string.String"]
    """<p>The HSMs public certificate file. When using Cloud HSM, the file name is server.pem.</p>"""
    tags: NotRequired["capo_redshift.types.tag_list.TagList"]
    """<p>A list of tag instances.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateHsmConfigurationMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "hsm_configuration_identifier" in value:
        pairs.append(
            (
                f"{prefix}.HsmConfigurationIdentifier",
                str(value["hsm_configuration_identifier"]),
            )
        )
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "hsm_ip_address" in value:
        pairs.append((f"{prefix}.HsmIpAddress", str(value["hsm_ip_address"])))
    if "hsm_partition_name" in value:
        pairs.append((f"{prefix}.HsmPartitionName", str(value["hsm_partition_name"])))
    if "hsm_partition_password" in value:
        pairs.append(
            (f"{prefix}.HsmPartitionPassword", str(value["hsm_partition_password"]))
        )
    if "hsm_server_public_certificate" in value:
        pairs.append(
            (
                f"{prefix}.HsmServerPublicCertificate",
                str(value["hsm_server_public_certificate"]),
            )
        )
    if "tags" in value:
        import capo_redshift.types.tag_list

        capo_redshift.types.tag_list.serialize_query(
            value["tags"], pairs, f"{prefix}.Tags"
        )


def deserialize_query(el: Element) -> CreateHsmConfigurationMessage:
    out: CreateHsmConfigurationMessage = {}  # type: ignore[typeddict-item]
    child_hsm_configuration_identifier = el.find("HsmConfigurationIdentifier")
    if child_hsm_configuration_identifier is not None:
        out["hsm_configuration_identifier"] = str(
            child_hsm_configuration_identifier.text or ""
        )
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_hsm_ip_address = el.find("HsmIpAddress")
    if child_hsm_ip_address is not None:
        out["hsm_ip_address"] = str(child_hsm_ip_address.text or "")
    child_hsm_partition_name = el.find("HsmPartitionName")
    if child_hsm_partition_name is not None:
        out["hsm_partition_name"] = str(child_hsm_partition_name.text or "")
    child_hsm_partition_password = el.find("HsmPartitionPassword")
    if child_hsm_partition_password is not None:
        out["hsm_partition_password"] = str(child_hsm_partition_password.text or "")
    child_hsm_server_public_certificate = el.find("HsmServerPublicCertificate")
    if child_hsm_server_public_certificate is not None:
        out["hsm_server_public_certificate"] = str(
            child_hsm_server_public_certificate.text or ""
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_redshift.types.tag_list

        out["tags"] = capo_redshift.types.tag_list.deserialize_query(child_tags)
    return out
