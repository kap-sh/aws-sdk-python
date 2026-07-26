"""Generated from Smithy shape ``com.amazonaws.workspaces#AuthorizeIpRulesResult``."""

from typing_extensions import TypedDict


class AuthorizeIpRulesResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AuthorizeIpRulesResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> AuthorizeIpRulesResult:
    out: AuthorizeIpRulesResult = {}  # type: ignore[typeddict-item]
    return out
