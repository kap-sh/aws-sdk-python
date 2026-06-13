"""Generated from Smithy shape ``com.amazonaws.omics#RunConfigurationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_omics.types.vpc_config_response


class RunConfigurationsResponse(TypedDict):
    vpc_config: NotRequired["aws_sdk_omics.types.vpc_config_response.VpcConfigResponse"]
    """<p>VPC configuration for workflow runs with computed VPC ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RunConfigurationsResponse) -> dict:
    out: dict = {}
    if "vpc_config" in value:
        import aws_sdk_omics.types.vpc_config_response

        out["vpcConfig"] = aws_sdk_omics.types.vpc_config_response.serialize_json(
            value["vpc_config"]
        )
    return out


def deserialize_json(data: dict) -> RunConfigurationsResponse:
    out: RunConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if "vpcConfig" in data:
        import aws_sdk_omics.types.vpc_config_response

        out["vpc_config"] = aws_sdk_omics.types.vpc_config_response.deserialize_json(
            data["vpcConfig"]
        )
    return out
