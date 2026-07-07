"""Generated from Smithy shape ``com.amazonaws.kafka#VpcConnectivity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.vpc_connectivity_client_authentication


class VpcConnectivity(TypedDict, closed=True):
    client_authentication: NotRequired[
        "aws_sdk_kafka.types.vpc_connectivity_client_authentication.VpcConnectivityClientAuthentication"
    ]
    """<p>Includes all client authentication information for VPC connectivity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcConnectivity) -> dict:
    out: dict = {}
    if "client_authentication" in value:
        import aws_sdk_kafka.types.vpc_connectivity_client_authentication

        out["clientAuthentication"] = (
            aws_sdk_kafka.types.vpc_connectivity_client_authentication.serialize_json(
                value["client_authentication"]
            )
        )
    return out


def deserialize_json(data: dict) -> VpcConnectivity:
    out: VpcConnectivity = {}  # type: ignore[typeddict-item]
    if "clientAuthentication" in data:
        import aws_sdk_kafka.types.vpc_connectivity_client_authentication

        out["client_authentication"] = (
            aws_sdk_kafka.types.vpc_connectivity_client_authentication.deserialize_json(
                data["clientAuthentication"]
            )
        )
    return out
