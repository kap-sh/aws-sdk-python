"""Generated from Smithy shape ``com.amazonaws.tnb#GetSolVnfcResourceInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_tnb.types.get_sol_vnfc_resource_info_metadata


class GetSolVnfcResourceInfo(TypedDict, closed=True):
    metadata: NotRequired[
        "aws_sdk_tnb.types.get_sol_vnfc_resource_info_metadata.GetSolVnfcResourceInfoMetadata"
    ]
    """<p>The metadata of the network function compute.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSolVnfcResourceInfo) -> dict:
    out: dict = {}
    if "metadata" in value:
        import aws_sdk_tnb.types.get_sol_vnfc_resource_info_metadata

        out["metadata"] = (
            aws_sdk_tnb.types.get_sol_vnfc_resource_info_metadata.serialize_json(
                value["metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetSolVnfcResourceInfo:
    out: GetSolVnfcResourceInfo = {}  # type: ignore[typeddict-item]
    if "metadata" in data:
        import aws_sdk_tnb.types.get_sol_vnfc_resource_info_metadata

        out["metadata"] = (
            aws_sdk_tnb.types.get_sol_vnfc_resource_info_metadata.deserialize_json(
                data["metadata"]
            )
        )
    return out
