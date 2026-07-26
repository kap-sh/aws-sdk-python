"""Generated from Smithy shape ``com.amazonaws.codeconnections#UpdateHostInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codeconnections.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codeconnections.types.host_arn
    import capo_codeconnections.types.url
    import capo_codeconnections.types.vpc_configuration


class UpdateHostInput(TypedDict, closed=True):
    host_arn: "capo_codeconnections.types.host_arn.HostArn"
    """<p>The Amazon Resource Name (ARN) of the host to be updated.</p>"""
    provider_endpoint: NotRequired["capo_codeconnections.types.url.Url"]
    """<p>The URL or endpoint of the host to be updated.</p>"""
    vpc_configuration: NotRequired[
        "capo_codeconnections.types.vpc_configuration.VpcConfiguration"
    ]
    """<p>The VPC configuration of the host to be updated. A VPC must be configured and the infrastructure to be represented by the host must already be connected to the VPC.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateHostInput) -> dict:
    out: dict = {}
    out["HostArn"] = value["host_arn"]
    if "provider_endpoint" in value:
        out["ProviderEndpoint"] = value["provider_endpoint"]
    if "vpc_configuration" in value:
        import capo_codeconnections.types.vpc_configuration

        out["VpcConfiguration"] = (
            capo_codeconnections.types.vpc_configuration.serialize_aws_json_1_0(
                value["vpc_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateHostInput:
    out: UpdateHostInput = {}  # type: ignore[typeddict-item]
    if "HostArn" in data:
        out["host_arn"] = data["HostArn"]
    else:
        raise DeserializationError("UpdateHostInput.host_arn required")
    if "ProviderEndpoint" in data:
        out["provider_endpoint"] = data["ProviderEndpoint"]
    if "VpcConfiguration" in data:
        import capo_codeconnections.types.vpc_configuration

        out["vpc_configuration"] = (
            capo_codeconnections.types.vpc_configuration.deserialize_aws_json_1_0(
                data["VpcConfiguration"]
            )
        )
    return out
