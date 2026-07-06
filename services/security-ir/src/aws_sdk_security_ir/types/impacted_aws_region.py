"""Generated from Smithy shape ``com.amazonaws.securityir#ImpactedAwsRegion``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_security_ir.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_security_ir.types.aws_region


class ImpactedAwsRegion(TypedDict, closed=True):
    region: "aws_sdk_security_ir.types.aws_region.AwsRegion"
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImpactedAwsRegion) -> dict:
    out: dict = {}
    import aws_sdk_security_ir.types.aws_region

    out["region"] = aws_sdk_security_ir.types.aws_region.serialize_json(value["region"])
    return out


def deserialize_json(data: dict) -> ImpactedAwsRegion:
    out: ImpactedAwsRegion = {}  # type: ignore[typeddict-item]
    if "region" in data:
        import aws_sdk_security_ir.types.aws_region

        out["region"] = aws_sdk_security_ir.types.aws_region.deserialize_json(
            data["region"]
        )
    else:
        raise DeserializationError("ImpactedAwsRegion.region required")
    return out
