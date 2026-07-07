"""Generated from Smithy shape ``com.amazonaws.guardduty#RdsDbUserDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.string


class RdsDbUserDetails(TypedDict, closed=True):
    user: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The user name used in the anomalous login attempt.</p>"""
    application: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The application name used in the anomalous login attempt.</p>"""
    database: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The name of the database instance involved in the anomalous login attempt.</p>"""
    ssl: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The version of the Secure Socket Layer (SSL) used for the network.</p>"""
    auth_method: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The authentication method used by the user involved in the finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RdsDbUserDetails) -> dict:
    out: dict = {}
    if "user" in value:
        out["user"] = value["user"]
    if "application" in value:
        out["application"] = value["application"]
    if "database" in value:
        out["database"] = value["database"]
    if "ssl" in value:
        out["ssl"] = value["ssl"]
    if "auth_method" in value:
        out["authMethod"] = value["auth_method"]
    return out


def deserialize_json(data: dict) -> RdsDbUserDetails:
    out: RdsDbUserDetails = {}  # type: ignore[typeddict-item]
    if "user" in data:
        out["user"] = data["user"]
    if "application" in data:
        out["application"] = data["application"]
    if "database" in data:
        out["database"] = data["database"]
    if "ssl" in data:
        out["ssl"] = data["ssl"]
    if "authMethod" in data:
        out["auth_method"] = data["authMethod"]
    return out
