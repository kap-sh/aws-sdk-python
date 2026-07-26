"""Generated from Smithy shape ``com.amazonaws.kafka#ServerlessSasl``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.iam


class ServerlessSasl(TypedDict, closed=True):
    iam: NotRequired["capo_kafka.types.iam.Iam"]
    """<p>Indicates whether IAM access control is enabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServerlessSasl) -> dict:
    out: dict = {}
    if "iam" in value:
        import capo_kafka.types.iam

        out["iam"] = capo_kafka.types.iam.serialize_json(value["iam"])
    return out


def deserialize_json(data: dict) -> ServerlessSasl:
    out: ServerlessSasl = {}  # type: ignore[typeddict-item]
    if "iam" in data:
        import capo_kafka.types.iam

        out["iam"] = capo_kafka.types.iam.deserialize_json(data["iam"])
    return out
