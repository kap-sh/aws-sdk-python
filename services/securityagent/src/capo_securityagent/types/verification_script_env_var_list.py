"""Generated from Smithy shape ``com.amazonaws.securityagent#VerificationScriptEnvVarList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.verification_script_env_var

VerificationScriptEnvVarList: TypeAlias = list[
    "capo_securityagent.types.verification_script_env_var.VerificationScriptEnvVar"
]


# --- restJson1 ser/de ---
def serialize_json(value: VerificationScriptEnvVarList) -> list:
    import capo_securityagent.types.verification_script_env_var

    out: list = []
    for item in value:
        out.append(
            capo_securityagent.types.verification_script_env_var.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> VerificationScriptEnvVarList:
    import capo_securityagent.types.verification_script_env_var

    out: VerificationScriptEnvVarList = []
    for item in data:
        out.append(
            capo_securityagent.types.verification_script_env_var.deserialize_json(item)
        )
    return out
