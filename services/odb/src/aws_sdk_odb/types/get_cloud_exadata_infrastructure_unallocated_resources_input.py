"""Generated from Smithy shape ``com.amazonaws.odb#GetCloudExadataInfrastructureUnallocatedResourcesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_odb.types.resource_id_or_arn
    import aws_sdk_odb.types.string_list


class GetCloudExadataInfrastructureUnallocatedResourcesInput(TypedDict, closed=True):
    cloud_exadata_infrastructure_id: (
        "aws_sdk_odb.types.resource_id_or_arn.ResourceIdOrArn"
    )
    """<p>The unique identifier of the Cloud Exadata infrastructure for which to retrieve unallocated resources.</p>"""
    db_servers: NotRequired["aws_sdk_odb.types.string_list.StringList"]
    """<p>The database servers to include in the unallocated resources query.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: GetCloudExadataInfrastructureUnallocatedResourcesInput,
) -> dict:
    out: dict = {}
    if "db_servers" in value:
        import aws_sdk_odb.types.string_list

        out["dbServers"] = aws_sdk_odb.types.string_list.serialize_aws_json_1_0(
            value["db_servers"]
        )
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> GetCloudExadataInfrastructureUnallocatedResourcesInput:
    out: GetCloudExadataInfrastructureUnallocatedResourcesInput = {}  # type: ignore[typeddict-item]
    if "dbServers" in data:
        import aws_sdk_odb.types.string_list

        out["db_servers"] = aws_sdk_odb.types.string_list.deserialize_aws_json_1_0(
            data["dbServers"]
        )
    return out
