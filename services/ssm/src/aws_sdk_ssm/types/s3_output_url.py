"""Generated from Smithy shape ``com.amazonaws.ssm#S3OutputUrl``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.url


class S3OutputUrl(TypedDict):
    output_url: NotRequired["aws_sdk_ssm.types.url.Url"]
    """<p>A URL for an S3 bucket where you want to store the results of this request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3OutputUrl) -> dict:
    out: dict = {}
    if "output_url" in value:
        out["OutputUrl"] = value["output_url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3OutputUrl:
    out: S3OutputUrl = {}  # type: ignore[typeddict-item]
    if "OutputUrl" in data:
        out["output_url"] = data["OutputUrl"]
    return out
