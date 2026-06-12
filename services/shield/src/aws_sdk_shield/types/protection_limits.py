"""Generated from Smithy shape ``com.amazonaws.shield#ProtectionLimits``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_shield.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_shield.types.limits


class ProtectionLimits(TypedDict):
    protected_resource_type_limits: "aws_sdk_shield.types.limits.Limits"
    """<p>The maximum number of resource types that you can specify in a protection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProtectionLimits) -> dict:
    out: dict = {}
    import aws_sdk_shield.types.limits

    out["ProtectedResourceTypeLimits"] = (
        aws_sdk_shield.types.limits.serialize_aws_json_1_1(
            value["protected_resource_type_limits"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProtectionLimits:
    out: ProtectionLimits = {}  # type: ignore[typeddict-item]
    if "ProtectedResourceTypeLimits" in data:
        import aws_sdk_shield.types.limits

        out["protected_resource_type_limits"] = (
            aws_sdk_shield.types.limits.deserialize_aws_json_1_1(
                data["ProtectedResourceTypeLimits"]
            )
        )
    else:
        raise DeserializationError(
            "ProtectionLimits.protected_resource_type_limits required"
        )
    return out
