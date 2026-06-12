"""Generated from Smithy shape ``com.amazonaws.redshift#ClusterVersion``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.string


class ClusterVersion(TypedDict):
    cluster_version: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The version number used by the cluster.</p>"""
    cluster_parameter_group_family: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The name of the cluster parameter group family for the cluster.</p>"""
    description: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The description of the cluster version.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ClusterVersion, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cluster_version" in value:
        pairs.append((f"{prefix}.ClusterVersion", str(value["cluster_version"])))
    if "cluster_parameter_group_family" in value:
        pairs.append(
            (
                f"{prefix}.ClusterParameterGroupFamily",
                str(value["cluster_parameter_group_family"]),
            )
        )
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))


def deserialize_query(el: Element) -> ClusterVersion:
    out: ClusterVersion = {}  # type: ignore[typeddict-item]
    child_cluster_version = el.find("ClusterVersion")
    if child_cluster_version is not None:
        out["cluster_version"] = str(child_cluster_version.text or "")
    child_cluster_parameter_group_family = el.find("ClusterParameterGroupFamily")
    if child_cluster_parameter_group_family is not None:
        out["cluster_parameter_group_family"] = str(
            child_cluster_parameter_group_family.text or ""
        )
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    return out
