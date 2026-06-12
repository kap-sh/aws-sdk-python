"""Generated from Smithy shape ``com.amazonaws.cloudtrail#ListPublicKeysResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.public_key_list
    import aws_sdk_cloudtrail.types.string


class ListPublicKeysResponse(TypedDict):
    public_key_list: NotRequired[
        "aws_sdk_cloudtrail.types.public_key_list.PublicKeyList"
    ]
    """<p>Contains an array of PublicKey objects.</p> <note> <p>The returned public keys may have validity time ranges that overlap.</p> </note>"""
    next_token: NotRequired["aws_sdk_cloudtrail.types.string.String"]
    """<p>Reserved for future use.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPublicKeysResponse) -> dict:
    out: dict = {}
    if "public_key_list" in value:
        import aws_sdk_cloudtrail.types.public_key_list

        out["PublicKeyList"] = (
            aws_sdk_cloudtrail.types.public_key_list.serialize_aws_json_1_1(
                value["public_key_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPublicKeysResponse:
    out: ListPublicKeysResponse = {}  # type: ignore[typeddict-item]
    if "PublicKeyList" in data:
        import aws_sdk_cloudtrail.types.public_key_list

        out["public_key_list"] = (
            aws_sdk_cloudtrail.types.public_key_list.deserialize_aws_json_1_1(
                data["PublicKeyList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
