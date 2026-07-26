"""Generated from Smithy shape ``com.amazonaws.appsync#SyncConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.conflict_detection_type
    import capo_appsync.types.conflict_handler_type
    import capo_appsync.types.lambda_conflict_handler_config


class SyncConfig(TypedDict, closed=True):
    conflict_handler: NotRequired[
        "capo_appsync.types.conflict_handler_type.ConflictHandlerType"
    ]
    """<p>The Conflict Resolution strategy to perform in the event of a conflict.</p> <ul> <li> <p> <b>OPTIMISTIC_CONCURRENCY</b>: Resolve conflicts by rejecting mutations when versions don't match the latest version at the server.</p> </li> <li> <p> <b>AUTOMERGE</b>: Resolve conflicts with the Automerge conflict resolution strategy.</p> </li> <li> <p> <b>LAMBDA</b>: Resolve conflicts with an Lambda function supplied in the <code>LambdaConflictHandlerConfig</code>.</p> </li> </ul>"""
    conflict_detection: NotRequired[
        "capo_appsync.types.conflict_detection_type.ConflictDetectionType"
    ]
    """<p>The Conflict Detection strategy to use.</p> <ul> <li> <p> <b>VERSION</b>: Detect conflicts based on object versions for this resolver.</p> </li> <li> <p> <b>NONE</b>: Do not detect conflicts when invoking this resolver.</p> </li> </ul>"""
    lambda_conflict_handler_config: NotRequired[
        "capo_appsync.types.lambda_conflict_handler_config.LambdaConflictHandlerConfig"
    ]
    """<p>The <code>LambdaConflictHandlerConfig</code> when configuring <code>LAMBDA</code> as the Conflict Handler.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SyncConfig) -> dict:
    out: dict = {}
    if "conflict_handler" in value:
        import capo_appsync.types.conflict_handler_type

        out["conflictHandler"] = (
            capo_appsync.types.conflict_handler_type.serialize_json(
                value["conflict_handler"]
            )
        )
    if "conflict_detection" in value:
        import capo_appsync.types.conflict_detection_type

        out["conflictDetection"] = (
            capo_appsync.types.conflict_detection_type.serialize_json(
                value["conflict_detection"]
            )
        )
    if "lambda_conflict_handler_config" in value:
        import capo_appsync.types.lambda_conflict_handler_config

        out["lambdaConflictHandlerConfig"] = (
            capo_appsync.types.lambda_conflict_handler_config.serialize_json(
                value["lambda_conflict_handler_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> SyncConfig:
    out: SyncConfig = {}  # type: ignore[typeddict-item]
    if "conflictHandler" in data:
        import capo_appsync.types.conflict_handler_type

        out["conflict_handler"] = (
            capo_appsync.types.conflict_handler_type.deserialize_json(
                data["conflictHandler"]
            )
        )
    if "conflictDetection" in data:
        import capo_appsync.types.conflict_detection_type

        out["conflict_detection"] = (
            capo_appsync.types.conflict_detection_type.deserialize_json(
                data["conflictDetection"]
            )
        )
    if "lambdaConflictHandlerConfig" in data:
        import capo_appsync.types.lambda_conflict_handler_config

        out["lambda_conflict_handler_config"] = (
            capo_appsync.types.lambda_conflict_handler_config.deserialize_json(
                data["lambdaConflictHandlerConfig"]
            )
        )
    return out
