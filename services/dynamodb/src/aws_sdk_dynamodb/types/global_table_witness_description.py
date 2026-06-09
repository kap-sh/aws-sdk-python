"""Generated from Smithy shape ``com.amazonaws.dynamodb#GlobalTableWitnessDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.region_name
    import aws_sdk_dynamodb.types.witness_status


class GlobalTableWitnessDescription(TypedDict):
    region_name: NotRequired["aws_sdk_dynamodb.types.region_name.RegionName"]
    """<p>The name of the Amazon Web Services Region that serves as a witness for the MRSC global table.</p>"""
    witness_status: NotRequired["aws_sdk_dynamodb.types.witness_status.WitnessStatus"]
    """<p>The current status of the witness Region in the MRSC global table.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GlobalTableWitnessDescription) -> dict:
    out: dict = {}
    if "region_name" in value:
        out["RegionName"] = value["region_name"]
    if "witness_status" in value:
        import aws_sdk_dynamodb.types.witness_status

        out["WitnessStatus"] = (
            aws_sdk_dynamodb.types.witness_status.serialize_aws_json_1_0(
                value["witness_status"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GlobalTableWitnessDescription:
    out: GlobalTableWitnessDescription = {}  # type: ignore[typeddict-item]
    if "RegionName" in data:
        out["region_name"] = data["RegionName"]
    if "WitnessStatus" in data:
        import aws_sdk_dynamodb.types.witness_status

        out["witness_status"] = (
            aws_sdk_dynamodb.types.witness_status.deserialize_aws_json_1_0(
                data["WitnessStatus"]
            )
        )
    return out
