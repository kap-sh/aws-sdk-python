"""Generated from Smithy shape ``com.amazonaws.securityagent#VerificationScript``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.verification_script_env_var_list


class VerificationScript(TypedDict):
    script_type: NotRequired["str"]
    """<p>The type of script. Valid values are python and bash.</p>"""
    script_url: NotRequired["str"]
    """<p>URL to download the verification script.</p>"""
    instructions: NotRequired["str"]
    """<p>Instructions for running the verification script, including prerequisites and how to interpret results.</p>"""
    env_vars: NotRequired[
        "aws_sdk_securityagent.types.verification_script_env_var_list.VerificationScriptEnvVarList"
    ]
    """<p>The list of environment variables required to run the verification script.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VerificationScript) -> dict:
    out: dict = {}
    if "script_type" in value:
        out["scriptType"] = value["script_type"]
    if "script_url" in value:
        out["scriptUrl"] = value["script_url"]
    if "instructions" in value:
        out["instructions"] = value["instructions"]
    if "env_vars" in value:
        import aws_sdk_securityagent.types.verification_script_env_var_list

        out["envVars"] = (
            aws_sdk_securityagent.types.verification_script_env_var_list.serialize_json(
                value["env_vars"]
            )
        )
    return out


def deserialize_json(data: dict) -> VerificationScript:
    out: VerificationScript = {}  # type: ignore[typeddict-item]
    if "scriptType" in data:
        out["script_type"] = data["scriptType"]
    if "scriptUrl" in data:
        out["script_url"] = data["scriptUrl"]
    if "instructions" in data:
        out["instructions"] = data["instructions"]
    if "envVars" in data:
        import aws_sdk_securityagent.types.verification_script_env_var_list

        out["env_vars"] = (
            aws_sdk_securityagent.types.verification_script_env_var_list.deserialize_json(
                data["envVars"]
            )
        )
    return out
