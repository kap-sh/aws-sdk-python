"""Generated from Smithy shape ``com.amazonaws.odb#GetCloudExadataInfrastructureOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.cloud_exadata_infrastructure


class GetCloudExadataInfrastructureOutput(TypedDict, closed=True):
    cloud_exadata_infrastructure: NotRequired[
        "capo_odb.types.cloud_exadata_infrastructure.CloudExadataInfrastructure"
    ]
    """<p>The Exadata infrastructure.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetCloudExadataInfrastructureOutput) -> dict:
    out: dict = {}
    if "cloud_exadata_infrastructure" in value:
        import capo_odb.types.cloud_exadata_infrastructure

        out["cloudExadataInfrastructure"] = (
            capo_odb.types.cloud_exadata_infrastructure.serialize_aws_json_1_0(
                value["cloud_exadata_infrastructure"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetCloudExadataInfrastructureOutput:
    out: GetCloudExadataInfrastructureOutput = {}  # type: ignore[typeddict-item]
    if "cloudExadataInfrastructure" in data:
        import capo_odb.types.cloud_exadata_infrastructure

        out["cloud_exadata_infrastructure"] = (
            capo_odb.types.cloud_exadata_infrastructure.deserialize_aws_json_1_0(
                data["cloudExadataInfrastructure"]
            )
        )
    return out
