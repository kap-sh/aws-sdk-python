"""Generated from Smithy shape ``com.amazonaws.cloudhsm#GetConfigResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudhsm.types.string


class GetConfigResponse(TypedDict):
    config_type: NotRequired["aws_sdk_cloudhsm.types.string.String"]
    """<p>The type of credentials.</p>"""
    config_file: NotRequired["aws_sdk_cloudhsm.types.string.String"]
    """<p>The chrystoki.conf configuration file.</p>"""
    config_cred: NotRequired["aws_sdk_cloudhsm.types.string.String"]
    """<p>The certificate file containing the server.pem files of the HSMs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetConfigResponse) -> dict:
    out: dict = {}
    if "config_type" in value:
        out["ConfigType"] = value["config_type"]
    if "config_file" in value:
        out["ConfigFile"] = value["config_file"]
    if "config_cred" in value:
        out["ConfigCred"] = value["config_cred"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetConfigResponse:
    out: GetConfigResponse = {}  # type: ignore[typeddict-item]
    if "ConfigType" in data:
        out["config_type"] = data["ConfigType"]
    if "ConfigFile" in data:
        out["config_file"] = data["ConfigFile"]
    if "ConfigCred" in data:
        out["config_cred"] = data["ConfigCred"]
    return out
