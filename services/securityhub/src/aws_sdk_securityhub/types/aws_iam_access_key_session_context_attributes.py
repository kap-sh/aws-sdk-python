"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsIamAccessKeySessionContextAttributes``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.non_empty_string


class AwsIamAccessKeySessionContextAttributes(TypedDict):
    mfa_authenticated: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Indicates whether the session used multi-factor authentication (MFA).</p>"""
    creation_date: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    r"""<p>Indicates when the session was created.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href=\"https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps\">Timestamps</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsIamAccessKeySessionContextAttributes) -> dict:
    out: dict = {}
    if "mfa_authenticated" in value:
        out["MfaAuthenticated"] = value["mfa_authenticated"]
    if "creation_date" in value:
        out["CreationDate"] = value["creation_date"]
    return out


def deserialize_json(data: dict) -> AwsIamAccessKeySessionContextAttributes:
    out: AwsIamAccessKeySessionContextAttributes = {}  # type: ignore[typeddict-item]
    if "MfaAuthenticated" in data:
        out["mfa_authenticated"] = data["MfaAuthenticated"]
    if "CreationDate" in data:
        out["creation_date"] = data["CreationDate"]
    return out
