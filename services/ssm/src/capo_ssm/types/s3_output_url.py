"""Generated from Smithy shape ``com.amazonaws.ssm#S3OutputUrl``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.url


class S3OutputUrl(TypedDict, closed=True):
    output_url: NotRequired["capo_ssm.types.url.Url"]
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
