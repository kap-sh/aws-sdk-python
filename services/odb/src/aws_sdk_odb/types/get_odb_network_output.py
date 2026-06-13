"""Generated from Smithy shape ``com.amazonaws.odb#GetOdbNetworkOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_odb.types.odb_network


class GetOdbNetworkOutput(TypedDict):
    odb_network: NotRequired["aws_sdk_odb.types.odb_network.OdbNetwork"]
    """<p>The ODB network.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetOdbNetworkOutput) -> dict:
    out: dict = {}
    if "odb_network" in value:
        import aws_sdk_odb.types.odb_network

        out["odbNetwork"] = aws_sdk_odb.types.odb_network.serialize_aws_json_1_0(
            value["odb_network"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetOdbNetworkOutput:
    out: GetOdbNetworkOutput = {}  # type: ignore[typeddict-item]
    if "odbNetwork" in data:
        import aws_sdk_odb.types.odb_network

        out["odb_network"] = aws_sdk_odb.types.odb_network.deserialize_aws_json_1_0(
            data["odbNetwork"]
        )
    return out
