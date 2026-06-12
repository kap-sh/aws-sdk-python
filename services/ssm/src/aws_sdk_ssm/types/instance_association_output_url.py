"""Generated from Smithy shape ``com.amazonaws.ssm#InstanceAssociationOutputUrl``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.s3_output_url


class InstanceAssociationOutputUrl(TypedDict):
    s3_output_url: NotRequired["aws_sdk_ssm.types.s3_output_url.S3OutputUrl"]
    """<p>The URL of S3 bucket where you want to store the results of this request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceAssociationOutputUrl) -> dict:
    out: dict = {}
    if "s3_output_url" in value:
        import aws_sdk_ssm.types.s3_output_url

        out["S3OutputUrl"] = aws_sdk_ssm.types.s3_output_url.serialize_aws_json_1_1(
            value["s3_output_url"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceAssociationOutputUrl:
    out: InstanceAssociationOutputUrl = {}  # type: ignore[typeddict-item]
    if "S3OutputUrl" in data:
        import aws_sdk_ssm.types.s3_output_url

        out["s3_output_url"] = aws_sdk_ssm.types.s3_output_url.deserialize_aws_json_1_1(
            data["S3OutputUrl"]
        )
    return out
