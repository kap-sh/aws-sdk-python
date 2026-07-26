"""Generated from Smithy shape ``com.amazonaws.redshift#ModifyAquaInputMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.aqua_configuration_status
    import capo_redshift.types.string


class ModifyAquaInputMessage(TypedDict, closed=True):
    cluster_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>The identifier of the cluster to be modified.</p>"""
    aqua_configuration_status: NotRequired[
        "capo_redshift.types.aqua_configuration_status.AquaConfigurationStatus"
    ]
    """<p>This parameter is retired. Amazon Redshift automatically determines whether to use AQUA (Advanced Query Accelerator).</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyAquaInputMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cluster_identifier" in value:
        pairs.append((f"{prefix}.ClusterIdentifier", str(value["cluster_identifier"])))
    if "aqua_configuration_status" in value:
        import capo_redshift.types.aqua_configuration_status

        capo_redshift.types.aqua_configuration_status.serialize_query(
            value["aqua_configuration_status"],
            pairs,
            f"{prefix}.AquaConfigurationStatus",
        )


def deserialize_query(el: Element) -> ModifyAquaInputMessage:
    out: ModifyAquaInputMessage = {}  # type: ignore[typeddict-item]
    child_cluster_identifier = el.find("ClusterIdentifier")
    if child_cluster_identifier is not None:
        out["cluster_identifier"] = str(child_cluster_identifier.text or "")
    child_aqua_configuration_status = el.find("AquaConfigurationStatus")
    if child_aqua_configuration_status is not None:
        import capo_redshift.types.aqua_configuration_status

        out["aqua_configuration_status"] = (
            capo_redshift.types.aqua_configuration_status.deserialize_query(
                child_aqua_configuration_status
            )
        )
    return out
