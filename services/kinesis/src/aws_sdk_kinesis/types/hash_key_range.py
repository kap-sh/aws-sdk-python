"""Generated from Smithy shape ``com.amazonaws.kinesis#HashKeyRange``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_kinesis.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis.types.hash_key


class HashKeyRange(TypedDict):
    starting_hash_key: "aws_sdk_kinesis.types.hash_key.HashKey"
    """<p>The starting hash key of the hash key range.</p>"""
    ending_hash_key: "aws_sdk_kinesis.types.hash_key.HashKey"
    """<p>The ending hash key of the hash key range.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HashKeyRange) -> dict:
    out: dict = {}
    out["StartingHashKey"] = value["starting_hash_key"]
    out["EndingHashKey"] = value["ending_hash_key"]
    return out


def deserialize_aws_json_1_1(data: dict) -> HashKeyRange:
    out: HashKeyRange = {}  # type: ignore[typeddict-item]
    if "StartingHashKey" in data:
        out["starting_hash_key"] = data["StartingHashKey"]
    else:
        raise DeserializationError("HashKeyRange.starting_hash_key required")
    if "EndingHashKey" in data:
        out["ending_hash_key"] = data["EndingHashKey"]
    else:
        raise DeserializationError("HashKeyRange.ending_hash_key required")
    return out
