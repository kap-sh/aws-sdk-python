"""Generated from Smithy shape ``com.amazonaws.gamelift#ResolveAliasInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.alias_id_or_arn


class ResolveAliasInput(TypedDict, closed=True):
    alias_id: NotRequired["aws_sdk_gamelift.types.alias_id_or_arn.AliasIdOrArn"]
    """<p>The unique identifier of the alias that you want to retrieve a fleet ID for. You can use either the alias ID or ARN value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResolveAliasInput) -> dict:
    out: dict = {}
    if "alias_id" in value:
        out["AliasId"] = value["alias_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResolveAliasInput:
    out: ResolveAliasInput = {}  # type: ignore[typeddict-item]
    if "AliasId" in data:
        out["alias_id"] = data["AliasId"]
    return out
