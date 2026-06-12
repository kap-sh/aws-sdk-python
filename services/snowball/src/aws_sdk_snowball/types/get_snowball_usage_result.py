"""Generated from Smithy shape ``com.amazonaws.snowball#GetSnowballUsageResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_snowball.types.integer


class GetSnowballUsageResult(TypedDict):
    snowball_limit: NotRequired["aws_sdk_snowball.types.integer.Integer"]
    """<p>The service limit for number of Snow devices this account can have at once. The default service limit is 1 (one).</p>"""
    snowballs_in_use: NotRequired["aws_sdk_snowball.types.integer.Integer"]
    """<p>The number of Snow devices that this account is currently using.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSnowballUsageResult) -> dict:
    out: dict = {}
    if "snowball_limit" in value:
        out["SnowballLimit"] = value["snowball_limit"]
    if "snowballs_in_use" in value:
        out["SnowballsInUse"] = value["snowballs_in_use"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSnowballUsageResult:
    out: GetSnowballUsageResult = {}  # type: ignore[typeddict-item]
    if "SnowballLimit" in data:
        out["snowball_limit"] = data["SnowballLimit"]
    if "SnowballsInUse" in data:
        out["snowballs_in_use"] = data["SnowballsInUse"]
    return out
