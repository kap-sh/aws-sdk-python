"""Generated from Smithy shape ``com.amazonaws.kafka#ServerlessClientAuthentication``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.serverless_sasl


class ServerlessClientAuthentication(TypedDict, closed=True):
    sasl: NotRequired["capo_kafka.types.serverless_sasl.ServerlessSasl"]
    """<p>Details for ClientAuthentication using SASL.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServerlessClientAuthentication) -> dict:
    out: dict = {}
    if "sasl" in value:
        import capo_kafka.types.serverless_sasl

        out["sasl"] = capo_kafka.types.serverless_sasl.serialize_json(value["sasl"])
    return out


def deserialize_json(data: dict) -> ServerlessClientAuthentication:
    out: ServerlessClientAuthentication = {}  # type: ignore[typeddict-item]
    if "sasl" in data:
        import capo_kafka.types.serverless_sasl

        out["sasl"] = capo_kafka.types.serverless_sasl.deserialize_json(data["sasl"])
    return out
