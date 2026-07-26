"""Generated from Smithy shape ``com.amazonaws.wafregional#CreateSqlInjectionMatchSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_waf_regional.errors import DeserializationError

if TYPE_CHECKING:
    import capo_waf_regional.types.change_token
    import capo_waf_regional.types.resource_name


class CreateSqlInjectionMatchSetRequest(TypedDict, closed=True):
    name: "capo_waf_regional.types.resource_name.ResourceName"
    """<p>A friendly name or description for the <a>SqlInjectionMatchSet</a> that you're creating. You can't change <code>Name</code> after you create the <code>SqlInjectionMatchSet</code>.</p>"""
    change_token: "capo_waf_regional.types.change_token.ChangeToken"
    """<p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateSqlInjectionMatchSetRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["ChangeToken"] = value["change_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateSqlInjectionMatchSetRequest:
    out: CreateSqlInjectionMatchSetRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateSqlInjectionMatchSetRequest.name required")
    if "ChangeToken" in data:
        out["change_token"] = data["ChangeToken"]
    else:
        raise DeserializationError(
            "CreateSqlInjectionMatchSetRequest.change_token required"
        )
    return out
