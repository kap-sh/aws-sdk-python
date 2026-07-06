"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeAliasInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.alias_id_or_arn


class DescribeAliasInput(TypedDict, closed=True):
    alias_id: NotRequired["aws_sdk_gamelift.types.alias_id_or_arn.AliasIdOrArn"]
    """<p>The unique identifier for the fleet alias that you want to retrieve. You can use either the alias ID or ARN value. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAliasInput) -> dict:
    out: dict = {}
    if "alias_id" in value:
        out["AliasId"] = value["alias_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAliasInput:
    out: DescribeAliasInput = {}  # type: ignore[typeddict-item]
    if "AliasId" in data:
        out["alias_id"] = data["AliasId"]
    return out
