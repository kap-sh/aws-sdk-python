"""Generated from Smithy shape ``com.amazonaws.kafka#VpcConnectivityClientAuthentication``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.vpc_connectivity_sasl
    import aws_sdk_kafka.types.vpc_connectivity_tls


class VpcConnectivityClientAuthentication(TypedDict, closed=True):
    sasl: NotRequired["aws_sdk_kafka.types.vpc_connectivity_sasl.VpcConnectivitySasl"]
    """<p>SASL authentication type details for VPC connectivity.</p>"""
    tls: NotRequired["aws_sdk_kafka.types.vpc_connectivity_tls.VpcConnectivityTls"]
    """<p>TLS authentication type details for VPC connectivity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcConnectivityClientAuthentication) -> dict:
    out: dict = {}
    if "sasl" in value:
        import aws_sdk_kafka.types.vpc_connectivity_sasl

        out["sasl"] = aws_sdk_kafka.types.vpc_connectivity_sasl.serialize_json(
            value["sasl"]
        )
    if "tls" in value:
        import aws_sdk_kafka.types.vpc_connectivity_tls

        out["tls"] = aws_sdk_kafka.types.vpc_connectivity_tls.serialize_json(
            value["tls"]
        )
    return out


def deserialize_json(data: dict) -> VpcConnectivityClientAuthentication:
    out: VpcConnectivityClientAuthentication = {}  # type: ignore[typeddict-item]
    if "sasl" in data:
        import aws_sdk_kafka.types.vpc_connectivity_sasl

        out["sasl"] = aws_sdk_kafka.types.vpc_connectivity_sasl.deserialize_json(
            data["sasl"]
        )
    if "tls" in data:
        import aws_sdk_kafka.types.vpc_connectivity_tls

        out["tls"] = aws_sdk_kafka.types.vpc_connectivity_tls.deserialize_json(
            data["tls"]
        )
    return out
