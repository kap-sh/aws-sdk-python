"""Generated from Smithy shape ``com.amazonaws.omics#RunConfigurations``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.vpc_config


class RunConfigurations(TypedDict, closed=True):
    vpc_config: NotRequired["aws_sdk_omics.types.vpc_config.VpcConfig"]
    """<p>VPC configuration for workflow runs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RunConfigurations) -> dict:
    out: dict = {}
    if "vpc_config" in value:
        import aws_sdk_omics.types.vpc_config

        out["vpcConfig"] = aws_sdk_omics.types.vpc_config.serialize_json(
            value["vpc_config"]
        )
    return out


def deserialize_json(data: dict) -> RunConfigurations:
    out: RunConfigurations = {}  # type: ignore[typeddict-item]
    if "vpcConfig" in data:
        import aws_sdk_omics.types.vpc_config

        out["vpc_config"] = aws_sdk_omics.types.vpc_config.deserialize_json(
            data["vpcConfig"]
        )
    return out
