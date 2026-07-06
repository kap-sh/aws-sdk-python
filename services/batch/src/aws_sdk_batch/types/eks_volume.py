"""Generated from Smithy shape ``com.amazonaws.batch#EksVolume``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_batch.types.eks_empty_dir
    import aws_sdk_batch.types.eks_host_path
    import aws_sdk_batch.types.eks_persistent_volume_claim
    import aws_sdk_batch.types.eks_secret
    import aws_sdk_batch.types.string


class EksVolume(TypedDict, closed=True):
    name: NotRequired["aws_sdk_batch.types.string.String"]
    r"""<p>The name of the volume. The name must be allowed as a DNS subdomain name. For more information, see <a href=\"https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-subdomain-names\">DNS subdomain names</a> in the <i>Kubernetes documentation</i>.</p>"""
    host_path: NotRequired["aws_sdk_batch.types.eks_host_path.EksHostPath"]
    r"""<p>Specifies the configuration of a Kubernetes <code>hostPath</code> volume. For more information, see <a href=\"https://kubernetes.io/docs/concepts/storage/volumes/#hostpath\">hostPath</a> in the <i>Kubernetes documentation</i>.</p>"""
    empty_dir: NotRequired["aws_sdk_batch.types.eks_empty_dir.EksEmptyDir"]
    r"""<p>Specifies the configuration of a Kubernetes <code>emptyDir</code> volume. For more information, see <a href=\"https://kubernetes.io/docs/concepts/storage/volumes/#emptydir\">emptyDir</a> in the <i>Kubernetes documentation</i>.</p>"""
    secret: NotRequired["aws_sdk_batch.types.eks_secret.EksSecret"]
    r"""<p>Specifies the configuration of a Kubernetes <code>secret</code> volume. For more information, see <a href=\"https://kubernetes.io/docs/concepts/storage/volumes/#secret\">secret</a> in the <i>Kubernetes documentation</i>.</p>"""
    persistent_volume_claim: NotRequired[
        "aws_sdk_batch.types.eks_persistent_volume_claim.EksPersistentVolumeClaim"
    ]
    r"""<p>Specifies the configuration of a Kubernetes <code>persistentVolumeClaim</code> bounded to a <code>persistentVolume</code>. For more information, see <a href=\"https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims\"> Persistent Volume Claims</a> in the <i>Kubernetes documentation</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EksVolume) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "host_path" in value:
        import aws_sdk_batch.types.eks_host_path

        out["hostPath"] = aws_sdk_batch.types.eks_host_path.serialize_json(
            value["host_path"]
        )
    if "empty_dir" in value:
        import aws_sdk_batch.types.eks_empty_dir

        out["emptyDir"] = aws_sdk_batch.types.eks_empty_dir.serialize_json(
            value["empty_dir"]
        )
    if "secret" in value:
        import aws_sdk_batch.types.eks_secret

        out["secret"] = aws_sdk_batch.types.eks_secret.serialize_json(value["secret"])
    if "persistent_volume_claim" in value:
        import aws_sdk_batch.types.eks_persistent_volume_claim

        out["persistentVolumeClaim"] = (
            aws_sdk_batch.types.eks_persistent_volume_claim.serialize_json(
                value["persistent_volume_claim"]
            )
        )
    return out


def deserialize_json(data: dict) -> EksVolume:
    out: EksVolume = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "hostPath" in data:
        import aws_sdk_batch.types.eks_host_path

        out["host_path"] = aws_sdk_batch.types.eks_host_path.deserialize_json(
            data["hostPath"]
        )
    if "emptyDir" in data:
        import aws_sdk_batch.types.eks_empty_dir

        out["empty_dir"] = aws_sdk_batch.types.eks_empty_dir.deserialize_json(
            data["emptyDir"]
        )
    if "secret" in data:
        import aws_sdk_batch.types.eks_secret

        out["secret"] = aws_sdk_batch.types.eks_secret.deserialize_json(data["secret"])
    if "persistentVolumeClaim" in data:
        import aws_sdk_batch.types.eks_persistent_volume_claim

        out["persistent_volume_claim"] = (
            aws_sdk_batch.types.eks_persistent_volume_claim.deserialize_json(
                data["persistentVolumeClaim"]
            )
        )
    return out
