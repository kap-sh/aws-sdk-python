"""Generated from Smithy shape ``com.amazonaws.supplychain#DataIntegrationFlowS3Options``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_supplychain.types.data_integration_flow_file_type


class DataIntegrationFlowS3Options(TypedDict, closed=True):
    file_type: NotRequired[
        "capo_supplychain.types.data_integration_flow_file_type.DataIntegrationFlowFileType"
    ]
    """<p>The Amazon S3 file type in S3 options.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataIntegrationFlowS3Options) -> dict:
    out: dict = {}
    if "file_type" in value:
        import capo_supplychain.types.data_integration_flow_file_type

        out["fileType"] = (
            capo_supplychain.types.data_integration_flow_file_type.serialize_json(
                value["file_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataIntegrationFlowS3Options:
    out: DataIntegrationFlowS3Options = {}  # type: ignore[typeddict-item]
    if "fileType" in data:
        import capo_supplychain.types.data_integration_flow_file_type

        out["file_type"] = (
            capo_supplychain.types.data_integration_flow_file_type.deserialize_json(
                data["fileType"]
            )
        )
    return out
