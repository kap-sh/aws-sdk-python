"""Generated from Smithy shape ``com.amazonaws.configservice#PutConfigRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_config_service.types.config_rule
    import capo_config_service.types.tags_list


class PutConfigRuleRequest(TypedDict, closed=True):
    config_rule: "capo_config_service.types.config_rule.ConfigRule"
    """<p>The rule that you want to add to your account.</p>"""
    tags: NotRequired["capo_config_service.types.tags_list.TagsList"]
    """<p>An array of tag object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutConfigRuleRequest) -> dict:
    out: dict = {}
    import capo_config_service.types.config_rule

    out["ConfigRule"] = capo_config_service.types.config_rule.serialize_aws_json_1_1(
        value["config_rule"]
    )
    if "tags" in value:
        import capo_config_service.types.tags_list

        out["Tags"] = capo_config_service.types.tags_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutConfigRuleRequest:
    out: PutConfigRuleRequest = {}  # type: ignore[typeddict-item]
    if "ConfigRule" in data:
        import capo_config_service.types.config_rule

        out["config_rule"] = (
            capo_config_service.types.config_rule.deserialize_aws_json_1_1(
                data["ConfigRule"]
            )
        )
    else:
        raise DeserializationError("PutConfigRuleRequest.config_rule required")
    if "Tags" in data:
        import capo_config_service.types.tags_list

        out["tags"] = capo_config_service.types.tags_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
