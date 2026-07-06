"""Generated from Smithy shape ``com.amazonaws.evs#Secret``."""

from typing_extensions import NotRequired, TypedDict


class Secret(TypedDict, closed=True):
    secret_arn: NotRequired["str"]
    """<p> The Amazon Resource Name (ARN) of the secret.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Secret) -> dict:
    out: dict = {}
    if "secret_arn" in value:
        out["secretArn"] = value["secret_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Secret:
    out: Secret = {}  # type: ignore[typeddict-item]
    if "secretArn" in data:
        out["secret_arn"] = data["secretArn"]
    return out
