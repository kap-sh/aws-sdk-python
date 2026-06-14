"""Generated from Smithy shape ``com.amazonaws.grafana#AssertionAttributes``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_grafana.types.assertion_attribute


class AssertionAttributes(TypedDict):
    name: NotRequired["aws_sdk_grafana.types.assertion_attribute.AssertionAttribute"]
    r"""<p>The name of the attribute within the SAML assertion to use as the user full \"friendly\" names for SAML users.</p>"""
    login: NotRequired["aws_sdk_grafana.types.assertion_attribute.AssertionAttribute"]
    """<p>The name of the attribute within the SAML assertion to use as the login names for SAML users.</p>"""
    email: NotRequired["aws_sdk_grafana.types.assertion_attribute.AssertionAttribute"]
    """<p>The name of the attribute within the SAML assertion to use as the email names for SAML users.</p>"""
    groups: NotRequired["aws_sdk_grafana.types.assertion_attribute.AssertionAttribute"]
    r"""<p>The name of the attribute within the SAML assertion to use as the user full \"friendly\" names for user groups.</p>"""
    role: NotRequired["aws_sdk_grafana.types.assertion_attribute.AssertionAttribute"]
    """<p>The name of the attribute within the SAML assertion to use as the user roles.</p>"""
    org: NotRequired["aws_sdk_grafana.types.assertion_attribute.AssertionAttribute"]
    r"""<p>The name of the attribute within the SAML assertion to use as the user full \"friendly\" names for the users' organizations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssertionAttributes) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "login" in value:
        out["login"] = value["login"]
    if "email" in value:
        out["email"] = value["email"]
    if "groups" in value:
        out["groups"] = value["groups"]
    if "role" in value:
        out["role"] = value["role"]
    if "org" in value:
        out["org"] = value["org"]
    return out


def deserialize_json(data: dict) -> AssertionAttributes:
    out: AssertionAttributes = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "login" in data:
        out["login"] = data["login"]
    if "email" in data:
        out["email"] = data["email"]
    if "groups" in data:
        out["groups"] = data["groups"]
    if "role" in data:
        out["role"] = data["role"]
    if "org" in data:
        out["org"] = data["org"]
    return out
