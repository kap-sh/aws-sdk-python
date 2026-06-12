"""Generated from Smithy shape ``com.amazonaws.kafka#ListScramSecretsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__list_of__string
    import aws_sdk_kafka.types.__string


class ListScramSecretsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>Paginated results marker.</p>"""
    secret_arn_list: NotRequired[
        "aws_sdk_kafka.types.__list_of__string.__listOf__string"
    ]
    """<p>The list of scram secrets associated with the cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListScramSecretsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "secret_arn_list" in value:
        import aws_sdk_kafka.types.__list_of__string

        out["secretArnList"] = aws_sdk_kafka.types.__list_of__string.serialize_json(
            value["secret_arn_list"]
        )
    return out


def deserialize_json(data: dict) -> ListScramSecretsResponse:
    out: ListScramSecretsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "secretArnList" in data:
        import aws_sdk_kafka.types.__list_of__string

        out["secret_arn_list"] = aws_sdk_kafka.types.__list_of__string.deserialize_json(
            data["secretArnList"]
        )
    return out
