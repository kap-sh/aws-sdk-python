"""Generated from Smithy shape ``com.amazonaws.dynamodb#DeleteGlobalSecondaryIndexAction``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.index_name


class DeleteGlobalSecondaryIndexAction(TypedDict):
    index_name: "aws_sdk_dynamodb.types.index_name.IndexName"
    """<p>The name of the global secondary index to be deleted.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteGlobalSecondaryIndexAction) -> dict:
    out: dict = {}
    out["IndexName"] = value["index_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteGlobalSecondaryIndexAction:
    out: DeleteGlobalSecondaryIndexAction = {}  # type: ignore[typeddict-item]
    if "IndexName" in data:
        out["index_name"] = data["IndexName"]
    else:
        raise DeserializationError(
            "DeleteGlobalSecondaryIndexAction.index_name required"
        )
    return out
