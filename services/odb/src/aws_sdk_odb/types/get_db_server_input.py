"""Generated from Smithy shape ``com.amazonaws.odb#GetDbServerInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_odb.types.resource_id
    import aws_sdk_odb.types.resource_id_or_arn


class GetDbServerInput(TypedDict, closed=True):
    cloud_exadata_infrastructure_id: (
        "aws_sdk_odb.types.resource_id_or_arn.ResourceIdOrArn"
    )
    """<p>The unique identifier of the Oracle Exadata infrastructure that contains the database server.</p>"""
    db_server_id: "aws_sdk_odb.types.resource_id.ResourceId"
    """<p>The unique identifier of the database server to retrieve information about.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetDbServerInput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> GetDbServerInput:
    out: GetDbServerInput = {}  # type: ignore[typeddict-item]
    return out
