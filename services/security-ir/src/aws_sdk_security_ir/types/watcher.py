"""Generated from Smithy shape ``com.amazonaws.securityir#Watcher``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_security_ir.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_security_ir.types.email_address
    import aws_sdk_security_ir.types.job_title
    import aws_sdk_security_ir.types.person_name


class Watcher(TypedDict):
    email: "aws_sdk_security_ir.types.email_address.EmailAddress"
    """<p/>"""
    name: NotRequired["aws_sdk_security_ir.types.person_name.PersonName"]
    """<p/>"""
    job_title: NotRequired["aws_sdk_security_ir.types.job_title.JobTitle"]
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: Watcher) -> dict:
    out: dict = {}
    out["email"] = value["email"]
    if "name" in value:
        out["name"] = value["name"]
    if "job_title" in value:
        out["jobTitle"] = value["job_title"]
    return out


def deserialize_json(data: dict) -> Watcher:
    out: Watcher = {}  # type: ignore[typeddict-item]
    if "email" in data:
        out["email"] = data["email"]
    else:
        raise DeserializationError("Watcher.email required")
    if "name" in data:
        out["name"] = data["name"]
    if "jobTitle" in data:
        out["job_title"] = data["jobTitle"]
    return out
