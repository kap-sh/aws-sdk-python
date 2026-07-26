"""Generated from Smithy shape ``com.amazonaws.cloudtrail#ListPublicKeysResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.public_key_list
    import capo_cloudtrail.types.string


class ListPublicKeysResponse(TypedDict, closed=True):
    public_key_list: NotRequired["capo_cloudtrail.types.public_key_list.PublicKeyList"]
    """<p>Contains an array of PublicKey objects.</p> <note> <p>The returned public keys may have validity time ranges that overlap.</p> </note>"""
    next_token: NotRequired["capo_cloudtrail.types.string.String"]
    """<p>Reserved for future use.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPublicKeysResponse) -> dict:
    out: dict = {}
    if "public_key_list" in value:
        import capo_cloudtrail.types.public_key_list

        out["PublicKeyList"] = (
            capo_cloudtrail.types.public_key_list.serialize_aws_json_1_1(
                value["public_key_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPublicKeysResponse:
    out: ListPublicKeysResponse = {}  # type: ignore[typeddict-item]
    if "PublicKeyList" in data:
        import capo_cloudtrail.types.public_key_list

        out["public_key_list"] = (
            capo_cloudtrail.types.public_key_list.deserialize_aws_json_1_1(
                data["PublicKeyList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
