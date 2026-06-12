"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#AwsSubmission``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.sales_involvement_type
    import aws_sdk_partnercentral_selling.types.visibility


class AwsSubmission(TypedDict):
    involvement_type: "aws_sdk_partnercentral_selling.types.sales_involvement_type.SalesInvolvementType"
    """<p>Specifies the type of AWS involvement in the opportunity, such as coselling, deal support, or technical consultation. This helps categorize the nature of AWS participation.</p>"""
    visibility: NotRequired[
        "aws_sdk_partnercentral_selling.types.visibility.Visibility"
    ]
    """<p>Determines who can view AWS involvement in the opportunity. Typically, this field is set to <code>Full</code> for most cases, but it may be restricted based on special program requirements or confidentiality needs.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AwsSubmission) -> dict:
    out: dict = {}
    import aws_sdk_partnercentral_selling.types.sales_involvement_type

    out["InvolvementType"] = (
        aws_sdk_partnercentral_selling.types.sales_involvement_type.serialize_aws_json_1_0(
            value["involvement_type"]
        )
    )
    if "visibility" in value:
        import aws_sdk_partnercentral_selling.types.visibility

        out["Visibility"] = (
            aws_sdk_partnercentral_selling.types.visibility.serialize_aws_json_1_0(
                value["visibility"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AwsSubmission:
    out: AwsSubmission = {}  # type: ignore[typeddict-item]
    if "InvolvementType" in data:
        import aws_sdk_partnercentral_selling.types.sales_involvement_type

        out["involvement_type"] = (
            aws_sdk_partnercentral_selling.types.sales_involvement_type.deserialize_aws_json_1_0(
                data["InvolvementType"]
            )
        )
    else:
        raise DeserializationError("AwsSubmission.involvement_type required")
    if "Visibility" in data:
        import aws_sdk_partnercentral_selling.types.visibility

        out["visibility"] = (
            aws_sdk_partnercentral_selling.types.visibility.deserialize_aws_json_1_0(
                data["Visibility"]
            )
        )
    return out
