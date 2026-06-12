"""Generated from Smithy shape ``com.amazonaws.configservice#PutConfigRuleRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.config_rule
    import aws_sdk_config_service.types.tags_list


class PutConfigRuleRequest(TypedDict):
    config_rule: "aws_sdk_config_service.types.config_rule.ConfigRule"
    """<p>The rule that you want to add to your account.</p>"""
    tags: NotRequired["aws_sdk_config_service.types.tags_list.TagsList"]
    """<p>An array of tag object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutConfigRuleRequest) -> dict:
    out: dict = {}
    import aws_sdk_config_service.types.config_rule

    out["ConfigRule"] = aws_sdk_config_service.types.config_rule.serialize_aws_json_1_1(
        value["config_rule"]
    )
    if "tags" in value:
        import aws_sdk_config_service.types.tags_list

        out["Tags"] = aws_sdk_config_service.types.tags_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutConfigRuleRequest:
    out: PutConfigRuleRequest = {}  # type: ignore[typeddict-item]
    if "ConfigRule" in data:
        import aws_sdk_config_service.types.config_rule

        out["config_rule"] = (
            aws_sdk_config_service.types.config_rule.deserialize_aws_json_1_1(
                data["ConfigRule"]
            )
        )
    else:
        raise DeserializationError("PutConfigRuleRequest.config_rule required")
    if "Tags" in data:
        import aws_sdk_config_service.types.tags_list

        out["tags"] = aws_sdk_config_service.types.tags_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
