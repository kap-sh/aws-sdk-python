"""Generated from Smithy shape ``com.amazonaws.sagemakeredge#Definition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker_edge.types.checksum
    import aws_sdk_sagemaker_edge.types.entity_name
    import aws_sdk_sagemaker_edge.types.model_state
    import aws_sdk_sagemaker_edge.types.s3_uri


class Definition(TypedDict, closed=True):
    model_handle: NotRequired["aws_sdk_sagemaker_edge.types.entity_name.EntityName"]
    """<p>The unique model handle.</p>"""
    s3_url: NotRequired["aws_sdk_sagemaker_edge.types.s3_uri.S3Uri"]
    """<p>The absolute S3 location of the model.</p>"""
    checksum: NotRequired["aws_sdk_sagemaker_edge.types.checksum.Checksum"]
    """<p>The checksum information of the model.</p>"""
    state: NotRequired["aws_sdk_sagemaker_edge.types.model_state.ModelState"]
    """<p>The desired state of the model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Definition) -> dict:
    out: dict = {}
    if "model_handle" in value:
        out["ModelHandle"] = value["model_handle"]
    if "s3_url" in value:
        out["S3Url"] = value["s3_url"]
    if "checksum" in value:
        import aws_sdk_sagemaker_edge.types.checksum

        out["Checksum"] = aws_sdk_sagemaker_edge.types.checksum.serialize_json(
            value["checksum"]
        )
    if "state" in value:
        import aws_sdk_sagemaker_edge.types.model_state

        out["State"] = aws_sdk_sagemaker_edge.types.model_state.serialize_json(
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
        import aws_sdk_sagemaker_edge.types.checksum

        out["checksum"] = aws_sdk_sagemaker_edge.types.checksum.deserialize_json(
            data["Checksum"]
        )
    if "State" in data:
        import aws_sdk_sagemaker_edge.types.model_state

        out["state"] = aws_sdk_sagemaker_edge.types.model_state.deserialize_json(
            data["State"]
        )
    return out
