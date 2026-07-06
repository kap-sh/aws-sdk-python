"""Generated from Smithy shape ``com.amazonaws.odb#ListCloudExadataInfrastructuresOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_odb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_odb.types.cloud_exadata_infrastructure_list


class ListCloudExadataInfrastructuresOutput(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    cloud_exadata_infrastructures: "aws_sdk_odb.types.cloud_exadata_infrastructure_list.CloudExadataInfrastructureList"
    """<p>The list of Exadata infrastructures along with their properties.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListCloudExadataInfrastructuresOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_odb.types.cloud_exadata_infrastructure_list

    out["cloudExadataInfrastructures"] = (
        aws_sdk_odb.types.cloud_exadata_infrastructure_list.serialize_aws_json_1_0(
            value["cloud_exadata_infrastructures"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListCloudExadataInfrastructuresOutput:
    out: ListCloudExadataInfrastructuresOutput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "cloudExadataInfrastructures" in data:
        import aws_sdk_odb.types.cloud_exadata_infrastructure_list

        out["cloud_exadata_infrastructures"] = (
            aws_sdk_odb.types.cloud_exadata_infrastructure_list.deserialize_aws_json_1_0(
                data["cloudExadataInfrastructures"]
            )
        )
    else:
        raise DeserializationError(
            "ListCloudExadataInfrastructuresOutput.cloud_exadata_infrastructures required"
        )
    return out
