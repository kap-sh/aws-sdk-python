"""Generated from Smithy shape ``com.amazonaws.gamelift#DeleteAliasInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.alias_id_or_arn


class DeleteAliasInput(TypedDict):
    alias_id: NotRequired["aws_sdk_gamelift.types.alias_id_or_arn.AliasIdOrArn"]
    """<p>A unique identifier of the alias that you want to delete. You can use either the alias ID or ARN value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAliasInput) -> dict:
    out: dict = {}
    if "alias_id" in value:
        out["AliasId"] = value["alias_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteAliasInput:
    out: DeleteAliasInput = {}  # type: ignore[typeddict-item]
    if "AliasId" in data:
        out["alias_id"] = data["AliasId"]
    return out
