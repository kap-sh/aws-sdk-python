"""Generated from Smithy shape ``com.amazonaws.odb#GetOdbPeeringConnectionOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_odb.types.odb_peering_connection


class GetOdbPeeringConnectionOutput(TypedDict):
    odb_peering_connection: NotRequired[
        "aws_sdk_odb.types.odb_peering_connection.OdbPeeringConnection"
    ]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetOdbPeeringConnectionOutput) -> dict:
    out: dict = {}
    if "odb_peering_connection" in value:
        import aws_sdk_odb.types.odb_peering_connection

        out["odbPeeringConnection"] = (
            aws_sdk_odb.types.odb_peering_connection.serialize_aws_json_1_0(
                value["odb_peering_connection"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetOdbPeeringConnectionOutput:
    out: GetOdbPeeringConnectionOutput = {}  # type: ignore[typeddict-item]
    if "odbPeeringConnection" in data:
        import aws_sdk_odb.types.odb_peering_connection

        out["odb_peering_connection"] = (
            aws_sdk_odb.types.odb_peering_connection.deserialize_aws_json_1_0(
                data["odbPeeringConnection"]
            )
        )
    return out
