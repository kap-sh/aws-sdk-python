"""Generated from Smithy shape ``com.amazonaws.wafregional#CreateWebACLMigrationStackResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_waf_regional.errors import DeserializationError

if TYPE_CHECKING:
    import capo_waf_regional.types.s3_object_url


class CreateWebACLMigrationStackResponse(TypedDict, closed=True):
    s3_object_url: "capo_waf_regional.types.s3_object_url.S3ObjectUrl"
    """<p>The URL of the template created in Amazon S3. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateWebACLMigrationStackResponse) -> dict:
    out: dict = {}
    out["S3ObjectUrl"] = value["s3_object_url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateWebACLMigrationStackResponse:
    out: CreateWebACLMigrationStackResponse = {}  # type: ignore[typeddict-item]
    if "S3ObjectUrl" in data:
        out["s3_object_url"] = data["S3ObjectUrl"]
    else:
        raise DeserializationError(
            "CreateWebACLMigrationStackResponse.s3_object_url required"
        )
    return out
