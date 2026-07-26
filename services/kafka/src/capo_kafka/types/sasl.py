"""Generated from Smithy shape ``com.amazonaws.kafka#Sasl``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.iam
    import capo_kafka.types.scram


class Sasl(TypedDict, closed=True):
    scram: NotRequired["capo_kafka.types.scram.Scram"]
    """<p>Details for SASL/SCRAM client authentication.</p>"""
    iam: NotRequired["capo_kafka.types.iam.Iam"]
    """<p>Indicates whether IAM access control is enabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Sasl) -> dict:
    out: dict = {}
    if "scram" in value:
        import capo_kafka.types.scram

        out["scram"] = capo_kafka.types.scram.serialize_json(value["scram"])
    if "iam" in value:
        import capo_kafka.types.iam

        out["iam"] = capo_kafka.types.iam.serialize_json(value["iam"])
    return out


def deserialize_json(data: dict) -> Sasl:
    out: Sasl = {}  # type: ignore[typeddict-item]
    if "scram" in data:
        import capo_kafka.types.scram

        out["scram"] = capo_kafka.types.scram.deserialize_json(data["scram"])
    if "iam" in data:
        import capo_kafka.types.iam

        out["iam"] = capo_kafka.types.iam.deserialize_json(data["iam"])
    return out
