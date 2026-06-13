"""Generated from Smithy shape ``com.amazonaws.odb#GetOdbNetworkInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_odb.types.resource_id_or_arn


class GetOdbNetworkInput(TypedDict):
    odb_network_id: "aws_sdk_odb.types.resource_id_or_arn.ResourceIdOrArn"
    """<p>The unique identifier of the ODB network.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetOdbNetworkInput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> GetOdbNetworkInput:
    out: GetOdbNetworkInput = {}  # type: ignore[typeddict-item]
    return out
