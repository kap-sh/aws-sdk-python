"""Generated from Smithy shape ``com.amazonaws.mailmanager#DeleteRuleSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.rule_set_id


class DeleteRuleSetRequest(TypedDict, closed=True):
    rule_set_id: "aws_sdk_mailmanager.types.rule_set_id.RuleSetId"
    """<p>The identifier of an existing rule set resource to delete.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteRuleSetRequest) -> dict:
    out: dict = {}
    out["RuleSetId"] = value["rule_set_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteRuleSetRequest:
    out: DeleteRuleSetRequest = {}  # type: ignore[typeddict-item]
    if "RuleSetId" in data:
        out["rule_set_id"] = data["RuleSetId"]
    else:
        raise DeserializationError("DeleteRuleSetRequest.rule_set_id required")
    return out
