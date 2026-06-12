"""Generated from Smithy shape ``com.amazonaws.kafka#ServerlessSasl``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.iam


class ServerlessSasl(TypedDict):
    iam: NotRequired["aws_sdk_kafka.types.iam.Iam"]
    """<p>Indicates whether IAM access control is enabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServerlessSasl) -> dict:
    out: dict = {}
    if "iam" in value:
        import aws_sdk_kafka.types.iam

        out["iam"] = aws_sdk_kafka.types.iam.serialize_json(value["iam"])
    return out


def deserialize_json(data: dict) -> ServerlessSasl:
    out: ServerlessSasl = {}  # type: ignore[typeddict-item]
    if "iam" in data:
        import aws_sdk_kafka.types.iam

        out["iam"] = aws_sdk_kafka.types.iam.deserialize_json(data["iam"])
    return out
