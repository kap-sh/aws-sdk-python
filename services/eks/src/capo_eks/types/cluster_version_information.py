"""Generated from Smithy shape ``com.amazonaws.eks#ClusterVersionInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.boolean
    import capo_eks.types.cluster_version_status
    import capo_eks.types.string
    import capo_eks.types.timestamp
    import capo_eks.types.version_status


class ClusterVersionInformation(TypedDict, closed=True):
    cluster_version: NotRequired["capo_eks.types.string.String"]
    """<p>The Kubernetes version for the cluster.</p>"""
    cluster_type: NotRequired["capo_eks.types.string.String"]
    """<p>The type of cluster this version is for.</p>"""
    default_platform_version: NotRequired["capo_eks.types.string.String"]
    """<p>Default platform version for this Kubernetes version.</p>"""
    default_version: "capo_eks.types.boolean.Boolean"
    """<p>Indicates if this is a default version.</p>"""
    release_date: NotRequired["capo_eks.types.timestamp.Timestamp"]
    """<p>The release date of this cluster version.</p>"""
    end_of_standard_support_date: NotRequired["capo_eks.types.timestamp.Timestamp"]
    """<p>Date when standard support ends for this version.</p>"""
    end_of_extended_support_date: NotRequired["capo_eks.types.timestamp.Timestamp"]
    """<p>Date when extended support ends for this version.</p>"""
    status: NotRequired["capo_eks.types.cluster_version_status.ClusterVersionStatus"]
    """<important> <p>This field is deprecated. Use <code>versionStatus</code> instead, as that field matches for input and output of this action.</p> </important> <p>Current status of this cluster version.</p>"""
    version_status: NotRequired["capo_eks.types.version_status.VersionStatus"]
    """<p>Current status of this cluster version.</p>"""
    kubernetes_patch_version: NotRequired["capo_eks.types.string.String"]
    """<p>The patch version of Kubernetes for this cluster version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClusterVersionInformation) -> dict:
    out: dict = {}
    if "cluster_version" in value:
        out["clusterVersion"] = value["cluster_version"]
    if "cluster_type" in value:
        out["clusterType"] = value["cluster_type"]
    if "default_platform_version" in value:
        out["defaultPlatformVersion"] = value["default_platform_version"]
    out["defaultVersion"] = value.get("default_version", False)
    if "release_date" in value:
        import capo_eks.types.timestamp

        out["releaseDate"] = capo_eks.types.timestamp.serialize_json(
            value["release_date"]
        )
    if "end_of_standard_support_date" in value:
        import capo_eks.types.timestamp

        out["endOfStandardSupportDate"] = capo_eks.types.timestamp.serialize_json(
            value["end_of_standard_support_date"]
        )
    if "end_of_extended_support_date" in value:
        import capo_eks.types.timestamp

        out["endOfExtendedSupportDate"] = capo_eks.types.timestamp.serialize_json(
            value["end_of_extended_support_date"]
        )
    if "status" in value:
        import capo_eks.types.cluster_version_status

        out["status"] = capo_eks.types.cluster_version_status.serialize_json(
            value["status"]
        )
    if "version_status" in value:
        import capo_eks.types.version_status

        out["versionStatus"] = capo_eks.types.version_status.serialize_json(
            value["version_status"]
        )
    if "kubernetes_patch_version" in value:
        out["kubernetesPatchVersion"] = value["kubernetes_patch_version"]
    return out


def deserialize_json(data: dict) -> ClusterVersionInformation:
    out: ClusterVersionInformation = {}  # type: ignore[typeddict-item]
    if "clusterVersion" in data:
        out["cluster_version"] = data["clusterVersion"]
    if "clusterType" in data:
        out["cluster_type"] = data["clusterType"]
    if "defaultPlatformVersion" in data:
        out["default_platform_version"] = data["defaultPlatformVersion"]
    if "defaultVersion" in data:
        out["default_version"] = data["defaultVersion"]
    else:
        out["default_version"] = False
    if "releaseDate" in data:
        import capo_eks.types.timestamp

        out["release_date"] = capo_eks.types.timestamp.deserialize_json(
            data["releaseDate"]
        )
    if "endOfStandardSupportDate" in data:
        import capo_eks.types.timestamp

        out["end_of_standard_support_date"] = capo_eks.types.timestamp.deserialize_json(
            data["endOfStandardSupportDate"]
        )
    if "endOfExtendedSupportDate" in data:
        import capo_eks.types.timestamp

        out["end_of_extended_support_date"] = capo_eks.types.timestamp.deserialize_json(
            data["endOfExtendedSupportDate"]
        )
    if "status" in data:
        import capo_eks.types.cluster_version_status

        out["status"] = capo_eks.types.cluster_version_status.deserialize_json(
            data["status"]
        )
    if "versionStatus" in data:
        import capo_eks.types.version_status

        out["version_status"] = capo_eks.types.version_status.deserialize_json(
            data["versionStatus"]
        )
    if "kubernetesPatchVersion" in data:
        out["kubernetes_patch_version"] = data["kubernetesPatchVersion"]
    return out
