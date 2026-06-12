"""Generated from Smithy shape ``com.amazonaws.redshift#HsmConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.string
    import aws_sdk_redshift.types.tag_list


class HsmConfiguration(TypedDict):
    hsm_configuration_identifier: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The name of the Amazon Redshift HSM configuration.</p>"""
    description: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>A text description of the HSM configuration.</p>"""
    hsm_ip_address: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The IP address that the Amazon Redshift cluster must use to access the HSM.</p>"""
    hsm_partition_name: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The name of the partition in the HSM where the Amazon Redshift clusters will store their database encryption keys.</p>"""
    tags: NotRequired["aws_sdk_redshift.types.tag_list.TagList"]
    """<p>The list of tags for the HSM configuration.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: HsmConfiguration, pairs: list[tuple[str, str]], prefix: str
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
    if "tags" in value:
        import aws_sdk_redshift.types.tag_list

        aws_sdk_redshift.types.tag_list.serialize_query(
            value["tags"], pairs, f"{prefix}.Tags"
        )


def deserialize_query(el: Element) -> HsmConfiguration:
    out: HsmConfiguration = {}  # type: ignore[typeddict-item]
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
    child_tags = el.find("Tags")
    if child_tags is not None:
        import aws_sdk_redshift.types.tag_list

        out["tags"] = aws_sdk_redshift.types.tag_list.deserialize_query(child_tags)
    return out
