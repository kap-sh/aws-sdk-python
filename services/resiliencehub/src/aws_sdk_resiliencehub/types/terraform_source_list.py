"""Generated from Smithy shape ``com.amazonaws.resiliencehub#TerraformSourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.terraform_source

TerraformSourceList: TypeAlias = list[
    "aws_sdk_resiliencehub.types.terraform_source.TerraformSource"
]


# --- restJson1 ser/de ---
def serialize_json(value: TerraformSourceList) -> list:
    import aws_sdk_resiliencehub.types.terraform_source

    out: list = []
    for item in value:
        out.append(aws_sdk_resiliencehub.types.terraform_source.serialize_json(item))
    return out


def deserialize_json(data: list) -> TerraformSourceList:
    import aws_sdk_resiliencehub.types.terraform_source

    out: TerraformSourceList = []
    for item in data:
        out.append(aws_sdk_resiliencehub.types.terraform_source.deserialize_json(item))
    return out
