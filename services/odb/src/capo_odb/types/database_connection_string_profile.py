"""Generated from Smithy shape ``com.amazonaws.odb#DatabaseConnectionStringProfile``."""

from typing_extensions import NotRequired, TypedDict


class DatabaseConnectionStringProfile(TypedDict, closed=True):
    consumer_group: NotRequired["str"]
    """<p>The consumer group associated with the connection string profile.</p>"""
    display_name: NotRequired["str"]
    """<p>The user-friendly name of the connection string profile.</p>"""
    host_format: NotRequired["str"]
    """<p>The host name format used in the connection string.</p>"""
    is_regional: NotRequired["bool"]
    """<p>Indicates whether the connection string profile is regional.</p>"""
    protocol: NotRequired["str"]
    """<p>The protocol used by the connection string profile.</p>"""
    session_mode: NotRequired["str"]
    """<p>The session mode of the connection string profile.</p>"""
    syntax_format: NotRequired["str"]
    """<p>The syntax format of the connection string profile.</p>"""
    tls_authentication: NotRequired["str"]
    """<p>The TLS authentication method used by the connection string profile.</p>"""
    value: NotRequired["str"]
    """<p>The connection string value of the profile.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DatabaseConnectionStringProfile) -> dict:
    out: dict = {}
    if "consumer_group" in value:
        out["consumerGroup"] = value["consumer_group"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "host_format" in value:
        out["hostFormat"] = value["host_format"]
    if "is_regional" in value:
        out["isRegional"] = value["is_regional"]
    if "protocol" in value:
        out["protocol"] = value["protocol"]
    if "session_mode" in value:
        out["sessionMode"] = value["session_mode"]
    if "syntax_format" in value:
        out["syntaxFormat"] = value["syntax_format"]
    if "tls_authentication" in value:
        out["tlsAuthentication"] = value["tls_authentication"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DatabaseConnectionStringProfile:
    out: DatabaseConnectionStringProfile = {}  # type: ignore[typeddict-item]
    if "consumerGroup" in data:
        out["consumer_group"] = data["consumerGroup"]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "hostFormat" in data:
        out["host_format"] = data["hostFormat"]
    if "isRegional" in data:
        out["is_regional"] = data["isRegional"]
    if "protocol" in data:
        out["protocol"] = data["protocol"]
    if "sessionMode" in data:
        out["session_mode"] = data["sessionMode"]
    if "syntaxFormat" in data:
        out["syntax_format"] = data["syntaxFormat"]
    if "tlsAuthentication" in data:
        out["tls_authentication"] = data["tlsAuthentication"]
    if "value" in data:
        out["value"] = data["value"]
    return out
