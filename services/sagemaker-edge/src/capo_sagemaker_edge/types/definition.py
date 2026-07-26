"""Generated from Smithy shape ``com.amazonaws.sagemakeredge#Definition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_edge.types.checksum
    import capo_sagemaker_edge.types.entity_name
    import capo_sagemaker_edge.types.model_state
    import capo_sagemaker_edge.types.s3_uri


class Definition(TypedDict, closed=True):
    model_handle: NotRequired["capo_sagemaker_edge.types.entity_name.EntityName"]
    """<p>The unique model handle.</p>"""
    s3_url: NotRequired["capo_sagemaker_edge.types.s3_uri.S3Uri"]
    """<p>The absolute S3 location of the model.</p>"""
    checksum: NotRequired["capo_sagemaker_edge.types.checksum.Checksum"]
    """<p>The checksum information of the model.</p>"""
    state: NotRequired["capo_sagemaker_edge.types.model_state.ModelState"]
    """<p>The desired state of the model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Definition) -> dict:
    out: dict = {}
    if "model_handle" in value:
        out["ModelHandle"] = value["model_handle"]
    if "s3_url" in value:
        out["S3Url"] = value["s3_url"]
    if "checksum" in value:
        import capo_sagemaker_edge.types.checksum

        out["Checksum"] = capo_sagemaker_edge.types.checksum.serialize_json(
            value["checksum"]
        )
    if "state" in value:
        import capo_sagemaker_edge.types.model_state

        out["State"] = capo_sagemaker_edge.types.model_state.serialize_json(
            value["state"]
        )
    return out


def deserialize_json(data: dict) -> Definition:
    out: Definition = {}  # type: ignore[typeddict-item]
    if "ModelHandle" in data:
        out["model_handle"] = data["ModelHandle"]
    if "S3Url" in data:
        out["s3_url"] = data["S3Url"]
    if "Checksum" in data:
        import capo_sagemaker_edge.types.checksum

        out["checksum"] = capo_sagemaker_edge.types.checksum.deserialize_json(
            data["Checksum"]
        )
    if "State" in data:
        import capo_sagemaker_edge.types.model_state

        out["state"] = capo_sagemaker_edge.types.model_state.deserialize_json(
            data["State"]
        )
    return out
