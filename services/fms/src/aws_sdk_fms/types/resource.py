"""Generated from Smithy shape ``com.amazonaws.fms#Resource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_fms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_fms.types.aws_account_id
    import aws_sdk_fms.types.identifier


class Resource(TypedDict, closed=True):
    uri: "aws_sdk_fms.types.identifier.Identifier"
    """<p>The resource's universal resource indicator (URI).</p>"""
    account_id: NotRequired["aws_sdk_fms.types.aws_account_id.AWSAccountId"]
    """<p>The Amazon Web Services account ID that the associated resource belongs to.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Resource) -> dict:
    out: dict = {}
    out["URI"] = value["uri"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Resource:
    out: Resource = {}  # type: ignore[typeddict-item]
    if "URI" in data:
        out["uri"] = data["URI"]
    else:
        raise DeserializationError("Resource.uri required")
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    return out
