"""Generated from Smithy shape ``com.amazonaws.lightsail#ResetDistributionCacheResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.iso_date
    import aws_sdk_lightsail.types.operation
    import aws_sdk_lightsail.types.string


class ResetDistributionCacheResult(TypedDict, closed=True):
    status: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The status of the reset cache request.</p>"""
    create_time: NotRequired["aws_sdk_lightsail.types.iso_date.IsoDate"]
    """<p>The timestamp of the reset cache request (<code>1479734909.17</code>) in Unix time format.</p>"""
    operation: NotRequired["aws_sdk_lightsail.types.operation.Operation"]
    """<p>An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResetDistributionCacheResult) -> dict:
    out: dict = {}
    if "status" in value:
        out["status"] = value["status"]
    if "create_time" in value:
        import aws_sdk_lightsail.types.iso_date

        out["createTime"] = aws_sdk_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["create_time"]
        )
    if "operation" in value:
        import aws_sdk_lightsail.types.operation

        out["operation"] = aws_sdk_lightsail.types.operation.serialize_aws_json_1_1(
            value["operation"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResetDistributionCacheResult:
    out: ResetDistributionCacheResult = {}  # type: ignore[typeddict-item]
    if "status" in data:
        out["status"] = data["status"]
    if "createTime" in data:
        import aws_sdk_lightsail.types.iso_date

        out["create_time"] = aws_sdk_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["createTime"]
        )
    if "operation" in data:
        import aws_sdk_lightsail.types.operation

        out["operation"] = aws_sdk_lightsail.types.operation.deserialize_aws_json_1_1(
            data["operation"]
        )
    return out
