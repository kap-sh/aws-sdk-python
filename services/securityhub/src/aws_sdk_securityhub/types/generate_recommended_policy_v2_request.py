"""Generated from Smithy shape ``com.amazonaws.securityhub#GenerateRecommendedPolicyV2Request``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class GenerateRecommendedPolicyV2Request(TypedDict):
    metadata_uid: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    """<p>The unique identifier (ID) of Security Hub OCSF findings found under the <code>metadata.uid</code> field of the finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GenerateRecommendedPolicyV2Request) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GenerateRecommendedPolicyV2Request:
    out: GenerateRecommendedPolicyV2Request = {}  # type: ignore[typeddict-item]
    return out
