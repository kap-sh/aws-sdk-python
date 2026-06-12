"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#LambdaEndpointSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_migration_hub_refactor_spaces.types.lambda_arn


class LambdaEndpointSummary(TypedDict):
    arn: NotRequired["aws_sdk_migration_hub_refactor_spaces.types.lambda_arn.LambdaArn"]
    """<p>The Amazon Resource Name (ARN) of the Lambda endpoint. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LambdaEndpointSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> LambdaEndpointSummary:
    out: LambdaEndpointSummary = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
