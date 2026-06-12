"""Generated from Smithy shape ``com.amazonaws.ssm#InstanceAssociationOutputLocation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.s3_output_location


class InstanceAssociationOutputLocation(TypedDict):
    s3_location: NotRequired["aws_sdk_ssm.types.s3_output_location.S3OutputLocation"]
    """<p>An S3 bucket where you want to store the results of this request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceAssociationOutputLocation) -> dict:
    out: dict = {}
    if "s3_location" in value:
        import aws_sdk_ssm.types.s3_output_location

        out["S3Location"] = aws_sdk_ssm.types.s3_output_location.serialize_aws_json_1_1(
            value["s3_location"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceAssociationOutputLocation:
    out: InstanceAssociationOutputLocation = {}  # type: ignore[typeddict-item]
    if "S3Location" in data:
        import aws_sdk_ssm.types.s3_output_location

        out["s3_location"] = (
            aws_sdk_ssm.types.s3_output_location.deserialize_aws_json_1_1(
                data["S3Location"]
            )
        )
    return out
