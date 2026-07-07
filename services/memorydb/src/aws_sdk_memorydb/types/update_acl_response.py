"""Generated from Smithy shape ``com.amazonaws.memorydb#UpdateACLResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.acl


class UpdateACLResponse(TypedDict, closed=True):
    acl: NotRequired["aws_sdk_memorydb.types.acl.ACL"]
    """<p>The updated Access Control List.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateACLResponse) -> dict:
    out: dict = {}
    if "acl" in value:
        import aws_sdk_memorydb.types.acl

        out["ACL"] = aws_sdk_memorydb.types.acl.serialize_aws_json_1_1(value["acl"])
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateACLResponse:
    out: UpdateACLResponse = {}  # type: ignore[typeddict-item]
    if "ACL" in data:
        import aws_sdk_memorydb.types.acl

        out["acl"] = aws_sdk_memorydb.types.acl.deserialize_aws_json_1_1(data["ACL"])
    return out
