"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#LambdaEndpointConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_migration_hub_refactor_spaces.types.lambda_arn


class LambdaEndpointConfig(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_migration_hub_refactor_spaces.types.lambda_arn.LambdaArn"]
    """<p>The Amazon Resource Name (ARN) of the Lambda endpoint. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LambdaEndpointConfig) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> LambdaEndpointConfig:
    out: LambdaEndpointConfig = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
