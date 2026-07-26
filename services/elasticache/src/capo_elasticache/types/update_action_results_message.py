"""Generated from Smithy shape ``com.amazonaws.elasticache#UpdateActionResultsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.processed_update_action_list
    import capo_elasticache.types.unprocessed_update_action_list


class UpdateActionResultsMessage(TypedDict, closed=True):
    processed_update_actions: NotRequired[
        "capo_elasticache.types.processed_update_action_list.ProcessedUpdateActionList"
    ]
    """<p>Update actions that have been processed successfully</p>"""
    unprocessed_update_actions: NotRequired[
        "capo_elasticache.types.unprocessed_update_action_list.UnprocessedUpdateActionList"
    ]
    """<p>Update actions that haven't been processed successfully</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdateActionResultsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "processed_update_actions" in value:
        import capo_elasticache.types.processed_update_action_list

        capo_elasticache.types.processed_update_action_list.serialize_query(
            value["processed_update_actions"], pairs, f"{prefix}.ProcessedUpdateActions"
        )
    if "unprocessed_update_actions" in value:
        import capo_elasticache.types.unprocessed_update_action_list

        capo_elasticache.types.unprocessed_update_action_list.serialize_query(
            value["unprocessed_update_actions"],
            pairs,
            f"{prefix}.UnprocessedUpdateActions",
        )


def deserialize_query(el: Element) -> UpdateActionResultsMessage:
    out: UpdateActionResultsMessage = {}  # type: ignore[typeddict-item]
    child_processed_update_actions = el.find("ProcessedUpdateActions")
    if child_processed_update_actions is not None:
        import capo_elasticache.types.processed_update_action_list

        out["processed_update_actions"] = (
            capo_elasticache.types.processed_update_action_list.deserialize_query(
                child_processed_update_actions
            )
        )
    child_unprocessed_update_actions = el.find("UnprocessedUpdateActions")
    if child_unprocessed_update_actions is not None:
        import capo_elasticache.types.unprocessed_update_action_list

        out["unprocessed_update_actions"] = (
            capo_elasticache.types.unprocessed_update_action_list.deserialize_query(
                child_unprocessed_update_actions
            )
        )
    return out
