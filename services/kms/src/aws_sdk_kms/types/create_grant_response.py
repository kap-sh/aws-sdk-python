"""Generated from Smithy shape ``com.amazonaws.kms#CreateGrantResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kms.types.grant_id_type
    import aws_sdk_kms.types.grant_token_type


class CreateGrantResponse(TypedDict):
    grant_token: NotRequired["aws_sdk_kms.types.grant_token_type.GrantTokenType"]
    """<p>The grant token.</p> <p>Use a grant token when your permission to call this operation comes from a new grant that has not yet achieved <i>eventual consistency</i>. For more information, see <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/grants.html#grant_token\">Grant token</a> and <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/using-grant-token.html\">Using a grant token</a> in the <i>Key Management Service Developer Guide</i>.</p>"""
    grant_id: NotRequired["aws_sdk_kms.types.grant_id_type.GrantIdType"]
    """<p>The unique identifier for the grant.</p> <p>You can use the <code>GrantId</code> in a <a>ListGrants</a>, <a>RetireGrant</a>, or <a>RevokeGrant</a> operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateGrantResponse) -> dict:
    out: dict = {}
    if "grant_token" in value:
        out["GrantToken"] = value["grant_token"]
    if "grant_id" in value:
        out["GrantId"] = value["grant_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateGrantResponse:
    out: CreateGrantResponse = {}  # type: ignore[typeddict-item]
    if "GrantToken" in data:
        out["grant_token"] = data["GrantToken"]
    if "GrantId" in data:
        out["grant_id"] = data["GrantId"]
    return out
