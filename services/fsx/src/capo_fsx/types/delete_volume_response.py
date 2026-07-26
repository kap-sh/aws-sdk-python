"""Generated from Smithy shape ``com.amazonaws.fsx#DeleteVolumeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.delete_volume_ontap_response
    import capo_fsx.types.volume_id
    import capo_fsx.types.volume_lifecycle


class DeleteVolumeResponse(TypedDict, closed=True):
    volume_id: NotRequired["capo_fsx.types.volume_id.VolumeId"]
    """<p>The ID of the volume that's being deleted.</p>"""
    lifecycle: NotRequired["capo_fsx.types.volume_lifecycle.VolumeLifecycle"]
    """<p>The lifecycle state of the volume being deleted. If the <code>DeleteVolume</code> operation is successful, this value is <code>DELETING</code>.</p>"""
    ontap_response: NotRequired[
        "capo_fsx.types.delete_volume_ontap_response.DeleteVolumeOntapResponse"
    ]
    """<p>Returned after a <code>DeleteVolume</code> request, showing the status of the delete request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteVolumeResponse) -> dict:
    out: dict = {}
    if "volume_id" in value:
        out["VolumeId"] = value["volume_id"]
    if "lifecycle" in value:
        import capo_fsx.types.volume_lifecycle

        out["Lifecycle"] = capo_fsx.types.volume_lifecycle.serialize_aws_json_1_1(
            value["lifecycle"]
        )
    if "ontap_response" in value:
        import capo_fsx.types.delete_volume_ontap_response

        out["OntapResponse"] = (
            capo_fsx.types.delete_volume_ontap_response.serialize_aws_json_1_1(
                value["ontap_response"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteVolumeResponse:
    out: DeleteVolumeResponse = {}  # type: ignore[typeddict-item]
    if "VolumeId" in data:
        out["volume_id"] = data["VolumeId"]
    if "Lifecycle" in data:
        import capo_fsx.types.volume_lifecycle

        out["lifecycle"] = capo_fsx.types.volume_lifecycle.deserialize_aws_json_1_1(
            data["Lifecycle"]
        )
    if "OntapResponse" in data:
        import capo_fsx.types.delete_volume_ontap_response

        out["ontap_response"] = (
            capo_fsx.types.delete_volume_ontap_response.deserialize_aws_json_1_1(
                data["OntapResponse"]
            )
        )
    return out
