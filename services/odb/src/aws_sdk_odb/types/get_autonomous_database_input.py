"""Generated from Smithy shape ``com.amazonaws.odb#GetAutonomousDatabaseInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_odb.types.resource_id_or_arn


class GetAutonomousDatabaseInput(TypedDict, closed=True):
    autonomous_database_id: "aws_sdk_odb.types.resource_id_or_arn.ResourceIdOrArn"
    """<p>The unique identifier of the Autonomous Database to retrieve information about.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAutonomousDatabaseInput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAutonomousDatabaseInput:
    out: GetAutonomousDatabaseInput = {}  # type: ignore[typeddict-item]
    return out
