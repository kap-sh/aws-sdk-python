"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#AccountSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_account.types.unicode_string


class AccountSummary(TypedDict, closed=True):
    name: "aws_sdk_partnercentral_account.types.unicode_string.UnicodeString"
    """<p>The name associated with the AWS account.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AccountSummary) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AccountSummary:
    out: AccountSummary = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("AccountSummary.name required")
    return out
