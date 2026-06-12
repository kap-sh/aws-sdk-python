"""Generated from Smithy shape ``com.amazonaws.glacier#ListVaultsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glacier.types.string


class ListVaultsInput(TypedDict):
    account_id: "aws_sdk_glacier.types.string.string"
    """<p>The <code>AccountId</code> value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens ('-') in the ID.</p>"""
    marker: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>A string used for pagination. The marker specifies the vault ARN after which the listing of vaults should begin.</p>"""
    limit: NotRequired["int"]
    """<p>The maximum number of vaults to be returned. The default limit is 10. The number of vaults returned might be fewer than the specified limit, but the number of returned vaults never exceeds the limit.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListVaultsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListVaultsInput:
    out: ListVaultsInput = {}  # type: ignore[typeddict-item]
    return out
