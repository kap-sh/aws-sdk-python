"""Generated from Smithy shape ``com.amazonaws.ssoadmin#DescribeApplicationProviderRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.application_provider_arn


class DescribeApplicationProviderRequest(TypedDict):
    application_provider_arn: (
        "aws_sdk_sso_admin.types.application_provider_arn.ApplicationProviderArn"
    )
    """<p>Specifies the ARN of the application provider for which you want details.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeApplicationProviderRequest) -> dict:
    out: dict = {}
    out["ApplicationProviderArn"] = value["application_provider_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeApplicationProviderRequest:
    out: DescribeApplicationProviderRequest = {}  # type: ignore[typeddict-item]
    if "ApplicationProviderArn" in data:
        out["application_provider_arn"] = data["ApplicationProviderArn"]
    else:
        raise DeserializationError(
            "DescribeApplicationProviderRequest.application_provider_arn required"
        )
    return out
