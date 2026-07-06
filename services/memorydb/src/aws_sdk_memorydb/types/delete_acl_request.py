"""Generated from Smithy shape ``com.amazonaws.memorydb#DeleteACLRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_memorydb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.string


class DeleteACLRequest(TypedDict, closed=True):
    acl_name: "aws_sdk_memorydb.types.string.String"
    """<p>The name of the Access Control List to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteACLRequest) -> dict:
    out: dict = {}
    out["ACLName"] = value["acl_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteACLRequest:
    out: DeleteACLRequest = {}  # type: ignore[typeddict-item]
    if "ACLName" in data:
        out["acl_name"] = data["ACLName"]
    else:
        raise DeserializationError("DeleteACLRequest.acl_name required")
    return out
