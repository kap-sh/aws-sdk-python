"""Generated from Smithy shape ``com.amazonaws.emr#UsernamePassword``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.xml_string_max_len256


class UsernamePassword(TypedDict, closed=True):
    username: NotRequired["capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"]
    """<p>The username associated with the temporary credentials that you use to connect to cluster endpoints.</p>"""
    password: NotRequired["capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"]
    """<p>The password associated with the temporary credentials that you use to connect to cluster endpoints.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UsernamePassword) -> dict:
    out: dict = {}
    if "username" in value:
        out["Username"] = value["username"]
    if "password" in value:
        out["Password"] = value["password"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UsernamePassword:
    out: UsernamePassword = {}  # type: ignore[typeddict-item]
    if "Username" in data:
        out["username"] = data["Username"]
    if "Password" in data:
        out["password"] = data["Password"]
    return out
