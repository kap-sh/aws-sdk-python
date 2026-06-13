"""Generated from Smithy shape ``com.amazonaws.odb#GetCloudExadataInfrastructureOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_odb.types.cloud_exadata_infrastructure


class GetCloudExadataInfrastructureOutput(TypedDict):
    cloud_exadata_infrastructure: NotRequired[
        "aws_sdk_odb.types.cloud_exadata_infrastructure.CloudExadataInfrastructure"
    ]
    """<p>The Exadata infrastructure.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetCloudExadataInfrastructureOutput) -> dict:
    out: dict = {}
    if "cloud_exadata_infrastructure" in value:
        import aws_sdk_odb.types.cloud_exadata_infrastructure

        out["cloudExadataInfrastructure"] = (
            aws_sdk_odb.types.cloud_exadata_infrastructure.serialize_aws_json_1_0(
                value["cloud_exadata_infrastructure"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetCloudExadataInfrastructureOutput:
    out: GetCloudExadataInfrastructureOutput = {}  # type: ignore[typeddict-item]
    if "cloudExadataInfrastructure" in data:
        import aws_sdk_odb.types.cloud_exadata_infrastructure

        out["cloud_exadata_infrastructure"] = (
            aws_sdk_odb.types.cloud_exadata_infrastructure.deserialize_aws_json_1_0(
                data["cloudExadataInfrastructure"]
            )
        )
    return out
