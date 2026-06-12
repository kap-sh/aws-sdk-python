"""Generated from Smithy shape ``com.amazonaws.shield#DescribeProtectionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_shield.types.protection


class DescribeProtectionResponse(TypedDict):
    protection: NotRequired["aws_sdk_shield.types.protection.Protection"]
    """<p>The <a>Protection</a> that you requested. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeProtectionResponse) -> dict:
    out: dict = {}
    if "protection" in value:
        import aws_sdk_shield.types.protection

        out["Protection"] = aws_sdk_shield.types.protection.serialize_aws_json_1_1(
            value["protection"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeProtectionResponse:
    out: DescribeProtectionResponse = {}  # type: ignore[typeddict-item]
    if "Protection" in data:
        import aws_sdk_shield.types.protection

        out["protection"] = aws_sdk_shield.types.protection.deserialize_aws_json_1_1(
            data["Protection"]
        )
    return out
