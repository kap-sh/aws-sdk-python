"""Generated from Smithy shape ``com.amazonaws.dynamodb#WriteRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.delete_request
    import capo_dynamodb.types.put_request


class WriteRequest(TypedDict, closed=True):
    put_request: NotRequired["capo_dynamodb.types.put_request.PutRequest"]
    """<p>A request to perform a <code>PutItem</code> operation.</p>"""
    delete_request: NotRequired["capo_dynamodb.types.delete_request.DeleteRequest"]
    """<p>A request to perform a <code>DeleteItem</code> operation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WriteRequest) -> dict:
    out: dict = {}
    if "put_request" in value:
        import capo_dynamodb.types.put_request

        out["PutRequest"] = capo_dynamodb.types.put_request.serialize_aws_json_1_0(
            value["put_request"]
        )
    if "delete_request" in value:
        import capo_dynamodb.types.delete_request

        out["DeleteRequest"] = (
            capo_dynamodb.types.delete_request.serialize_aws_json_1_0(
                value["delete_request"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> WriteRequest:
    out: WriteRequest = {}  # type: ignore[typeddict-item]
    if "PutRequest" in data:
        import capo_dynamodb.types.put_request

        out["put_request"] = capo_dynamodb.types.put_request.deserialize_aws_json_1_0(
            data["PutRequest"]
        )
    if "DeleteRequest" in data:
        import capo_dynamodb.types.delete_request

        out["delete_request"] = (
            capo_dynamodb.types.delete_request.deserialize_aws_json_1_0(
                data["DeleteRequest"]
            )
        )
    return out
