"""Generated from Smithy shape ``com.amazonaws.iot#AuthResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.allowed
    import capo_iot.types.auth_decision
    import capo_iot.types.auth_info
    import capo_iot.types.denied
    import capo_iot.types.missing_context_values


class AuthResult(TypedDict, closed=True):
    auth_info: NotRequired["capo_iot.types.auth_info.AuthInfo"]
    """<p>Authorization information.</p>"""
    allowed: NotRequired["capo_iot.types.allowed.Allowed"]
    """<p>The policies and statements that allowed the specified action.</p>"""
    denied: NotRequired["capo_iot.types.denied.Denied"]
    """<p>The policies and statements that denied the specified action.</p>"""
    auth_decision: NotRequired["capo_iot.types.auth_decision.AuthDecision"]
    """<p>The final authorization decision of this scenario. Multiple statements are taken into account when determining the authorization decision. An explicit deny statement can override multiple allow statements.</p>"""
    missing_context_values: NotRequired[
        "capo_iot.types.missing_context_values.MissingContextValues"
    ]
    """<p>Contains any missing context values found while evaluating policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuthResult) -> dict:
    out: dict = {}
    if "auth_info" in value:
        import capo_iot.types.auth_info

        out["authInfo"] = capo_iot.types.auth_info.serialize_json(value["auth_info"])
    if "allowed" in value:
        import capo_iot.types.allowed

        out["allowed"] = capo_iot.types.allowed.serialize_json(value["allowed"])
    if "denied" in value:
        import capo_iot.types.denied

        out["denied"] = capo_iot.types.denied.serialize_json(value["denied"])
    if "auth_decision" in value:
        import capo_iot.types.auth_decision

        out["authDecision"] = capo_iot.types.auth_decision.serialize_json(
            value["auth_decision"]
        )
    if "missing_context_values" in value:
        import capo_iot.types.missing_context_values

        out["missingContextValues"] = (
            capo_iot.types.missing_context_values.serialize_json(
                value["missing_context_values"]
            )
        )
    return out


def deserialize_json(data: dict) -> AuthResult:
    out: AuthResult = {}  # type: ignore[typeddict-item]
    if "authInfo" in data:
        import capo_iot.types.auth_info

        out["auth_info"] = capo_iot.types.auth_info.deserialize_json(data["authInfo"])
    if "allowed" in data:
        import capo_iot.types.allowed

        out["allowed"] = capo_iot.types.allowed.deserialize_json(data["allowed"])
    if "denied" in data:
        import capo_iot.types.denied

        out["denied"] = capo_iot.types.denied.deserialize_json(data["denied"])
    if "authDecision" in data:
        import capo_iot.types.auth_decision

        out["auth_decision"] = capo_iot.types.auth_decision.deserialize_json(
            data["authDecision"]
        )
    if "missingContextValues" in data:
        import capo_iot.types.missing_context_values

        out["missing_context_values"] = (
            capo_iot.types.missing_context_values.deserialize_json(
                data["missingContextValues"]
            )
        )
    return out
