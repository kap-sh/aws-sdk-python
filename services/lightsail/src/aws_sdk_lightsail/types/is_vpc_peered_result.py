"""Generated from Smithy shape ``com.amazonaws.lightsail#IsVpcPeeredResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.boolean


class IsVpcPeeredResult(TypedDict):
    is_peered: NotRequired["aws_sdk_lightsail.types.boolean.boolean"]
    """<p>Returns <code>true</code> if the Lightsail VPC is peered; otherwise, <code>false</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IsVpcPeeredResult) -> dict:
    out: dict = {}
    if "is_peered" in value:
        out["isPeered"] = value["is_peered"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IsVpcPeeredResult:
    out: IsVpcPeeredResult = {}  # type: ignore[typeddict-item]
    if "isPeered" in data:
        out["is_peered"] = data["isPeered"]
    return out
