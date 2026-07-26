"""Generated from Smithy shape ``com.amazonaws.kafka#ClientAuthentication``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.sasl
    import capo_kafka.types.tls
    import capo_kafka.types.unauthenticated


class ClientAuthentication(TypedDict, closed=True):
    sasl: NotRequired["capo_kafka.types.sasl.Sasl"]
    """<p>Details for ClientAuthentication using SASL.</p>"""
    tls: NotRequired["capo_kafka.types.tls.Tls"]
    """<p>Details for ClientAuthentication using TLS.</p>"""
    unauthenticated: NotRequired["capo_kafka.types.unauthenticated.Unauthenticated"]
    """<p>Contains information about unauthenticated traffic to the cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClientAuthentication) -> dict:
    out: dict = {}
    if "sasl" in value:
        import capo_kafka.types.sasl

        out["sasl"] = capo_kafka.types.sasl.serialize_json(value["sasl"])
    if "tls" in value:
        import capo_kafka.types.tls

        out["tls"] = capo_kafka.types.tls.serialize_json(value["tls"])
    if "unauthenticated" in value:
        import capo_kafka.types.unauthenticated

        out["unauthenticated"] = capo_kafka.types.unauthenticated.serialize_json(
            value["unauthenticated"]
        )
    return out


def deserialize_json(data: dict) -> ClientAuthentication:
    out: ClientAuthentication = {}  # type: ignore[typeddict-item]
    if "sasl" in data:
        import capo_kafka.types.sasl

        out["sasl"] = capo_kafka.types.sasl.deserialize_json(data["sasl"])
    if "tls" in data:
        import capo_kafka.types.tls

        out["tls"] = capo_kafka.types.tls.deserialize_json(data["tls"])
    if "unauthenticated" in data:
        import capo_kafka.types.unauthenticated

        out["unauthenticated"] = capo_kafka.types.unauthenticated.deserialize_json(
            data["unauthenticated"]
        )
    return out
