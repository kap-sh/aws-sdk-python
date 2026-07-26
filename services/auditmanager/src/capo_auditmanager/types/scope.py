"""Generated from Smithy shape ``com.amazonaws.auditmanager#Scope``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.aws_accounts
    import capo_auditmanager.types.aws_services


class Scope(TypedDict, closed=True):
    aws_accounts: NotRequired["capo_auditmanager.types.aws_accounts.AWSAccounts"]
    """<p> The Amazon Web Services accounts that are included in the scope of the assessment. </p>"""
    aws_services: NotRequired["capo_auditmanager.types.aws_services.AWSServices"]
    """<p> The Amazon Web Services services that are included in the scope of the assessment. </p> <important> <p>This API parameter is no longer supported. If you use this parameter to specify one or more Amazon Web Services services, Audit Manager ignores this input. Instead, the value for <code>awsServices</code> will show as empty.</p> </important>"""


# --- restJson1 ser/de ---
def serialize_json(value: Scope) -> dict:
    out: dict = {}
    if "aws_accounts" in value:
        import capo_auditmanager.types.aws_accounts

        out["awsAccounts"] = capo_auditmanager.types.aws_accounts.serialize_json(
            value["aws_accounts"]
        )
    if "aws_services" in value:
        import capo_auditmanager.types.aws_services

        out["awsServices"] = capo_auditmanager.types.aws_services.serialize_json(
            value["aws_services"]
        )
    return out


def deserialize_json(data: dict) -> Scope:
    out: Scope = {}  # type: ignore[typeddict-item]
    if "awsAccounts" in data:
        import capo_auditmanager.types.aws_accounts

        out["aws_accounts"] = capo_auditmanager.types.aws_accounts.deserialize_json(
            data["awsAccounts"]
        )
    if "awsServices" in data:
        import capo_auditmanager.types.aws_services

        out["aws_services"] = capo_auditmanager.types.aws_services.deserialize_json(
            data["awsServices"]
        )
    return out
