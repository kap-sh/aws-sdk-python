"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotVersionReplicaSortBy``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_version_replica_sort_attribute
    import aws_sdk_lex_models_v2.types.sort_order


class BotVersionReplicaSortBy(TypedDict):
    attribute: "aws_sdk_lex_models_v2.types.bot_version_replica_sort_attribute.BotVersionReplicaSortAttribute"
    """<p>The attribute of the sort category for the version replicated bots.</p>"""
    order: "aws_sdk_lex_models_v2.types.sort_order.SortOrder"
    """<p>The order of the sort category for the version replicated bots.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BotVersionReplicaSortBy) -> dict:
    out: dict = {}
    import aws_sdk_lex_models_v2.types.bot_version_replica_sort_attribute

    out["attribute"] = (
        aws_sdk_lex_models_v2.types.bot_version_replica_sort_attribute.serialize_json(
            value["attribute"]
        )
    )
    import aws_sdk_lex_models_v2.types.sort_order

    out["order"] = aws_sdk_lex_models_v2.types.sort_order.serialize_json(value["order"])
    return out


def deserialize_json(data: dict) -> BotVersionReplicaSortBy:
    out: BotVersionReplicaSortBy = {}  # type: ignore[typeddict-item]
    if "attribute" in data:
        import aws_sdk_lex_models_v2.types.bot_version_replica_sort_attribute

        out["attribute"] = (
            aws_sdk_lex_models_v2.types.bot_version_replica_sort_attribute.deserialize_json(
                data["attribute"]
            )
        )
    else:
        raise DeserializationError("BotVersionReplicaSortBy.attribute required")
    if "order" in data:
        import aws_sdk_lex_models_v2.types.sort_order

        out["order"] = aws_sdk_lex_models_v2.types.sort_order.deserialize_json(
            data["order"]
        )
    else:
        raise DeserializationError("BotVersionReplicaSortBy.order required")
    return out
