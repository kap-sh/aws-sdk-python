"""Generated from Smithy shape ``com.amazonaws.sagemaker#SourceIpConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cidrs


class SourceIpConfig(TypedDict):
    cidrs: NotRequired["aws_sdk_sagemaker.types.cidrs.Cidrs"]
    r"""<p>A list of one to ten <a href=\"https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html\">Classless Inter-Domain Routing</a> (CIDR) values.</p> <p>Maximum: Ten CIDR values</p> <note> <p>The following Length Constraints apply to individual CIDR values in the CIDR value list.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceIpConfig) -> dict:
    out: dict = {}
    if "cidrs" in value:
        import aws_sdk_sagemaker.types.cidrs

        out["Cidrs"] = aws_sdk_sagemaker.types.cidrs.serialize_aws_json_1_1(
            value["cidrs"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SourceIpConfig:
    out: SourceIpConfig = {}  # type: ignore[typeddict-item]
    if "Cidrs" in data:
        import aws_sdk_sagemaker.types.cidrs

        out["cidrs"] = aws_sdk_sagemaker.types.cidrs.deserialize_aws_json_1_1(
            data["Cidrs"]
        )
    return out
