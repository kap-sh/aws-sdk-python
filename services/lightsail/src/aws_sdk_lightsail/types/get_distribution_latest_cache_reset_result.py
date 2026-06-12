"""Generated from Smithy shape ``com.amazonaws.lightsail#GetDistributionLatestCacheResetResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.iso_date
    import aws_sdk_lightsail.types.string


class GetDistributionLatestCacheResetResult(TypedDict):
    status: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The status of the last cache reset.</p>"""
    create_time: NotRequired["aws_sdk_lightsail.types.iso_date.IsoDate"]
    """<p>The timestamp of the last cache reset (<code>1479734909.17</code>) in Unix time format.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDistributionLatestCacheResetResult) -> dict:
    out: dict = {}
    if "status" in value:
        out["status"] = value["status"]
    if "create_time" in value:
        import aws_sdk_lightsail.types.iso_date

        out["createTime"] = aws_sdk_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["create_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDistributionLatestCacheResetResult:
    out: GetDistributionLatestCacheResetResult = {}  # type: ignore[typeddict-item]
    if "status" in data:
        out["status"] = data["status"]
    if "createTime" in data:
        import aws_sdk_lightsail.types.iso_date

        out["create_time"] = aws_sdk_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["createTime"]
        )
    return out
