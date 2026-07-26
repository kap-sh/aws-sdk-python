"""Generated from Smithy shape ``com.amazonaws.qbusiness#RuleConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_qbusiness.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_qbusiness.types.content_blocker_rule
    import capo_qbusiness.types.content_retrieval_rule


class _RuleConfiguration_contentBlockerRule(TypedDict, closed=True):
    contentBlockerRule: "capo_qbusiness.types.content_blocker_rule.ContentBlockerRule"


class _RuleConfiguration_contentRetrievalRule(TypedDict, closed=True):
    contentRetrievalRule: (
        "capo_qbusiness.types.content_retrieval_rule.ContentRetrievalRule"
    )


RuleConfiguration: TypeAlias = (
    _RuleConfiguration_contentBlockerRule | _RuleConfiguration_contentRetrievalRule
)


# --- restJson1 ser/de ---
def serialize_json(value: RuleConfiguration) -> dict:
    if "contentBlockerRule" in value:
        import capo_qbusiness.types.content_blocker_rule

        return {
            "contentBlockerRule": capo_qbusiness.types.content_blocker_rule.serialize_json(
                value["contentBlockerRule"]
            )
        }
    elif "contentRetrievalRule" in value:
        import capo_qbusiness.types.content_retrieval_rule

        return {
            "contentRetrievalRule": capo_qbusiness.types.content_retrieval_rule.serialize_json(
                value["contentRetrievalRule"]
            )
        }
    else:
        raise SerializationError("RuleConfiguration: no variant present")


def deserialize_json(data: dict) -> RuleConfiguration:
    if "contentBlockerRule" in data:
        import capo_qbusiness.types.content_blocker_rule

        return {
            "contentBlockerRule": capo_qbusiness.types.content_blocker_rule.deserialize_json(
                data["contentBlockerRule"]
            )
        }
    elif "contentRetrievalRule" in data:
        import capo_qbusiness.types.content_retrieval_rule

        return {
            "contentRetrievalRule": capo_qbusiness.types.content_retrieval_rule.deserialize_json(
                data["contentRetrievalRule"]
            )
        }
    else:
        raise DeserializationError("RuleConfiguration: no recognized variant key")
