"""Generated from Smithy shape ``com.amazonaws.memorydb#CreateACLResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.acl


class CreateACLResponse(TypedDict):
    acl: NotRequired["aws_sdk_memorydb.types.acl.ACL"]
    """<p>The newly-created Access Control List.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateACLResponse) -> dict:
    out: dict = {}
    if "acl" in value:
        import aws_sdk_memorydb.types.acl

        out["ACL"] = aws_sdk_memorydb.types.acl.serialize_aws_json_1_1(value["acl"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateACLResponse:
    out: CreateACLResponse = {}  # type: ignore[typeddict-item]
    if "ACL" in data:
        import aws_sdk_memorydb.types.acl

        out["acl"] = aws_sdk_memorydb.types.acl.deserialize_aws_json_1_1(data["ACL"])
    return out
