"""Generated from Smithy shape ``com.amazonaws.macie2#CreateMemberRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.account_detail
    import capo_macie2.types.tag_map


class CreateMemberRequest(TypedDict, closed=True):
    account: NotRequired["capo_macie2.types.account_detail.AccountDetail"]
    """<p>The details of the account to associate with the administrator account.</p>"""
    tags: NotRequired["capo_macie2.types.tag_map.TagMap"]
    """<p>A map of key-value pairs that specifies the tags to associate with the account in Amazon Macie.</p> <p>An account can have a maximum of 50 tags. Each tag consists of a tag key and an associated tag value. The maximum length of a tag key is 128 characters. The maximum length of a tag value is 256 characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMemberRequest) -> dict:
    out: dict = {}
    if "account" in value:
        import capo_macie2.types.account_detail

        out["account"] = capo_macie2.types.account_detail.serialize_json(
            value["account"]
        )
    if "tags" in value:
        import capo_macie2.types.tag_map

        out["tags"] = capo_macie2.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateMemberRequest:
    out: CreateMemberRequest = {}  # type: ignore[typeddict-item]
    if "account" in data:
        import capo_macie2.types.account_detail

        out["account"] = capo_macie2.types.account_detail.deserialize_json(
            data["account"]
        )
    if "tags" in data:
        import capo_macie2.types.tag_map

        out["tags"] = capo_macie2.types.tag_map.deserialize_json(data["tags"])
    return out
