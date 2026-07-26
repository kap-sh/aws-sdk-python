"""Generated from Smithy shape ``com.amazonaws.odb#GetOdbNetworkOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.odb_network


class GetOdbNetworkOutput(TypedDict, closed=True):
    odb_network: NotRequired["capo_odb.types.odb_network.OdbNetwork"]
    """<p>The ODB network.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetOdbNetworkOutput) -> dict:
    out: dict = {}
    if "odb_network" in value:
        import capo_odb.types.odb_network

        out["odbNetwork"] = capo_odb.types.odb_network.serialize_aws_json_1_0(
            value["odb_network"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetOdbNetworkOutput:
    out: GetOdbNetworkOutput = {}  # type: ignore[typeddict-item]
    if "odbNetwork" in data:
        import capo_odb.types.odb_network

        out["odb_network"] = capo_odb.types.odb_network.deserialize_aws_json_1_0(
            data["odbNetwork"]
        )
    return out
