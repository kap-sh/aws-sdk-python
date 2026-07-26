"""Generated from Smithy shape ``com.amazonaws.kafka#ListScramSecretsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__list_of__string
    import capo_kafka.types.__string


class ListScramSecretsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_kafka.types.__string.__string"]
    """<p>Paginated results marker.</p>"""
    secret_arn_list: NotRequired["capo_kafka.types.__list_of__string.__listOf__string"]
    """<p>The list of scram secrets associated with the cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListScramSecretsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "secret_arn_list" in value:
        import capo_kafka.types.__list_of__string

        out["secretArnList"] = capo_kafka.types.__list_of__string.serialize_json(
            value["secret_arn_list"]
        )
    return out


def deserialize_json(data: dict) -> ListScramSecretsResponse:
    out: ListScramSecretsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "secretArnList" in data:
        import capo_kafka.types.__list_of__string

        out["secret_arn_list"] = capo_kafka.types.__list_of__string.deserialize_json(
            data["secretArnList"]
        )
    return out
