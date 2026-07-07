"""Generated from Smithy shape ``com.amazonaws.securityir#OptInFeature``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_security_ir.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_security_ir.types.opt_in_feature_name


class OptInFeature(TypedDict, closed=True):
    feature_name: "aws_sdk_security_ir.types.opt_in_feature_name.OptInFeatureName"
    """<p/>"""
    is_enabled: "bool"
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: OptInFeature) -> dict:
    out: dict = {}
    import aws_sdk_security_ir.types.opt_in_feature_name

    out["featureName"] = aws_sdk_security_ir.types.opt_in_feature_name.serialize_json(
        value["feature_name"]
    )
    out["isEnabled"] = value["is_enabled"]
    return out


def deserialize_json(data: dict) -> OptInFeature:
    out: OptInFeature = {}  # type: ignore[typeddict-item]
    if "featureName" in data:
        import aws_sdk_security_ir.types.opt_in_feature_name

        out["feature_name"] = (
            aws_sdk_security_ir.types.opt_in_feature_name.deserialize_json(
                data["featureName"]
            )
        )
    else:
        raise DeserializationError("OptInFeature.feature_name required")
    if "isEnabled" in data:
        out["is_enabled"] = data["isEnabled"]
    else:
        raise DeserializationError("OptInFeature.is_enabled required")
    return out
