"""Generated from Smithy shape ``com.amazonaws.securityir#OptInFeatures``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_security_ir.types.opt_in_feature

OptInFeatures: TypeAlias = list["aws_sdk_security_ir.types.opt_in_feature.OptInFeature"]


# --- restJson1 ser/de ---
def serialize_json(value: OptInFeatures) -> list:
    import aws_sdk_security_ir.types.opt_in_feature

    out: list = []
    for item in value:
        out.append(aws_sdk_security_ir.types.opt_in_feature.serialize_json(item))
    return out


def deserialize_json(data: list) -> OptInFeatures:
    import aws_sdk_security_ir.types.opt_in_feature

    out: OptInFeatures = []
    for item in data:
        out.append(aws_sdk_security_ir.types.opt_in_feature.deserialize_json(item))
    return out
