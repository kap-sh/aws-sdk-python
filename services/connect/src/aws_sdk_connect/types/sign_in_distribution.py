"""Generated from Smithy shape ``com.amazonaws.connect#SignInDistribution``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.aws_region
    import aws_sdk_connect.types.boolean


class SignInDistribution(TypedDict):
    region: "aws_sdk_connect.types.aws_region.AwsRegion"
    """<p>The Amazon Web Services Region of the sign in distribution.</p>"""
    enabled: "aws_sdk_connect.types.boolean.Boolean"
    """<p>Whether sign in distribution is enabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SignInDistribution) -> dict:
    out: dict = {}
    out["Region"] = value["region"]
    out["Enabled"] = value.get("enabled", False)
    return out


def deserialize_json(data: dict) -> SignInDistribution:
    out: SignInDistribution = {}  # type: ignore[typeddict-item]
    if "Region" in data:
        out["region"] = data["Region"]
    else:
        raise DeserializationError("SignInDistribution.region required")
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    else:
        out["enabled"] = False
    return out
