"""Generated from Smithy shape ``com.amazonaws.kafka#ClientAuthentication``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.sasl
    import aws_sdk_kafka.types.tls
    import aws_sdk_kafka.types.unauthenticated


class ClientAuthentication(TypedDict, closed=True):
    sasl: NotRequired["aws_sdk_kafka.types.sasl.Sasl"]
    """<p>Details for ClientAuthentication using SASL.</p>"""
    tls: NotRequired["aws_sdk_kafka.types.tls.Tls"]
    """<p>Details for ClientAuthentication using TLS.</p>"""
    unauthenticated: NotRequired["aws_sdk_kafka.types.unauthenticated.Unauthenticated"]
    """<p>Contains information about unauthenticated traffic to the cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClientAuthentication) -> dict:
    out: dict = {}
    if "sasl" in value:
        import aws_sdk_kafka.types.sasl

        out["sasl"] = aws_sdk_kafka.types.sasl.serialize_json(value["sasl"])
    if "tls" in value:
        import aws_sdk_kafka.types.tls

        out["tls"] = aws_sdk_kafka.types.tls.serialize_json(value["tls"])
    if "unauthenticated" in value:
        import aws_sdk_kafka.types.unauthenticated

        out["unauthenticated"] = aws_sdk_kafka.types.unauthenticated.serialize_json(
            value["unauthenticated"]
        )
    return out


def deserialize_json(data: dict) -> ClientAuthentication:
    out: ClientAuthentication = {}  # type: ignore[typeddict-item]
    if "sasl" in data:
        import aws_sdk_kafka.types.sasl

        out["sasl"] = aws_sdk_kafka.types.sasl.deserialize_json(data["sasl"])
    if "tls" in data:
        import aws_sdk_kafka.types.tls

        out["tls"] = aws_sdk_kafka.types.tls.deserialize_json(data["tls"])
    if "unauthenticated" in data:
        import aws_sdk_kafka.types.unauthenticated

        out["unauthenticated"] = aws_sdk_kafka.types.unauthenticated.deserialize_json(
            data["unauthenticated"]
        )
    return out
