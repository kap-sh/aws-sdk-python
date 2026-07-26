"""Generated from Smithy shape ``com.amazonaws.appsync#LambdaConflictHandlerConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.string


class LambdaConflictHandlerConfig(TypedDict, closed=True):
    lambda_conflict_handler_arn: NotRequired["capo_appsync.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the Lambda function to use as the Conflict Handler.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LambdaConflictHandlerConfig) -> dict:
    out: dict = {}
    if "lambda_conflict_handler_arn" in value:
        out["lambdaConflictHandlerArn"] = value["lambda_conflict_handler_arn"]
    return out


def deserialize_json(data: dict) -> LambdaConflictHandlerConfig:
    out: LambdaConflictHandlerConfig = {}  # type: ignore[typeddict-item]
    if "lambdaConflictHandlerArn" in data:
        out["lambda_conflict_handler_arn"] = data["lambdaConflictHandlerArn"]
    return out
