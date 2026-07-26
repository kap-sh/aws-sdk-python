"""Generated from Smithy shape ``com.amazonaws.kafka#VpcConnectivitySasl``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.vpc_connectivity_iam
    import capo_kafka.types.vpc_connectivity_scram


class VpcConnectivitySasl(TypedDict, closed=True):
    scram: NotRequired["capo_kafka.types.vpc_connectivity_scram.VpcConnectivityScram"]
    """<p>Details for SASL/SCRAM client authentication for VPC connectivity.</p>"""
    iam: NotRequired["capo_kafka.types.vpc_connectivity_iam.VpcConnectivityIam"]
    """<p>Details for SASL/IAM client authentication for VPC connectivity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcConnectivitySasl) -> dict:
    out: dict = {}
    if "scram" in value:
        import capo_kafka.types.vpc_connectivity_scram

        out["scram"] = capo_kafka.types.vpc_connectivity_scram.serialize_json(
            value["scram"]
        )
    if "iam" in value:
        import capo_kafka.types.vpc_connectivity_iam

        out["iam"] = capo_kafka.types.vpc_connectivity_iam.serialize_json(value["iam"])
    return out


def deserialize_json(data: dict) -> VpcConnectivitySasl:
    out: VpcConnectivitySasl = {}  # type: ignore[typeddict-item]
    if "scram" in data:
        import capo_kafka.types.vpc_connectivity_scram

        out["scram"] = capo_kafka.types.vpc_connectivity_scram.deserialize_json(
            data["scram"]
        )
    if "iam" in data:
        import capo_kafka.types.vpc_connectivity_iam

        out["iam"] = capo_kafka.types.vpc_connectivity_iam.deserialize_json(data["iam"])
    return out
