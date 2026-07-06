"""Generated from Smithy shape ``com.amazonaws.licensemanager#ScriptRuleStatement``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_license_manager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.string


class ScriptRuleStatement(TypedDict, closed=True):
    key_to_match: "aws_sdk_license_manager.types.string.String"
    """<p>Key name to match against in the script rule evaluation.</p>"""
    script: "aws_sdk_license_manager.types.string.String"
    """<p>Script code used to evaluate the rule condition.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScriptRuleStatement) -> dict:
    out: dict = {}
    out["KeyToMatch"] = value["key_to_match"]
    out["Script"] = value["script"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ScriptRuleStatement:
    out: ScriptRuleStatement = {}  # type: ignore[typeddict-item]
    if "KeyToMatch" in data:
        out["key_to_match"] = data["KeyToMatch"]
    else:
        raise DeserializationError("ScriptRuleStatement.key_to_match required")
    if "Script" in data:
        out["script"] = data["Script"]
    else:
        raise DeserializationError("ScriptRuleStatement.script required")
    return out
