"""Generated from Smithy shape ``com.amazonaws.kms#ListAliasesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kms.types.key_id_type
    import aws_sdk_kms.types.limit_type
    import aws_sdk_kms.types.marker_type


class ListAliasesRequest(TypedDict):
    key_id: NotRequired["aws_sdk_kms.types.key_id_type.KeyIdType"]
    """<p>Lists only aliases that are associated with the specified KMS key. Enter a KMS key in your Amazon Web Services account. </p> <p>This parameter is optional. If you omit it, <code>ListAliases</code> returns all aliases in the account and Region.</p> <p>Specify the key ID or key ARN of the KMS key.</p> <p>For example:</p> <ul> <li> <p>Key ID: <code>1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> <li> <p>Key ARN: <code>arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> </ul> <p>To get the key ID and key ARN for a KMS key, use <a>ListKeys</a> or <a>DescribeKey</a>.</p>"""
    limit: NotRequired["aws_sdk_kms.types.limit_type.LimitType"]
    """<p>Use this parameter to specify the maximum number of items to return. When this value is present, KMS does not return more than the specified number of items, but it might return fewer.</p> <p>This value is optional. If you include a value, it must be between 1 and 100, inclusive. If you do not include a value, it defaults to 50.</p>"""
    marker: NotRequired["aws_sdk_kms.types.marker_type.MarkerType"]
    """<p>Use this parameter in a subsequent request after you receive a response with truncated results. Set it to the value of <code>NextMarker</code> from the truncated response you just received.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAliasesRequest) -> dict:
    out: dict = {}
    if "key_id" in value:
        out["KeyId"] = value["key_id"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAliasesRequest:
    out: ListAliasesRequest = {}  # type: ignore[typeddict-item]
    if "KeyId" in data:
        out["key_id"] = data["KeyId"]
    if "Limit" in data:
        out["limit"] = data["Limit"]
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
