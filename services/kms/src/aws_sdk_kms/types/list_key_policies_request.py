"""Generated from Smithy shape ``com.amazonaws.kms#ListKeyPoliciesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kms.types.key_id_type
    import aws_sdk_kms.types.limit_type
    import aws_sdk_kms.types.marker_type


class ListKeyPoliciesRequest(TypedDict):
    key_id: "aws_sdk_kms.types.key_id_type.KeyIdType"
    """<p>Gets the names of key policies for the specified KMS key.</p> <p>Specify the key ID or key ARN of the KMS key.</p> <p>For example:</p> <ul> <li> <p>Key ID: <code>1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> <li> <p>Key ARN: <code>arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> </ul> <p>To get the key ID and key ARN for a KMS key, use <a>ListKeys</a> or <a>DescribeKey</a>.</p>"""
    limit: NotRequired["aws_sdk_kms.types.limit_type.LimitType"]
    """<p>Use this parameter to specify the maximum number of items to return. When this value is present, KMS does not return more than the specified number of items, but it might return fewer.</p> <p>This value is optional. If you include a value, it must be between 1 and 1000, inclusive. If you do not include a value, it defaults to 100.</p> <p>Only one policy can be attached to a key.</p>"""
    marker: NotRequired["aws_sdk_kms.types.marker_type.MarkerType"]
    """<p>Use this parameter in a subsequent request after you receive a response with truncated results. Set it to the value of <code>NextMarker</code> from the truncated response you just received.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListKeyPoliciesRequest) -> dict:
    out: dict = {}
    out["KeyId"] = value["key_id"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListKeyPoliciesRequest:
    out: ListKeyPoliciesRequest = {}  # type: ignore[typeddict-item]
    if "KeyId" in data:
        out["key_id"] = data["KeyId"]
    else:
        raise DeserializationError("ListKeyPoliciesRequest.key_id required")
    if "Limit" in data:
        out["limit"] = data["Limit"]
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
